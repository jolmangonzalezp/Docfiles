from libqtile import bar
from .widgets import screens, widget_defaults, color

def status_bar(widgets):
    return bar.Bar(widgets, 30, background = color[1]+"00")
