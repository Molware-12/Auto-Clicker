import time
import sys
from pynput.keyboard import Listener,KeyCode, Key
import pyautogui

class AutoClicker:
    def __init__(self, interval, start_key):
        self.interval = interval
        self.start_key = start_key
        self.running = False

    def on_press(self, key):
        """If the users start key is pressed, call the autoclick function. If 'e' is pressed, the program stops."""
        if key == KeyCode.from_char(self.start_key):
            self.running = True
            if self.running:
                print("AutoClicker started.")
                self.autoclick()
        if key == KeyCode.from_char("e"):
            print("Thanks for using the pyautoclicker!")
            sys.exit(0)

    def on_release(self, key):
        """If the escape key (Esc) is pressed, the autoclicker stops."""
        if key == Key.esc:
            self.running = False
            print("AutoClicker stopped.")

    def autoclick(self):
        """Clicks continuously while listening to the on_release function to know whether to the clicker or the program."""
        with Listener(on_release=self.on_release) as release_listener:
            while self.running:
                pyautogui.click()
                time.sleep(self.interval)
        return "AutoClicker stopped."
    def set_position(self, x, y):
        """Optional function, only use if you want clicks in a certain coordinate"""
        pyautogui.moveTo(x, y)

    def start_listener(self):
        with Listener(on_press=self.on_press) as press_listener:
            press_listener.join()

click = AutoClicker(float(input("Interval between clicks: ")), str(input("Key to start auto-clicking: ")))
click.set_position(100, 100)
click.start_listener()
