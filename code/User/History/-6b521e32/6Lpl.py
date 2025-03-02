from libqtile import bar
from libqtile.config import Screen
from .widgets import one_screen, color
import subprocess

def bar(widgets):
    return bar.Bar(widgets, 30, background = color[1]+"00")

screens = [Screen(top=bar(one_screen))]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

