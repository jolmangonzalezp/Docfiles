#!/bin/sh
## Keyboard distribution
setxkbmap latam &

## Systray Icons
picom &
# udiskie -t &
nm-applet &
# volumeicon &
nitrogen --restore &