from libqtile import bar
from .widgets import screens, widget_defaults

def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.92)
