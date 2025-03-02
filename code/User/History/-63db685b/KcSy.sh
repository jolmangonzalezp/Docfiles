#!/bin/sh
## Keyboard distribution
setxkbmap latam &

## Systray Icons
udiskie -t &
nm-applet &
volumeicon &