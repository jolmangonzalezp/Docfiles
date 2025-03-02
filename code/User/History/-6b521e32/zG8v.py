from libqtile import widget, bar, 
from libqtile.config import Screen

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