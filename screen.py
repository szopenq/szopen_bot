from PIL import ImageGrab
import win32com.client
import win32gui
import win32api, win32con
import time, random
from desktopmagic.screengrab_win32 import saveRectToBmp




def getWindowSize():
    samia = win32gui.FindWindow(None, "Samia")
    size = win32gui.GetWindowRect(samia)
    saveRectToBmp('img1.bmp', rect=size)

getWindowSize()