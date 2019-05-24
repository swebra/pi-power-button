# Pi Power Button
A simple combined shutdown / restart button with visual feedback for a Raspberry Pi.

A fork of [this script](https://github.com/scruss/shutdown_button) by @scruss, this simple python script allows for a single button to restart or shutdown a Pi depending on how long the button was held. This version adds LED sequences to distinguish between restarting and shutting down. The code structure has also been changed for personal preference, and the `systemd` service has been dropped for the same reason (although @scruss's service can still easily be used).

See [imswebra.com](https://www.imswebra.com/projects/pipowerbutton/) for more information on how I personally use this script.

## Defaults
- Holding the button for 2 to 5 seconds will restart your Pi. The LED will flash quickly to indicate a restart.
- Holding the button for more than 5 seconds will shutdown your Pi. The LED will slowly blink to indicate a shutdown.
- The button should be connected to [BCM pin 18](https://pinout.xyz/pinout/pin12_gpio18).
- The LED should be connected to [BCM pin 15](https://pinout.xyz/pinout/pin10_gpio15).

See the script's inline comments for more information on the user variables.

## Installation
Download or clone the script and add `python3 /path/to/pipowerbutton.py &` to your [`rc.local`](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md) file to have the script run on boot.

## License
This work is licensed under the [MIT](https://opensource.org/licenses/MIT) license.
