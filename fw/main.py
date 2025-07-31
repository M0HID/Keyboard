from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.digitalio import MatrixScanner
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
import board
import busio
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017
from kmk.scanners.encoder import RotaryioEncoder
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros


class MyKeyboard(KMKKeyboard):
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        mcp1 = MCP23017(i2c, address=0x20)
        mcp2 = MCP23017(i2c, address=0x21)

        self.row_pins = []
        for i in [0,1,2,3,4,5]:
            pin = mcp1.get_pin(i)
            self.row_pins.append(pin)

        self.col_pins = []
        for i in [6,7,8,9,10,11,12,13,14,15]:
            pin = mcp1.get_pin(i)
            self.col_pins.append(pin)
        for i in [0,1,2,3,4,5]:
            pin = mcp2.get_pin(i)
            self.col_pins.append(pin)

        super().__init__()

keyboard = MyKeyboard()

keyboard.extensions.append(MediaKeys())
macros = Macros()
keyboard.modules.append(macros)

keyboard.matrix = [
    MatrixScanner(
        cols=keyboard.col_pins,
        rows=keyboard.row_pins,
        diode_orientation=DiodeOrientation.COL2ROW,
        pull=digitalio.Pull.UP,
    ),
    RotaryioEncoder(
        pin_a=board.D7,
        pin_b=board.D8,
    ),
    KeysScanner(
        pins=[board.D6],
        value_when_pressed=False,
    )
]

keyboard.keymap = [
    [
        KC.ESC,    KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,   KC.PSCR,  KC.DEL,
        KC.GRV,    KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.MINS,  KC.EQL,   KC.BSPC,  KC.INS,
        KC.TAB,    KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.LBRC,  KC.RBRC,  KC.BSLS,  KC.HOME,
        KC.CAPS,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,  KC.ENT,            KC.PGUP,
        KC.LSFT,            KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,  KC.UP,    KC.PGDN,
        KC.LCTL,   KC.LGUI,  KC.LALT,                      KC.SPC,                       KC.RALT,  KC.RGUI,  KC.MO(1), KC.LEFT,  KC.DOWN,  KC.RGHT
    ]
]

keyboard.go()

