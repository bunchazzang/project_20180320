import socketserver
import threading

HOST = ''
PORT = 9009
lock = threading.Lock()

class UserManager:
   def __init__(self):
      self.users = {}
      self.num = 1

   def addUser(self, conn, addr):
      username = "user" + str(self.num)
      self.num += 1
      
      # 새로운 사용자를 등록함
      lock.acquire()
      self.users[username] = (conn, addr)
      lock.release()

      self.sendMessageToAll('[%s] 사용자가 접속했습니다.' %username)
      print('+++ 접속된 PC 수 [%d]' %len(self.users))
        
      return username

   def removeUser(self, username):
      if username not in self.users:
         return

      lock.acquire()
      del self.users[username]
      lock.release()

      self.sendMessageToAll('[%s] 사용자와 접속이 끊어졌습니다..' %username)
      print('--- 접속된 PC 수 [%d]' %len(self.users))

   def messageHandler(self, username, msg):
      if msg[0] != '/':
         self.sendMessageToAll('[%s] %s' %(username, msg))
         return

      if msg.strip() == '/quit':
         self.removeUser(username)
         return -1

   def sendMessageToAll(self, msg):
      for conn, addr in self.users.values():
         conn.send(msg.encode())
          

class MyTcpHandler(socketserver.BaseRequestHandler):
   userman = UserManager()
    
   def handle(self):        
      print('[%s] 연결됨' %self.client_address[0])

      try:
         username = self.registerUsername()
         msg = self.request.recv(1024)
         while msg:
            print("[%s]"%(username))
            print(msg.decode())
            if self.userman.messageHandler(username, msg.decode()) == -1:
               self.request.close()
               break
            msg = self.request.recv(1024)
                
      except Exception as e:
         print(e)

      print('[%s] 접속종료' %self.client_address[0])
      self.userman.removeUser(username)

   def registerUsername(self):
      while True:
         username = self.userman.addUser(self.request, self.client_address)
         if username:
            return username

class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
        
def runServer():
   print('+++ 서버를 시작합니다.')
   print('+++ 서버를 끝내려면 Ctrl + C를 누르세요.')

   try:
      server = ChatingServer((HOST, PORT), MyTcpHandler)
      server.serve_forever()
   except KeyboardInterrupt:
      print('-- 서버를 종료합니다.')
      server.shutdown()
      server.server_close()

runServer()
