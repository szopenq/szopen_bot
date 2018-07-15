# from PIL import ImageGrab
import win32com.client
import win32gui
import win32api, win32con
import time, random, ctypes, sys
from desktopmagic.screengrab_win32 import saveRectToBmp


# shell = win32com.client.Dispatch("WScript.Shell")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class Bot():
    def __init__(self):
        self.oreSet = False
        self.running = True

    def run(self):
        self.getOrePosition()
        self.getWindowSize()
        self.mine()

    def mine(self):
        while self.running:
            self.clickOre()
            time.sleep(1.5)
            self.screenshot()
            time.sleep(15 + random.uniform(-3, 3))

    def screenshot(self):
        saveRectToBmp('img.bmp', rect=self.size)

    def getWindowSize(self):
        samia = win32gui.FindWindow(None, "Samia")
        self.size = win32gui.GetWindowRect(samia)

    def getOrePosition(self):
        print("Najedz na zyle i kliknij J na klawiaturze")
        while not self.oreSet:
            if win32api.GetAsyncKeyState(ord("J")):
                self.orePos = win32gui.GetCursorPos()
                self.oreSet = True
        print(self.orePos)

    def clickOre(self):
        print("KOPIE RUDE")
        win32api.SetCursorPos(self.orePos)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.005)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


if __name__ == "__main__":
    if is_admin():
        bot = Bot()
        bot.run()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()
