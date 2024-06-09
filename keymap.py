# Keymap Autogenerated by Pog do not edit
from kmk.keys import KC
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.combos import Chord, Sequence

import pog
import customkeys

keymap = [
    [KC.LSFT(KC.LGUI(KC.N4)), simple_key_sequence((KC.LSFT(KC.LGUI(KC.N4)), KC.MACRO_SLEEP_MS(100), KC.SPC)), KC.END, KC.PGUP, KC.ESC, KC.UP, KC.ENT, KC.PGDOWN, KC.LEFT, KC.DOWN, KC.RIGHT, KC.LSFT, KC.LGUI(KC.SPC), KC.LGUI, KC.LALT, KC.SPC]
]

encoderKeymap = []
for l, layer in enumerate(pog.config['encoderKeymap']):
    layerEncoders = []
    for e, encoder in enumerate(layer):
        layerEncoders.append(tuple(map(eval, encoder)))
    encoderKeymap.append(tuple(layerEncoders))
