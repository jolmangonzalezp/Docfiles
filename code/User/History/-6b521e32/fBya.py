from libqtile import bar
from .widgets import screens, widget_defaults, color

def bar(widgets):
    return bar.Bar(widgets, 30, background = color[1]+"00")

screens = [Screen(top=bar(primary_widgets))]