from PIL import Image
import win32api, win32con, win32com.client, win32gui
import time, random, ctypes, sys
from desktopmagic.screengrab_win32 import saveRectToBmp


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class Bot():
    def __init__(self, botNumber=''):
        self.oreSet = False
        self.running = True
        self.shell = win32com.client.Dispatch("WScript.Shell")
        self.botNumber = botNumber
        self.saveFile = "pic" + str(botNumber) + ".bmp"

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
            self.checkBot()
            time.sleep(15 + random.uniform(-3, 3))

    def screenshot(self):
        x0 = self.size[0] + 353
        y0 = self.size[1] + 212
        x1 = self.size[0] + 657
        y1 = self.size[1] + 312
        saveRectToBmp(self.saveFile, rect=(x0, y0, x1, y1))

    def checkBot(self):
        self.screenshot()
        time.sleep(0.2)
        comp = Image.open(self.saveFile)
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
        samia = win32gui.GetForegroundWindow()
        if win32gui.GetWindowText(samia).lower() != "samia":
            raise Exception("Wrong window! - You need to be in Samia in order to activate the bot!")
        self.size = win32gui.GetWindowRect(samia)

    def getOrePosition(self):
        print("[INFO] - Najedz na zyle i kliknij J na klawiaturze")
        while not self.oreSet:
            if win32api.GetAsyncKeyState(ord("J")):
                self.orePos = win32gui.GetCursorPos()
                self.oreSet = True
        print("[INFO] - ORE POSTION: " + str(self.orePos))

    def clickOre(self):
        self.saveMousePos()
        win32api.SetCursorPos(self.orePos)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.005)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        self.returnMousePos()
        time.sleep(2)

    def clickAntiBot(self, number):
        self.saveMousePos()

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
        self.returnMousePos()
        self.clickOre()
        self.checkBot()

    def saveMousePos(self):
        self.oldPos = win32gui.GetCursorPos()
        self.activeWindow = win32gui.GetForegroundWindow()

    def returnMousePos(self):
        win32api.SetCursorPos(self.oldPos)
        try:
            self.shell.SendKeys('')  # Without this it will return an error
            win32gui.SetForegroundWindow(self.activeWindow)
        except:
            print("[EXCEPTION] - Error when chaning focus window")


if __name__ == "__main__":
    if is_admin():
        try:
            bot = Bot(sys.argv[1])
        except IndexError:
            bot = Bot()
        bot.run()
    else:
        arguments = " ".join(sys.argv[1:])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__ + " " + arguments, None, 1)
        sys.exit()
