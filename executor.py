import pyautogui
import pygetwindow as gw

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
screenWidth, screenHeight(2560, 1440)

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
currentMouseX, currentMouseY(1314, 345)

pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.
pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
pyautogui.doubleClick()     # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
    pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# Shift key is released automatically.

pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.



gw.getAllTitles()
#('', 'C:\\WINDOWS\\system32\\cmd.exe - pipenv  shell - python', 'C:\\github\\PyGetWindow\\README.md • - Sublime Text', "asweigart/PyGetWindow: A simple, cross-platform module for obtaining GUI information on application's windows. - Google Chrome", 'Untitled - Notepad', 'C:\\Users\\Al\\Desktop\\xlibkey.py • - Sublime Text', 'https://tronche.com/gui/x/xlib/ - Google Chrome', 'Xlib Programming Manual: XGetWindowAttributes - Google Chrome', 'Generic Ubuntu Box [Running] - Oracle VM VirtualBox', 'Oracle VM VirtualBox Manager', 'Microsoft Edge', 'Microsoft Edge', 'Microsoft Edge', '', 'Microsoft Edge', 'Settings', 'Settings', 'Microsoft Store', 'Microsoft Store', '', '', 'Backup and Sync', 'Google Hangouts - asweigart@gmail.com', 'Downloads', '', '', 'Program Manager')

gw.getAllWindows()
#(Win32Window(hWnd=131318), Win32Window(hWnd=1050492), Win32Window(hWnd=67206), Win32Window(hWnd=66754), Win32Window(hWnd=264354), Win32Window(hWnd=329210), Win32Window(hWnd=1114374), Win32Window(hWnd=852550), Win32Window(hWnd=328358), Win32Window(hWnd=66998), Win32Window(hWnd=132508), Win32Window(hWnd=66964), Win32Window(hWnd=66882), Win32Window(hWnd=197282), Win32Window(hWnd=393880), Win32Window(hWnd=66810), Win32Window(hWnd=328466), Win32Window(hWnd=132332), Win32Window(hWnd=262904), Win32Window(hWnd=65962), Win32Window(hWnd=65956), Win32Window(hWnd=197522), Win32Window(hWnd=131944), Win32Window(hWnd=329334), Win32Window(hWnd=395034), Win32Window(hWnd=132928), Win32Window(hWnd=65882))

gw.getWindowsWithTitle('Untitled')
#(Win32Window(hWnd=264354),)

gw.getActiveWindow()
#Win32Window(hWnd=1050492)

gw.getActiveWindow().title
#'C:\\WINDOWS\\system32\\cmd.exe - pipenv  shell - python'

gw.getWindowsAt(10, 10)
#(Win32Window(hWnd=67206), Win32Window(hWnd=66754), Win32Window(hWnd=329210), Win32Window(hWnd=1114374), Win32Window(hWnd=852550), Win32Window(hWnd=132508), Win32Window(hWnd=66964), Win32Window(hWnd=66882), Win32Window(hWnd=197282), Win32Window(hWnd=393880), Win32Window(hWnd=66810), Win32Window(hWnd=328466), Win32Window(hWnd=395034), Win32Window(hWnd=132928), Win32Window(hWnd=65882))
#Window objects can be minimized/maximized/restored/activated/resized/moved/closed and also have attributes for their current position, size, and state.

notepadWindow = gw.getWindowsWithTitle('Untitled')[0]
notepadWindow.maximize()
notepadWindow.isMaximized
notepadWindow.minimize()
notepadWindow.restore()
notepadWindow.activate()
notepadWindow.resize(10, 10) # increase by 10, 10
notepadWindow.resizeTo(100, 100) # set size to 100x100
notepadWindow.move(10, 10) # move 10 pixels right and 10 down
notepadWindow.moveTo(10, 10) # move window to 10, 10
notepadWindow.size
#(132, 100)
notepadWindow.width
#132
notepadWindow.height
#100
notepadWindow.topleft
#(10, 10)
notepadWindow.top
#10
notepadWindow.left
#10
notepadWindow.bottomright
#(142, 110)
notepadWindow.close()