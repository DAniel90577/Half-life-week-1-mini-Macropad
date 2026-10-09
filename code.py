import board
from kmk.kmkkeyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

keyboard.matrix = KeysScanner(
    pins=[board.D6, board.D8,  board.D10,  board.D5, board.D7, board.D9],
    value_when_pressed=False,
    pull=True
)
keyboard.keymap = [
    [KC.A, KC.B, KC.C,
     KC.D, KC.E, KC.F]
]
if __name__ == '__main__':
    keyboard.go()