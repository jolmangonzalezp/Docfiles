from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
alt = "mod1"
shft = "shift"
ctrl = "control"


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
    Key([mod], "Space",  lazy.spawn("rofi -icon-theme arc-icon-theme -show drun -show-icons"), desc="Mostrar el menu"),
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

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
]