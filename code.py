# Main Keyboard Configuration - v0.9.5
import board
import pog
from keybow_2040_rgb import Keybow2040Leds
from kmk.extensions.rgb import RGB, AnimationModes


# check if we just want to run the coord_mappping Assistant
if pog.coordMappingAssistant:
    from coordmaphelper import KMKKeyboard
    if __name__ == '__main__':
        KMKKeyboard().go()
        exit()
else:
    from kb import KMKKeyboard

# set the required features for you keyboard and keymap
# add custom ones in the kb.py

keyboard = KMKKeyboard(features=pog.kbFeatures)

rgb = RGB(
    pixel_pin=0,
    pixels=Keybow2040Leds(16),
    num_pixels=16,
    animation_mode=AnimationModes.BREATHING_RAINBOW,
)

# manage settings for our modules and extensions here
keyboard.tapdance.tap_time = 200
keyboard.extensions = [rgb]

# Keymap
import keymap
keyboard.keymap = keymap.keymap

# Encoder Keymap if available
if pog.hasEncoders:
    keyboard.encoder_handler.map = keymap.encoderKeymap

# Execute the keyboard loop
if __name__ == '__main__':
    keyboard.go()
