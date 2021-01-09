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
    
    ### QTILE COMMANDS ###
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    ### WINDOW CONTROLS ###
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "m", lazy.window.toggle_minimize()),
    Key([mod, "shift"], "x", lazy.window.toggle_maximize()),
    Key([mod], "Tab", lazy.group.next_window()),
    Key([mod], 'q', lazy.next_screen()),
    Key([mod], "space", lazy.next_layout()),
    Key([mod, "shift"], "a", lazy.layout.toggle_split()),
    Key([mod], "a", lazy.layout.up()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod], "w", lazy.window.kill()),

    ### APPLICATION BINDINGS ###
    Key([mod], "Return", lazy.spawn(myterm)),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "s", lazy.spawn("flameshot gui")),
    Key([mod], "m", lazy.spawn("umutmenu")),
    Key([mod], "e", lazy.spawn("pcmanfm")),
    Key([mod], "l", lazy.spawn("i3lock -c 000000 -e -f")),
]

group_names = [ ("1", {'layout': 'columns'}),
                ("2", {'layout': 'columns'}),
                ("3", {'layout': 'columns'}),
                ("4", {'layout': 'columns'}),
                ("5", {'layout': 'columns'}),
                ("6", {"layout": "columns"}),
                ("7", {'layout': 'columns'}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))


layouts = [
    layout.Columns(**layout_theme_1),
    layout.Max(**layout_theme_1),
    #layout.Floating(**layout_theme_2),
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
                filename = "~/.icons/cagan.jpg",
                mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('umutmenu')}
            ),
            widget.GroupBox(
                font = "Noto Sans",
                active = "000000",
                background = color4,
                highlight_method = "line",
                highlight_color = [color3],
                disable_drag = True,
                rounded = False,
                this_current_screen_border = color4,
                this_screen_border = color3,
                other_screen_border = color3,
            ),
            widget.TaskList(
                font = "Noto Sans",
                highlight_method = "block",
                foreground = "000000",
                padding_x = 2,
                max_title_width = 300,
                border = color3,
                rounded = False,
                icon_size = 0,
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
            widget.TextBox(
                foreground = color2,
                background = color4,
                text = "◀",
                fontsize = 37,
            ),
            widget.Spacer(length = 2, background = color2),
            widget.PulseVolume(background = color2, foreground = "000000"),
            widget.Spacer(length = 6, background = color2,),
            widget.CurrentLayoutIcon(scale=0.8, background = color2),
            widget.Spacer(length = 2, background = color2),
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
            ),
            widget.Spacer(length = 6, background = color3),

        ],
        20,
        background = color4,
        ),
    ),
    Screen(
        top=bar.Bar([
            widget.Image(
                filename = "~/.icons/cagan.jpg",
                mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('umutmenu')}
            ),
            widget.GroupBox(
                active = "000000",
                background = color4,
                highlight_method = "line",
                highlight_color = [color3],
                disable_drag = True,
                rounded = False,
                this_current_screen_border = color4,
                this_screen_border = color3,
                other_screen_border = color3,
            ),
            widget.TaskList(
                highlight_method = "block",
                foreground = "000000",
                padding_x = 2,
                max_title_width = 300,
                border = color3,
                rounded = False,
                icon_size = 0,
            ),
            widget.TextBox(
                foreground = color2,
                background = color4,
                text = "◀",
                fontsize = 37,
            ),
            widget.Spacer(length = 2, background = color2),
            widget.PulseVolume(background = color2, foreground = "000000"),
            widget.Spacer(length = 6, background = color2,),
            widget.CurrentLayoutIcon(scale=0.8, background = color2),
            widget.Spacer(length = 2, background = color2),
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
            ),
            widget.Spacer(length = 6, background = color3),
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
