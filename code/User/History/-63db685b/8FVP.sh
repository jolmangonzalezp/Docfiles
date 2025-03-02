#!/bin/sh
## Keyboard distribution
setxkbmap latam &

## Systray Icons
nitrogen --restore &
picom &
nm-applet &