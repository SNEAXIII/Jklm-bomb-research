from time import sleep
from typing import Optional

from icecream import ic
from pyperclip import paste

import pyautogui




class ImageNotFoundException(Exception):
    pass


RETRY = 10
TIMEOUT = 1
BOMB_IMAGE = "./images/bottom_bomb.png"
JOUE_IMAGE = "./images/joue.png"
CONFIDENCE = 0.90


class UiControl:
    def __init__(self):
        self.syllabe = None
        self.location: Optional[dict] = None
        try:
            self.set_bomb_location(BOMB_IMAGE)
        except ImageNotFoundException:
            print("BombNotFound")

    def get_bomb_location(self, image):
        for iteration in range(RETRY):
            print(f"Iteration {iteration + 1} of {RETRY}...")
            try:
                return pyautogui.locateOnScreen(image, confidence=CONFIDENCE)
            except Exception as e:
                print(f"Erreur lors de la détection de l'image : {repr(e)}")
                sleep(TIMEOUT)
                continue
            break
        return None

    def set_bomb_location(self, image) -> None:
        if self.location:
            print(f"Location already found: {self.location}")
        self.location = self.get_bomb_location(image)
        if not self.location:
            raise ImageNotFoundException(
                f"The bomb can't be located on the screen after {RETRY} attempts"
            )
        self.location = {
            "x": int(pyautogui.center(self.location)[0]),
            "y": int(self.location.top) - 20,
        }
        print(f"Bomb location : {self.location}")

    def copy_syllabe(self):
        if not self.location:
            return EnvironmentError("There is no self.region setup")
        # Copy
        pyautogui.doubleClick(**self.location, interval=0.1)
        with pyautogui.hold("ctrl"):
            pyautogui.press("c")
        self.syllabe = paste().lower()
        ic(self.syllabe)
        # Click outside
        pyautogui.moveTo(y=self.location["y"] + 50)
        pyautogui.click()
        return self.syllabe

    def is_my_turn(self):
        try:
            pyautogui.locateOnScreen(JOUE_IMAGE, confidence=CONFIDENCE, grayscale=False)
            return False
        except pyautogui.ImageNotFoundException:
            return True

if __name__ == "__main__":
    ui = UiControl()
    ui.copy_syllabe()
    ic(ui.syllabe)
    print(repr(ui.is_my_turn()))

