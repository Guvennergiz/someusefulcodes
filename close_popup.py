import win32gui
import win32con
import time

# Note "pip install pywin32" for importing win32gui

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

closed_popup = False
while not closed_popup:
  # get a list of open windows
  top_windows = []
  win32gui.EnumWindows(windowEnumerationHandler, top_windows)
  # check name of open windows
  for i in top_windows:
      if "ambient temperature" in i[1].lower():
        # if this is the popup, close it
        print(i[1])
        win32gui.PostMessage(i[0],win32con.WM_CLOSE,0,0)
        closed_popup = True
  if not closed_popup:
        print("popup not found")
        time.sleep(1.)