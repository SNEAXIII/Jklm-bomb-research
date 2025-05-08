from icecream import ic
from keyboard import is_pressed, write, press_and_release

from detector.UiControl import UiControl
from dataset.mot_api import get_mot_by_seq

ui = UiControl()


while True:
    if is_pressed("q"):
        break
    if is_pressed("ctrl"):
        if ui.is_my_turn():
            ic("a moi de jouer")
            syllabe = ui.copy_syllabe()
            mot = get_mot_by_seq(syllabe)
            write(mot)
            press_and_release("enter")
        else:
            ic("pas a moi de jouer")
