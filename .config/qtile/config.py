from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

### Variables ###
mod = "mod4"
alt = "mod1"
myterm = "alacritty"
color1 = "00897b" # My signature green
color2 = "b59ddd" # My signature purple-pink
color3 = "cc6666" # Pastel red
color4 = "282A2E" # Very dark gray

### Functions ###
var = "~/.icons/arch.png"
def m1(qtile):
    qtile.cmd_spawn('killall dunst'),

def m3(qtile):
    qtile.cmd_spawn('dunst &'),

### Themes ###

layout_theme_1 = {
    "border_focus": color3,
    "border_focus_stack": color3,
    "border_normal": color4,
    "border_normal_stack": color4,
    "margin": 1,
    "border_width": 2,
}
layout_theme_2 = {
    "border_focus": color3,
    "border_normal": color4,
    "border_width": 0,
    "margin": 0,
}
widget_theme_1 = {
    "foreground": color3,
    "background": color2,
    "text": "◀",
    "fontsize": "37",
}
widget_theme_2 = {
    "foreground": color2,
    "background": color3,
    "text": "◀",
    "fontsize": "37",
}

keys = [
    # I specifically gave all window control a binding with shift and control (if shift not possible),
    # and applications simple mod + "one key" bindings. Only bindings on window controls that are
    # using simple bindings are "q", "a" and "w": which are close to "Tab" on both physically and
    # functionally. This creates more easy learning curve and makes binding more easier to code.

    ### QTILE AND SYSTEM COMMANDS ###
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 2")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 2")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t")),


    ### WINDOW CONTROLS ###
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "o", lazy.layout.shrink_main()),
    Key([mod, "control"], "p", lazy.layout.grow_main()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "m", lazy.window.toggle_minimize()),
    Key([mod, "shift"], "x", lazy.window.toggle_fullscreen()),
    Key([mod], "Tab", lazy.group.next_window()),
    Key([mod], 'q', lazy.next_screen()),
    Key([mod], "space", lazy.next_layout()),
    Key([mod, "shift"], "a", lazy.layout.toggle_split()),
    Key([mod], "a", lazy.layout.up()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod], "w", lazy.window.kill()),

    ### APPLICATION BINDINGS ###
    Key([mod], "Return", lazy.spawn(myterm)),
    Key([mod], "r", lazy.spawn("rofi -show run")),
    Key(["control"], "space", lazy.spawn("rofi -show run")),
    Key([alt], "Tab", lazy.spawn("rofi -show window")),
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([mod], "m", lazy.spawn("umutmenu")),
    Key([mod], "e", lazy.spawn("pcmanfm")),
    Key([mod, "control", alt], "l", lazy.spawn("i3lock -c 000000 -e -f")),
    Key([mod], "l", lazy.spawn("i3lock -k -c 00000099 --insidevercolor=282a2e --insidewrongcolor=282a2e --insidecolor=282a2e --ringvercolor=cc6666 --ringcolor=cc6666 --line-uses-inside --timecolor=ffffff --datecolor=ffffff --separatorcolor=cc6666"))

]

### GROUPS ###

groups_info = [
	("1", ""),
	("2", ""),
	("3", ""),
	("4", ""),
	("5", ""),
	("6", ""),
	("7", ""),
]

groups = []
for key, icon in groups_info:
	groups.append(Group(icon))
	keys.append(Key([mod], key, lazy.group[icon].toscreen()))
	keys.append(Key([mod, "shift"], key, lazy.window.togroup(icon)))

layouts = [
    layout.MonadTall(**layout_theme_1),
    layout.Max(**layout_theme_1),
    layout.Columns(**layout_theme_1),
#    layout.Floating(**layout_theme_2),
]

