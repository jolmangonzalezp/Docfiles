import os
import subprocess
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
alt = "mod1"
shft = "shift"
ctrl = "control"
terminal = guess_terminal()
color = ["#1793d1","#333333","#0abdc6","#1c61c2","#123e7c"]

keys = [
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -3%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +3%")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")), 
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
    Key([], "Print", lazy.spawn("scrot")),
    ## mod + key
    Key([mod], "Down",   lazy.layout.down(), desc="Mueve el focus a abajo"),
    Key([mod], "Left",   lazy.layout.left(), desc="Mueve el focus a la izquierda"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Lanza la terminal"),
    Key([mod], "Right",  lazy.layout.right(), desc="Mueve el focus a la derecha"),
    Key([mod], "Up",     lazy.layout.up(), desc="Mueve el focus a arriba"),
    Key([mod], "Space",  lazy.spawn("rofi -icon-theme ePapirus-icon-theme -show drun -show-icons"), desc="Mostrar el menu"),
    Key([mod], "Tab",    lazy.next_layout(), desc="Alternar entre layouts"),
    Key([mod], "b",      lazy.spawn("firefox"), desc="Lanza Firefox"),
    Key([mod], "e",      lazy.spawn("pcmanfm"), desc="Lanza PcManFM"),
    Key([mod], "f",      lazy.window.toggle_fullscreen(), desc="Alternar ventana a pantalla completo"),
    Key([mod], "l",   lazy.spawn("setxkbmap latam"), desc=""),
    Key([mod], "n",      lazy.layout.normalize(), desc="Restablece todos los tamaños de ventana"),
    Key([mod], "q",      lazy.window.kill(), desc="Cerrar ventana"),
    Key([mod], "r",      lazy.spawn("sh /home/jolman/.config/rofi/rofi-wifi-menu/rofi-wifi-menu.sh"), desc="Wifi Menu"),
    Key([mod], "t",      lazy.window.toggle_floating(), desc="Alternar ventana flotante"),
    Key([mod], "u",   lazy.spawn("setxkbmap us"), desc=""),
    Key([mod], "v",      lazy.spawn("code"), desc="Lanza VSCode"),
    ## mod + alt + key
    Key([mod, alt], "c", lazy.reload_config(), desc="Recargar la config"),
    Key([mod, alt], "q", lazy.shutdown(), desc="Log out"),
    # Key([mod, alt], "r", lazy.spawn("reboot"), desc="reboot"),
    Key([mod, alt], "p", lazy.spawn("sh /home/jolman/.config/rofi/powermenu"), desc="power menu"),
    ## mod + control + key
    Key([mod, ctrl], "Down", lazy.layout.grow_down(), desc="Cambia el tamaño de la pantalla hacia abajo"),
    Key([mod, ctrl], "Left", lazy.layout.grow_left(), desc="Cambia el tamaño de la pantalla hacia la izquierda"),
    Key([mod, ctrl], "Right", lazy.layout.grow_right(), desc="Cambia el tamaño de la pantalla hacia la derecha"),
    Key([mod, ctrl], "Up", lazy.layout.grow_up(), desc="Cambia el tamaño de la pantalla hacia arriba"),
    ## mod + shift + key
    Key([mod, shft], "Down", lazy.layout.shuffle_down(), desc="Mueve la ventana hacia abajo"),
    Key([mod, shft], "Left", lazy.layout.shuffle_left(), desc="Mueve la ventana hacia la izquierda"),
    Key([mod, shft], "Right", lazy.layout.shuffle_right(), desc="Mueve la ventana hacia la derecha"),
    Key([mod, shft], "Up", lazy.layout.shuffle_up(), desc="Mueve la ventana hacia arriba"),

    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
]

for vt in range(1, 9):
    keys.append(
        Key(
            [ctrl, alt],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.RatioTile(),
    layout.Max(),
    layout.Matrix(),
]

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


class ToggleClock(widget.Clock):
    def __init__(self, **config):
        widget.Clock.__init__(self, **config)
        self.add_defaults({
            'format': '%H:%M %Y-%m-%d',
        })
        self.show_clock = True  # Add this line to define the attribute
        self.update_fmt()

    def update_fmt(self):
        if self.show_clock:
            self.format = self.fmt
        else:
            self.format = ""

    def cmd_toggle(self):
        self.show_clock = not self.show_clock
        self.update_fmt()

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

