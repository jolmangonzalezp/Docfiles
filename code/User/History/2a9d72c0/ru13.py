import os
import subprocess
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Match, Screen
from libqtile.lazy import lazy

from modules.keys import keys, mod
from modules.groups import groups
from modules.layouts import layouts

color = ["#1793d1","#333333","#0abdc6","#1c61c2","#123e7c"]


def sep(bg, fg):
    return widget.Sep(
        linewidth = 2,
        foreground = fg,
        background = bg,
        padding = 5
    )

def wicon(icon, bg, fg):
    return widget.TextBox(
        text = icon,
        background = bg,
        padding = 5,
        foreground = fg,
        fontsize = 20
    )

widget_defaults = dict(
    font="Monaspace Radon",
    fontsize=20,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.LaunchBar(),
                widget.GroupBox(
                    active = color[0],
                    foreground = 'ffffff',
                    inactive = "#ffffff",
                    highlight_method='line',
                    highlight_color = color[1],
                    
                ),
                widget.Net(
                    format = "󰖩 {up:6.2f}{up_suffix:<2}󰯎{down:6.2f}{down_suffix:<2}",
                    fontsize = 20,
                    padding = 5,
                    background = color[0],
                    foreground = color[1]
                ),
                widget.OpenWeather(
                    location = "Santa Marta",
                    format = " {main_temp} |  {humidity}",
                    padding = 5
                ),
                widget.Spacer(),
                widget.Clock(
                    format="%Y-%m-%d %H:%M",
                ),
                widget.Spacer(),

                widget.Systray(),
                
                widget.CheckUpdates(
                    distro = "Arch_yay",
                    colour_have_updates = "#ff0000",
                    display_format = " {updates}",
                    fontsize = 20,
                    padding = 5,
                    execute = "sudo pacman -Syyu",
                    initial_text = "",
                    no_update_string = "0"
                ),
                widget.HDD(
                    device = "nvme0n1",
                    fontsize = 20,
                    format = "󰋊 {HDDPercent}%",
                    padding = 5,
                    background = color[0],
                    foreground = color[1],
                ),
                sep(color[0], color[1]),
                widget.CPU(
                    format = " {freq_current}GHz",
                    fontsize = 20,
                    background = color[0],
                    foreground = color[1],
                ),
                widget.Memory(
                    padding = 5,
                    format = " {MemUsed: .0f}{mm}",
                    fontsize = 20,
                ),
                sep(None, "#ffffff"),
                widget.Memory(
                    padding = 5,
                    format = "󰯍 {SwapUsed: .0f}{ms}",
                    fontsize = 20,
                ),
                wicon("", color[0], color[1]),
                widget.Backlight(
                    backlight_name = "amdgpu_bl1",
                    background = color[0],
                    foreground = color[1],
                    padding = 5,
                    fontsize = 20,
                ),
                sep(color[0], color[1]),
                widget.Volume(
                    emoji = True,
                    volume_app = "pavucontrol",
                    fontsize = 20,
                    background = color[0],
                    foreground = color[1],
                ),
                widget.PulseVolume(
                    volume_app = "pavucontrol",
                    mute_format = "{volume}%",
                    mute_foreground = "ff0000",
                    fontsize = 20,
                    background = color[0],
                    foreground = color[1],
                ),
                widget.Battery(
                    format = "{char} {percent:2.0%}",
                    charge_char = "󰂄",
                    discharge_char = "󰁼",
                    empty_char = "󰂎",
                    unknown_char = "󰂑",
                    fontsize = 20,
                    full_char = "󰁹",
                    low_percentage = 0.2,
                    padding = 5,
                    update_interval = 30
                ),
                sep(None, "#ffffff"),
                widget.KeyboardLayout(
                    configured_keyboards = ["latam", "us"]
                ),
                # widget.QuickExit(),
            ],
            30,
            background = color[1]+"00",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 20

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([script])

