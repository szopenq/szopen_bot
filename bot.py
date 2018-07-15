from PIL import Image
import win32gui
import win32api, win32con
import time, random, ctypes, sys
from desktopmagic.screengrab_win32 import saveRectToBmp


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class Bot():
    def __init__(self):
        self.oreSet = False
        self.running = True

        self.img1 = Image.open("1.bmp")
        self.img2 = Image.open("2.bmp")
        self.img3 = Image.open("3.bmp")
        self.img4 = Image.open("4.bmp")

    def run(self):
        self.getOrePosition()
        self.getWindowSize()
        self.mine()

    def mine(self):
        while self.running:
            self.clickOre()
            self.screenshot()
            time.sleep(0.2)
            self.checkBot()
            time.sleep(15 + random.uniform(-3, 3))

    def screenshot(self):
        x0 = self.size[0] + 353
        y0 = self.size[1] + 212
        x1 = self.size[0] + 657
        y1 = self.size[1] + 312
        saveRectToBmp('pic.bmp', rect=(x0, y0, x1, y1))

    def checkBot(self):

        comp = Image.open("pic.bmp")
        if comp.tobytes() == self.img1.tobytes():
            print("[ANTI-BOT] - 1")
            self.clickAntiBot(1)
        elif comp.tobytes() == self.img2.tobytes():
            print("[ANTI-BOT] - 2")
            self.clickAntiBot(2)
        elif comp.tobytes() == self.img3.tobytes():
            print("[ANTI-BOT] - 3")
            self.clickAntiBot(3)
        elif comp.tobytes() == self.img4.tobytes():
            print("[ANTI-BOT] - 4")
            self.clickAntiBot(4)
        else:
            print("[ANTI-BOT] - NONE")

    def getWindowSize(self):
        samia = win32gui.FindWindow(None, "Samia")
        self.size = win32gui.GetWindowRect(samia)

    def getOrePosition(self):
        print("[INFO] - Najedz na zyle i kliknij J na klawiaturze")
        while not self.oreSet:
            if win32api.GetAsyncKeyState(ord("J")):
                self.orePos = win32gui.GetCursorPos()
                self.oreSet = True
        print(self.orePos)

    def clickOre(self):
        win32api.SetCursorPos(self.orePos)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.005)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(2)

    def clickAntiBot(self, number):
        w = int((self.size[2] - abs(self.size[0])) / 2)
        h = int((self.size[3] + abs(self.size[1])) / 2)

        if number == 1:
            win32api.SetCursorPos((w, h + 30))
        elif number == 2:
            win32api.SetCursorPos((w, h - 40))
        elif number == 3:
            win32api.SetCursorPos((w, h + 60))
        elif number == 4:
            win32api.SetCursorPos((w, h))
            
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.005)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        self.clickOre()


if __name__ == "__main__":
    if is_admin():
        bot = Bot()
        bot.run()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()
