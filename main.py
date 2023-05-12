from kb import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split
from kmk.modules.tapdance import TapDance
from kmk.modules.capsword import CapsWord
from kmk.modules.oneshot import OneShot
from kmk.modules.combos import Combos, Chord

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(Split(use_pio = True))
keyboard.modules.append(TapDance())
keyboard.modules.append(CapsWord())
keyboard.modules.append(OneShot())
combos = Combos()
keyboard.modules.append(combos)

combos.combos = [
    Chord((34, 31), KC.TG(3), match_coord=True),
]

# LSFT = KC.TD(KC.OS(KC.LSFT), KC.CW)
RSFT = KC.OS(KC.RSFT)

keyboard.keymap = [
    [   #0
        KC.ESC,  KC.N1, KC.N2,   KC.N3,   KC.N4, KC.N5,                         KC.N6, KC.N7, KC.N8,   KC.N9,  KC.N0,   KC.BSPC,
        KC.TAB,  KC.Q,  KC.W,    KC.E,    KC.R,  KC.T,                          KC.Y,  KC.U,  KC.I,    KC.O,   KC.P,    KC.BSLS,
        KC.GRV,  KC.A,  KC.S,    KC.D,    KC.F,  KC.G,                          KC.H,  KC.J,  KC.K,    KC.L,   KC.SCLN, KC.QUOT,
        KC.NO,   KC.Z,  KC.X,    KC.C,    KC.V,  KC.B,                          KC.N,  KC.M,  KC.COMM, KC.DOT, KC.SLSH, KC.NO,
                        KC.LBRC, KC.RBRC,                                                      KC.MINS, KC.EQL,
                                                KC.MO(2), KC.SPC,      KC.ENT,  KC.MO(1),
                                                KC.LCTL,  KC.CW,       KC.BKDL, RSFT,
                                                KC.LALT,  KC.LGUI,     KC.PGUP, KC.PGDN
    ] ,
    [  #1
        KC.TRNS, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,                         KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.TRNS,
        KC.TRNS, KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                         KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.TRNS,
        KC.TRNS, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC,                       KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.NO,
        KC.TRNS, KC.GRV,  KC.MINS, KC.EQL,  KC.QUOT, KC.BSLS,                       KC.NO,   KC.NO,   KC.LBRC, KC.RBRC, KC.NO,   KC.TRNS,
                          KC.NO,   KC.NO,                                                            KC.NO,   KC.NO,
                                                KC.TRNS, KC.TRNS,      KC.TRNS, KC.NO,
                                                KC.TRNS, KC.TRNS,      KC.TRNS, KC.TRNS,
                                                KC.TRNS, KC.TRNS,      KC.TRNS, KC.TRNS
    ],
    [  #2
        KC.TRNS, KC.NO,  KC.NO,  KC.NO, KC.NO, KC.NO,                           KC.NO,   KC.NO,   KC.NO, KC.NO,   KC.NO, KC.NO,
        KC.NO,   KC.NO,  KC.NO,  KC.NO, KC.NO, KC.NO,                           KC.NO,   KC.NO,   KC.NO, KC.NO,   KC.NO, KC.NO,
        KC.NO,   KC.NO,  KC.NO,  KC.NO, KC.NO, KC.NO,                           KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, KC.NO, KC.NO,
        KC.NO,   KC.NO,  KC.NO,  KC.NO, KC.NO, KC.NO,                           KC.NO,   KC.NO,   KC.NO, KC.NO,   KC.NO, KC.NO,
                         KC.NO,  KC.NO,                                                           KC.NO, KC.NO,
                                                    KC.NO,   KC.TRNS,      KC.TRNS, KC.TRNS,
                                                    KC.TRNS, KC.TRNS,      KC.TRNS, KC.TRNS,
                                                    KC.TRNS, KC.TRNS,      KC.HOME, KC.END
    ],
    [  #3
        KC.ESC,  KC.GRV, KC.N1,   KC.N2,   KC.N3, KC.N4,                         KC.N6, KC.N7, KC.N8,   KC.N9,  KC.N0,   KC.BSPC,
        KC.TAB,  KC.TAB,  KC.Q,    KC.W,    KC.E,  KC.R,                          KC.Y,  KC.U,  KC.I,    KC.O,   KC.P,    KC.BSLS,
        KC.LSFT,  KC.NO,  KC.A,    KC.S,    KC.D,  KC.F,                          KC.H,  KC.J,  KC.K,    KC.L,   KC.SCLN, KC.QUOT,
        KC.LCTL, KC.LCTL,  KC.Z,    KC.X,    KC.C,  KC.V,                          KC.N,  KC.M,  KC.COMM, KC.DOT, KC.SLSH, KC.APP,
                        KC.NO, KC.NO,                                                      KC.MINS, KC.EQL,
                                                KC.NO, KC.SPC,      KC.NO,  KC.NO,
                                                KC.NO,    KC.NO,      KC.NO, KC.NO,
                                                KC.LALT,  KC.NO,     KC.NO, KC.NO
    ]
]

if __name__ == '__main__':
    keyboard.go()
