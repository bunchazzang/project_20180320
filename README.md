# Keylogger Program #

## Setting :
Python 3.5.2 </br>
windows7

## Contents : 
**S.py** - Keylogger Server <br>
**C.py** - Keylogger Client

[Module] [Download site1](http://www.lfd.uci.edu/~gohlke/pythonlibs/) OR
[Download site2](http://blog.naver.com/samsjang/220626195405)

**pywin32 - pywin32-221-cp35-cp35m-win32.whl** </br>
**pyHook - pyHook-1.5.1-cp35-cp35m-win32.whl**

## Preparations :
### Windows environment variable settings
When the program(Python 3.5.2) is installed, add the Python path to the Windows evironment variable.

**[User variable] - [path]**

If the installed folder is 'C:\python35', Add the following path to the end of the variable.

C:\python35;C:\python35\lib\site-packages;C:\python35\Scripts
___
### Install pywin32
**pip install pywin32-221-cp35-cp35m-win32.whl**

If the installed folder is 'C:\python35', 'C:\python35\Scripts' has pywin32_postintall.py.

**python C:\python35\Scripts\pywin32_postintall.py -install**
___
### Install pyHook ###
**pip install pyHook-1.5.1-cp35-cp35m-win32.whl**

___
### If you get the following error ###
TypeError : KeyboardSwitch() missing 8 required positional arguments : 'msg', 'vk_code',
'scan_code', 'ascii', 'flags', 'time', 'hwnd', and 'win_name'

Overwrite a **'_cpyHook.cp35-win32.pyd'** with an existing file

If the installed folder is 'C:\python35', The pyHook installation folder is in the following path.

C:\python35\Lib\site-packages\pyHook