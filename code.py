# Name: Your Name Here
# Lab Number: CPX Lights and Sound Lab
# Date: 07/14/2025

from adafruit_circuitplayground.express import cpx
import time

# --- Global dictionaries ---

# Dictionary for musical note frequencies
notes_dict = {
    "A4": 440,
    "B4": 494,
    "C5": 523,
    "D5": 587,
    "E5": 659,
    "F5": 698,
    "G5": 784,
    "A5": 880,
    "B5": 988,
    "C6": 1047
}

# Dictionary for color names and RGB tuples
colors = {
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "purple": (255, 0, 255),
    "cyan": (0, 255, 255),
    "white": (255, 255, 255)
}

# --- Function to fill all pixels with a given color ---
def fill_pixels(color_tuple):
    cpx.pixels.fill(color_tuple)

# --- Main loop ---
while True:
    if cpx.touch_A1:
        cpx.start_tone(notes_dict['A4'])
        fill_pixels(colors['cyan'])

    elif cpx.touch_A3:
        cpx.start_tone(notes_dict['B4'])
        fill_pixels(colors['purple'])

    elif cpx.touch_A4:
        cpx.start_tone(notes_dict['E5'])
        fill_pixels(colors['yellow'])

    elif cpx.touch_A6:
        cpx.start_tone(notes_dict['G5'])
        fill_pixels(colors['green'])

    else:
        cpx.stop_tone()
        fill_pixels(colors['black'])

    time.sleep(0.05)  # debounce delay