widget_defaults = dict(
    font='JetBrains Mono',
    fontsize=12,
    padding=0,
    borderwidth = 2,
    border_width = 2,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar([
            widget.Image(
                margin = 2,
                filename = "~/.icons/arch.png",
                mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('umutmenu')}
            ),
            widget.GroupBox(
                font = "FontAwesome",
                fontsize = 15,
                active = color3,
                background = color4,
                block_highlight_text_color = color2,
                highlight_method = "line",
                highlight_color = [color4],
                disable_drag = True,
                rounded = False,
                this_current_screen_border = color1,
                this_screen_border = color3,
                other_screen_border = color4,
            ),
            widget.TaskList(
                font = "Noto Sans",
                highlight_method = "block",
                foreground = "000000",
                padding_y = 2,
                padding_x = 5,
                margin = 0,
                max_title_width = 200,
                spacing = 2,
                border = color2,
                unfocused_border = color3,
                rounded = True,
                icon_size = 13,
                txt_floating = " ",
                txt_minimized = " ",
                txt_maximized = " ",
            ),
            widget.TextBox(
                foreground = color2,
                background = color4,
                text = "◀",
                fontsize = 37,
            ),
            widget.Spacer(
                length = 6,
                background = color2,
            ),
            widget.Battery(
                background = color2,
                foreground = "000000",
                format = "{char} {percent:2.0%} {watt:.2f} W",
                discharge_char = "▽",
                charge_char = "△",
                full_char = "□",
            ),
            widget.Spacer(length=6, background = color2),
            widget.TextBox(**widget_theme_1),
            widget.Spacer(length=6, background = color3),
            widget.Net(
                format = "↓{down}",
                foreground = "000000",
                background = color3,
            ),
            widget.Spacer(length=6, background = color3),
            widget.TextBox(**widget_theme_2),
            widget.Spacer(length=6, background = color2),
            widget.Net(
                format = "↑{up}",
                background = color2,
                foreground = "000000",
            ),
            widget.Spacer(length=6, background = color2),
            widget.TextBox(**widget_theme_1),
            widget.Memory(
                format = "{MemUsed}M",
                foreground = "000000",
                background = color3,
            ),
            widget.Spacer(length=6, background = color3),
            widget.TextBox(**widget_theme_2),
            widget.Spacer(length=6, background = color2),
            widget.CPU(
                format = "{load_percent}%",
                foreground = "000000",
                background = color2,
            ),
            widget.Spacer(length=6, background = color2),
            widget.TextBox(
                foreground = color4,
                background = color2,
                text = "◀",
                fontsize = 37,
            ),
            widget.Systray(
                background = color4,
                padding = 3,
                icon_size = 18,
            ),
            widget.Spacer(length = 6),
            widget.PulseVolume(),
            widget.Spacer(length = 6),
            widget.TextBox(
                foreground = color3,
                background = color4,
                text = "◀",
                fontsize = 37,
            ),
            widget.Spacer(length = 6, background = color3),
            widget.Clock(
                background = color3,
                foreground = "000000",
                format = "%H:%M:%S",
                mouse_callbacks = {'Button1': m1, 'Button3': m3,},
            ),
            widget.Spacer(length = 4, background = color3),
            widget.CurrentLayoutIcon(scale=0.8, background = color3),
            widget.Spacer(length = 4, background = color3),
        ],
        20,
        background = color4,
        ),
    ),
    Screen(
        top=bar.Bar([
            widget.Image(
                margin = 2,
                filename = "~/.icons/arch.png",
                mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('umutmenu')}
            ),
            widget.GroupBox(
                font = "FontAwesome",
                fontsize = 15,
                active = color3,
                background = color4,
                block_highlight_text_color = color2,
                highlight_method = "line",
                highlight_color = [color4],
                disable_drag = True,
                rounded = False,
                this_current_screen_border = color1,
                this_screen_border = color3,
                other_screen_border = color4,
            ),
                widget.TaskList(
                font = "Noto Sans",
                highlight_method = "block",
                foreground = "000000",
                padding_y = 2,
                padding_x = 5,
                margin = 0,
                max_title_width = 200,
                spacing = 2,
                border = color2,
                unfocused_border = color3,
                rounded = True,
                icon_size = 13,
                txt_floating = " ",
                txt_minimized = " ",
                txt_maximized = " ",
            ),
            widget.TextBox(
                foreground = color2,
                background = color4,
                text = "◀",
                fontsize = 37,
            ),
            widget.Spacer(
                length = 6,
                background = color2,
            ),
            widget.Battery(
                background = color2,
                foreground = "000000",
                format = "{char} {percent:2.0%} {watt:.2f} W",
                discharge_char = "▽",
                charge_char = "△",
                full_char = "□",
            ),
            widget.Spacer(length=6, background = color2),
            widget.TextBox(**widget_theme_1),
            widget.Spacer(length=6, background = color3),
            widget.Net(
                format = "↓{down}",
                foreground = "000000",
                background = color3,
            ),
            widget.Spacer(length=6, background = color3),
            widget.TextBox(**widget_theme_2),
            widget.Spacer(length=6, background = color2),
            widget.Net(
                format = "↑{up}",
                background = color2,
                foreground = "000000",
            ),
            widget.Spacer(length=6, background = color2),
            widget.TextBox(**widget_theme_1),
            widget.Memory(
                format = "{MemUsed}M",
                foreground = "000000",
                background = color3,
            ),
            widget.Spacer(length=6, background = color3),
            widget.TextBox(**widget_theme_2),
            widget.Spacer(length=6, background = color2),
            widget.CPU(
                format = "{load_percent}%",
                foreground = "000000",
                background = color2,
            ),
            widget.Spacer(length=6, background = color2),
            widget.TextBox(
                foreground = color3,
                background = color2,
                text = "◀",
                fontsize = 37,
            ),
            widget.Spacer(length = 6, background = color3),
            widget.Clock(
                background = color3,
                foreground = "000000",
                format = "%H:%M:%S",
                mouse_callbacks = {'Button1': m1, 'Button3': m3,},
            ),
            widget.Spacer(length = 4, background = color3),
            widget.CurrentLayoutIcon(scale=0.8, background = color3),
            widget.Spacer(length = 4, background = color3),
        ],
        20,
        background = color4,
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
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'zoom'},
    {"wname": "Confirm File Replacing"},
])
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "qtile"
