## Imports
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os

## Colors
color = ["#00aaff", "#101010", "#ffffff"]

## Modifiers
mod = "mod4"
alt = "mod1"

## Keys

keys = [

    ## Key

    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 -q set Master 2dB+")), ## Subir volumen
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 -q set Master 2dB-")), ## Bajar volumen
    Key([], "XF86AudioMute", lazy.spawn("amixer -c 0 -q set Master toggle")), ## Silenciar
    Key([], "Print", lazy.spawn("flameshot full -p /home/jolman/screenshots")), ## Toma un screenshot

    ## Mod + key
    Key([mod], "Left", lazy.layout.left()), ## Focus en la ventana de la izq.
    Key([mod], "Right", lazy.layout.right()), ## Focus en la ventana de la der.
    Key([mod], "Down", lazy.layout.down()), ## Focus en la ventana de abajo
    Key([mod], "Up", lazy.layout.up()), ## Focus en la ventana de arriba
    Key([mod], "space", lazy.layout.next()), ## Focus en la siguiente ventana
    Key([mod], "Return", lazy.spawn("alacritty")), ## Lanza ALACRITTY
    Key([mod], "equal", lazy.spawn("amixer -c 0 -q set Master 2dB+")), ## Subir volumen
    Key([mod], "minus", lazy.spawn("amixer -c 0 -q set Master 2dB-")), ## Bajar volumen
    Key([mod], "e", lazy.spawn("pcmanfm")), ## Lanza Pcmanfm
    Key([mod], "f",lazy.window.toggle_floating()), ## Ventana en modo flotante
    Key([mod], "m",lazy.window.toggle_fullscreen()),  ## Ventana en modo pantalla completa
    Key([mod], "n", lazy.layout.normalize()), ## Resetea todos los tamaños de las ventanas
    Key([mod], "w", lazy.window.kill()), ## Cerrar ventanas
    Key([mod], "r", lazy.spawn("rofi -modi drun,run -show drun")), ## Lanza ROFI
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "v", lazy.spawn("code")), ## Lanza Visual Studio Code
    
    ## Mod + Shift + key
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    ## Mod + Alt + key
    Key([mod, alt],  "1", lazy.to_screen(0), lazy.group.toscreen(0)), ## Focus en el primer monitor
    Key([mod, alt],  "2", lazy.to_screen(1), lazy.group.toscreen(1)), ## Focus en el segundo monitor
    Key([mod, alt], "r", lazy.restart()), ## Reinicio de QTile
    Key([mod, alt], "q", lazy.shutdown()), ## Cerrar QTile

    ## Mod + Control + key
    Key([mod, "control"], "Left", lazy.layout.grow_left()),
    Key([mod, "control"], "Right", lazy.layout.grow_right()),
    Key([mod, "control"], "Down", lazy.layout.grow_down()),
    Key([mod, "control"], "Up", lazy.layout.grow_up()),
    

]

__groups = {
    1:Group("1", matches=[Match(wm_class=["code"])]),
    2:Group("2", matches=[Match(wm_class=["firefox"])]),
    3:Group("3", matches=[Match(wm_class=["alacritty"])]),
    4:Group("4", matches=[Match(wm_class=["pcmanfm"])]),
    5:Group("5"),
    6:Group("6", matches=[Match(wm_class=["vlc"])]),
    7:Group("7", matches=[Match(wm_class=["telegram-desktop"])]),
    8:Group("8", matches=[Match(wm_class=["libreoffice"])]),
    9:Group("9", matches=[Match(wm_class=["yt-dlg"])]),
    0:Group("10", matches=[Match(wm_class=["lxrandr"])])
}

groups = [__groups[i] for i in __groups]

