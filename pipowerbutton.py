#!/usr/bin/env python3

# Author: imswebra
# 06-2018
# http://www.imswebra.com/
#
# Based of script by Stewart C. Russell (scruss)
# https://github.com/scruss/shutdown_button/blob/master/shutdown_button.py
# https://web.archive.org/web/20180610034643/https://github.com/scruss/shutdown_button/blob/master/shutdown_button.py

# IMPORTS #
from gpiozero import Button, LED
from subprocess import check_call
from time import sleep
from signal import pause


# USER VARIABLES #

# The GPIO pin ID connected to the button. (BCM #)
buttonPin = 18
# The GPIO pin ID connected to the LED. (BCM #)
ledPin = 15

# The minimum length of time (in seconds) the button must be held to activate
# the shutdown script.
shutdownTime = 5
# The minimum length of time (in seconds) the button must be held to activate
# the restart script. Must be shorter than 'shutdownTime'.
restartTime = 2


# FUNCTIONS #

# Button held function
# This function runs every button.hold_time (set at 0.5 seconds at default in
# MAIN SCRIPT) while the button is being held, updating 'userHeldTime'
# accordingly.
def held():
    global userHeldTime
    # Need to use max() as held_time resets to zero on last callback
    userHeldTime = max(userHeldTime, button.held_time + button.hold_time)


# Button release function
# This function runs on the release of the button and contains the logic to
# determine whether to shutdown, restart, or do nothing.
def release():
    global userHeldTime
    if userHeldTime > shutdownTime:
        shutdown()
    elif userHeldTime > restartTime:
        restart()
    else:
        userHeldTime = 0


# Shutdown sequence function
def shutdown():
    LED.blink(0.7, 0.7, 2, False)
    check_call(["sudo", "shutdown", "now"])


# Restart sequence function
def restart():
    LED.blink(0.1, 0.1, 2, False)
    sleep(0.4)
    LED.blink(0.1, 0.1, 2, False)
    sleep(0.4)
    check_call(["sudo", "reboot"])


# MAIN SCRIPT #
button = Button(buttonPin, hold_time=0.5, hold_repeat=True,)
LED = LED(ledPin)
LED.on()

userHeldTime = 0
button.when_held = held
button.when_released = release

pause()
