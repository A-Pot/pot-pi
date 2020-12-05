#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: A-Pot 
# https://github.com/A-Pot/pot-pi

# Description: This plays randomly shuffled music in a specificed directory.
# A pause and skip buttons are implemented assuming they are hooked up to
# GPIO pins 14 and 16, respectively.
# Date: December 6, 2020

# Imports
import RPi.GPIO as GPIO
from time import sleep
from numpy import random
from pygame import mixer
from pathlib import Path

# Specify directory containing the MP3s to play
MUSIC_DIR = '/home/pi/Music/'

# Gather mp3 files and randomly shuffle them
mp3_path = Path(MUSIC_DIR)
mp3s = list(mp3_path.glob('*.mp3'))
assert len(mp3s) > 0, 'There were no mp3 files found in {}'.format(MUSIC_DIR)
random.shuffle(mp3s)

# Initialize the buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Pause Button
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Skip Button
           
# Initialize the mixer
mixer.init()

# Play each song in the list while listening for button presses
for song in mp3s:
        
    # Load and start playing the song 
    mixer.music.load(str(song))
    mixer.music.play()
    
    # While the song is playing...
    is_paused = False
    print('Now playing {}'.format(song))
    while mixer.music.get_busy():
        pause_state = GPIO.input(14)
        skip_state = GPIO.input(16)
        
        # If the skip button is pressed...
        if not skip_state:
            print('Skipping to next song...')
            mixer.music.stop()
            sleep(1)
        
        # If the pause button is pressed...
        if not pause_state:
            
            # Pause/Unpause accordingly
            if is_paused:
                print('Unpausing...')
                mixer.music.unpause()
                is_paused = False
            else:
                print('Pausing...')
                mixer.music.pause()
                is_paused = True
            
            # Delay 1 second so button press is not repeated instantaneously
            sleep(1)
            
print('Bye! Thanks for listening!')
exit()
