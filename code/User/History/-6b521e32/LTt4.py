from libqtile import bar
from libqtile.config import Screen
from libqtile.log_utils import logger
from .widgets import one_screen, color, many_screens, widget_defaultsbv
import subprocess

def bar(widgets):
    return bar.Bar(widgets, 30, background = color[1]+"00")

screens = [Screen(top=bar(one_screen))]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=bar(many_screens)))