def get_group_key (name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend([
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

# groups = [Group(i) for i in "1234567890"]

# for i in groups:
#     keys.extend([
#         # mod1 + letter of group = switch to group
#         Key([mod], i.name, lazy.group[i.name].toscreen(),
#             desc="Switch to group {}".format(i.name)),

#         # mod1 + shift + letter of group = switch to & move focused window to group
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(i.name)),
#         # Or, use below if you prefer not to switch to that group.
#         # # mod1 + shift + letter of group = move focused window to group
#         # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#         #     desc="move focused window to group {}".format(i.name)),
#     ])

layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    # layout.RatioTile(),
    layout.MonadTall(
        border_width=2,
        border_normal=color[1],
        border_focus=color[0],
        single_border_width=0,
        margin=5,
        single_margin=0
    ),
    layout.Max(),
    layout.Floating(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Hack',
    fontsize=20,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [

                widget.TextBox(
                    "", # "", 
                    background=color[1],
                    foreground=color[0],
                    center_aligned=True,
                    fontsize=30,
                    padding=5,
                ),

                widget.GroupBox(
                    active=color[2],
                    inactive=color[0],
                    foreground=color[0],
                    highlight_color=color[0],
                    highlight_text_color=color[1],
                    highlight_method="line",
                    block_highlight_text_color=color[1],
                    fontsize=25,
                    padding=5
                ),

                widget.Prompt(),

                widget.Spacer(),

                widget.Clock(
                    format='%H:%M %e %b %Y',
                    foreground=color[0],
                    fontsize=25
                ),
                # widget.Prompt(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ffffff", "#ff0000"),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.Spacer(),

                widget.Systray(),

                widget.Sep(),

                widget.CheckUpdates(
                    distro="Arch",
                    custom_command="checkupdates",
                    update_interval=1800,
                    display_format=" {updates} | ",
                    padding=10,
                    execute="alacritty -e sudo pacman -Syyu"
                ),

                widget.CheckUpdates(
                    custom_command="checkupdates",
                    background="#ff0000",
                    update_interval=1800,
                    colour_have_updates="#1793d1",
                    colour_no_updates="#ffffff",
                    display_format=' {updates}',
                    padding=10,
                    execute="alacritty -e sudo pacman -Syyu",
                    ),

                widget.CPU(
                    foreground=color[0],
                    format=' {freq_current}GHz'
                ),

                widget.Sep(),

                widget.Memory(
                    format=' {MemUsed:.0f}{mm}'
                ),

                widget.Sep(),
                
                widget.TextBox(
                    "ﯦ", 
                    foreground=color[0], 
                    center_aligned=True,
                    fontsize=35
                ),

                widget.Backlight(
                    foreground=color[0],  
                ),

                widget.Sep(),

                widget.TextBox(
                    "奔",
                    foreground=color[0], 
                    center_aligned=True,
                    fontsize=35
                ),

                widget.Volume(),

                widget.Sep(),

                widget.CurrentScreen(
                    active_text="",
                    active_color=color[0],
                    inactive_text="",
                    inactive_color=color[1],
                    fontsize=25
                ),
                
            ],
            size=34, 
            opacity=0.6,
        ),
    ),
    Screen(
        top=bar.Bar(
            [

                widget.TextBox(
                    "", 
                    foreground=color[0], 
                    center_aligned=True,
                    fontsize=40,
                ),

                widget.Sep(),

                widget.GroupBox(
                    active=color[1],
                    inactive=color[0],
                    foreground=color[0],
                    highlight_color=color[0],
                    highlight_text_color=color[1],
                    highlight_method="line",
                    block_highlight_text_color="ffffff",
                    fontsize=40
                ),

                widget.CheckUpdates(
                    custom_command="checkupdates",
                    update_interval=1800,
                    display_format="{updates}",
                    padding=10,
                    execute="alacritty -e sudo pacman -Syyu"
                ),
                widget.Spacer(),

                widget.Clock(
                    format='%H:%M %e %b %Y',
                    foreground=color[0]
                ),
                # widget.Prompt(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ffffff", "#ff0000"),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.Spacer(),

                widget.Systray(),
                #widget.Wlan(),

                widget.Sep(),

                widget.CPU(
                    foreground=color[0],
                    format=' {freq_current}GHz'
                ),

                widget.Sep(),

                widget.Memory(
                    format=' {MemUsed:.0f}{mm}'
                ),

                widget.Sep(),
                
                widget.TextBox(
                    "ﯦ", 
                    foreground=color[0], 
                    center_aligned=True,
                    fontsize=35
                ),

                widget.Backlight(
                    foreground=color[0],  
                ),

                widget.Sep(),

                widget.Volume(),

                widget.Sep(),

                widget.CurrentScreen(
                    active_text="",
                    active_color=color[0],
                    inactive_text="",
                    inactive_color=color[1],
                    fontsize=35
                ),
                
            ],
            size=35, 
            opacity=0.6,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

cmd=[
    "setxkbmap latam",
    "picom &",
    "nm-applet &",
    "numlockx on &",
    "/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & eval $(gnome-keyring-daemon -s --components=pkcs11,secrets,ssh,gpg)",
    "feh --bg-fill '/home/jolman/.wallpapers/wallpaper1.jpg'",
    #"sh /home/jolman/Projects/linux-config-master/i3/monitors.sh",
]

for x in cmd:
    os.system(x)
