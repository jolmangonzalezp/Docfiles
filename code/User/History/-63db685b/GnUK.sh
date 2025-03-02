#!/bin/sh
## Keyboard distribution
setxkbmap latam &

## Systray Icons
udiskie -t &
nm-applet &
volumeicon &
cbatticon -u 5 &
nitrogen --restore &