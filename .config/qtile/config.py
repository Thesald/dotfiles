import os
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy

mod = "mod4"
alt = "mod1"
control = "control"
shift = "shift"
myterm = "alacritty"
grey1 = "282a2e"
grey2 = "2a313e"
grey3 = "4c566a"
grey4 = "242831"
grey5 = "3b4252"
grey6 = "2e3440"
grey7 = "4e4e4e"
grey8 = "1f1f1f"
grey9 = "2d2d2d"
white = "ffffff"
white1 = "e5e9f0"
white2 = "d8dee9"
white3 = "a0a0a0"
white4 = "eeffff"
red1 = "cc6666"
red2 = "bf616a"
red3 = "e53935"
green1 = "00897b"
green2 = "a3be8c"
green3 = "c3e88d"
green4 = "91b859"
blue1 = "1f232d"
blue2 = "81a1c1"
blue3 = "82aaff"
blue4 = "6182b8"
blue5 = "0e2e6f"
cyan1 = "8fbcbb"
cyan2 = "88c0d0"
cyan3 = "89ddff"
cyan4 = "39adb5"
magenta1 = "b59ddd"
magenta2 = "b48ead"
magenta3 = "f07178"
magenta4 = "ff5370"
yellow1 = "ebcb8b"
yellow2 = "ffcb6b"
yellow3 = "ffb62c"
orange1 = "d08770"

keys = [
    ### QTILE AND SYSTEM COMMANDS ###
    Key([mod, control], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, control], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("./.config/qtile/scripts/volume_down")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("./.config/qtile/scripts/volume_up")),
    Key([], "XF86AudioMute", lazy.spawn("./.config/qtile/scripts/volume_mute")),
    ### WINDOW CONTROLS ###
    Key([mod, shift], "h", lazy.layout.shuffle_left()),
    Key([mod, shift], "j", lazy.layout.shuffle_down()),
    Key([mod, shift], "k", lazy.layout.shuffle_up()),
    Key([mod, shift], "l", lazy.layout.shuffle_right()),
    Key([mod, control], "h", lazy.layout.grow_left()),
    Key([mod, control], "j", lazy.layout.grow_down()),
    Key([mod, control], "k", lazy.layout.grow_up()),
    Key([mod, control], "l", lazy.layout.grow_right()),
    Key([mod, shift], "o", lazy.layout.shrink_main()),
    Key([mod, shift], "p", lazy.layout.grow_main()),
    Key([mod, shift], "n", lazy.layout.normalize()),
    Key([mod, shift], "m", lazy.window.toggle_minimize()),
    Key([mod, shift], "x", lazy.window.toggle_fullscreen()),
    Key([mod], "Tab", lazy.group.next_window()),
    Key([mod], "q", lazy.next_screen()),
    Key([mod], "space", lazy.next_layout()),
    Key([mod, shift], "a", lazy.layout.toggle_split()),
    Key([mod, shift], "f", lazy.window.toggle_floating()),
    Key([mod], "w", lazy.window.kill()),
    Key([alt], "Tab", lazy.screen.next_group()),
    Key([alt, shift], "Tab", lazy.screen.prev_group()),
    ### APPLICATION BINDINGS ###
    Key([mod], "Return", lazy.spawn(myterm)),
    Key([control, alt], "t", lazy.spawn(myterm)),
    Key([mod], "r", lazy.spawn("rofi -show combi -combi-modi 'run,drun' -modi combi")),
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([mod], "m", lazy.spawn("./.config/qtile/scripts/xmenu")),
    Key([mod], "e", lazy.spawn("pcmanfm")),
    Key([mod, control, alt], "l", lazy.spawn("./.config/qtile/scripts/i3lock_black")),
    Key([mod], "l", lazy.spawn("./.config/qtile/scripts/i3lock")),
    Key([], "Scroll_Lock", lazy.spawn("notify-send 'DUNST_COMMAND_TOGGLE'")),
    Key([control, alt, shift], "F11", lazy.spawn("./.config/qtile/scripts/huion1")),
    Key([control, alt, shift], "F12", lazy.spawn("./.config/qtile/scripts/huion2")),
    Key([control, alt, shift], "F10", lazy.spawn("./.config/qtile/scripts/huion")),
]

### GROUPS ###
groups_info = [
	("F1", ""),
	("F2", ""),
	("1", ""),
	("2", ""),
	("3", ""),
	("4", ""),
    ("5", ""),
    ("6", ""),
    ("7", ""),
    ("8", ""),
    ("9", ""),
    ("0", ""),
]
groups = []
for key, icon in groups_info:
	groups.append(Group(icon))
	keys.append(Key([mod], key, lazy.group[icon].toscreen()))
	keys.append(Key([mod, shift], key, lazy.window.togroup(icon)))

layout_theme_1 = {
    "border_focus": cyan2,
    "border_focus_stack": cyan2,
    "border_normal": blue1,
    "border_normal_stack": blue1,
    "margin": 5,
    "border_width": 1,
}
layout_theme_2 = {
    "border_focus": magenta2,
    "border_focus_stack": magenta2,
    "border_normal": blue1,
    "border_normal_stack": blue1,
    "margin": 0,
    "border_width": 1,
}

layouts = [
    layout.MonadTall(**layout_theme_1),
    layout.Max(**layout_theme_1),
    layout.Columns(**layout_theme_1),
]

### WIDGETS ###
widget_textbox_1 = {
    "text": "",
    "font": "Iosevka",
    "fontsize": 21,
    "background": grey2,
    "foreground": blue1,
}
widget_textbox_2 = {
    "text": "",
    "font": "Iosevka",
    "fontsize": 21,
    "background": grey2,
    "foreground": blue1,
}
widget_groupbox_1 = {
    "font": "Iosevka",
    "fontsize": 15,
    "padding": 3,
    "borderwidth": 2,
    "active": cyan2,
    "inactive": grey6,
    "disable_drag": True,
    "rounded": False,
    "highlight_color": blue1,
    "block_highlight_text_color": cyan2,
    "highlight_method": "line",
    "this_current_screen_border": cyan2,
    "this_screen_border": cyan2,
    "other_screen_border": grey3,
    "other_current_screen_border": grey3,
    "background": blue1,
    "urgent_border": red2,
    "hide_unused": False,
}
widget_tasklist_1 = {
    "font": "Noto Sans Display Medium",
    "highlight_method": "block",
    "padding": 5,
    "spacing": 2,
    "margin_y": 0,
    "max_title_width": 200,
    "icon_size": 10,
    "foreground": yellow1,
    "background": grey2,
    "border": blue1,
    "unfocused_border": grey2,
    "rounded": True,
    "txt_floating": "",
    "txt_minimized": "",
    "txt_maximized": "",
}
widget_currentlayouticon_1 = {
    "custom_icon_paths": [os.path.expanduser("~/.config/qtile/icons")],
    "background": blue1,
    "scale": 0.6,
}
widget_spacer_1 = {
    "background": grey2,
    "width": 6,
}
widget_spacer_2 = {
    "background": blue1,
    "width": 6,
}
widget_memory_1 = {
    "format": "{MemUsed}M ",
    "background": blue1,
    "foreground": orange1,
    "mouse_callbacks": {'Button1': lambda qtile: qtile.cmd_spawn(myterm + " -e bpytop")},
}
widget_cpu_1 = {
    "format": "{freq_current}GHz {load_percent}%  ",
    "background": blue1,
    "foreground": orange1,
    "mouse_callbacks": {'Button1': lambda qtile: qtile.cmd_spawn(myterm + " -e bpytop")},
}
widget_net_1 = {
    "format": "↓{down} ↑{up}  ",
    "foreground": magenta2,
    "background": blue1,
    "mouse_callbacks": {'Button1': lambda qtile: qtile.cmd_spawn("nm-connection-editor")},
}
widget_clock_1 = {
    "format": "%a, %b %d ",
    "background": blue1,
    "foreground": green2,
}
widget_clock_2 = {
    "format": "%H:%M:%S ",
    "mouse_callbacks": {'Button1': lambda qtile: qtile.cmd_spawn(myterm + " -e tty-clock -scb")},
    "background": blue1,
    "foreground": cyan2,
}
widget_defaults = dict(
    font = 'JetBrains Mono',
    fontsize = 12,
    padding = 0,
)

def main_screen_widgets():
    main_widgets_list = [
        widget.Spacer(**widget_spacer_2),
        widget.GroupBox(**widget_groupbox_1, visible_groups = ("", "")),
        widget.TextBox(**widget_textbox_2),
        widget.Spacer(**widget_spacer_1),
        widget.TextBox(**widget_textbox_1),
        widget.GroupBox(**widget_groupbox_1, visible_groups = ("", "", "", "", "", "", "", "", "", "")),
        widget.TextBox(**widget_textbox_2),
        widget.Spacer(**widget_spacer_1),
        widget.TaskList(**widget_tasklist_1),
        widget.Spacer(**widget_spacer_1),
        widget.TextBox(**widget_textbox_1),
        widget.Systray(padding = 5, background = blue1),
        widget.TextBox(**widget_textbox_2),
        widget.Spacer(**widget_spacer_1),
        widget.TextBox(**widget_textbox_1),
        widget.Memory(**widget_memory_1),
        widget.CPU(**widget_cpu_1),
        widget.TextBox(**widget_textbox_2),
        widget.Spacer(**widget_spacer_1),
        widget.TextBox(**widget_textbox_1),
        widget.Net(**widget_net_1),
        widget.TextBox(**widget_textbox_2),
        widget.Spacer(**widget_spacer_1),
        widget.TextBox(**widget_textbox_1),
        widget.Clock(**widget_clock_1),
        widget.TextBox(**widget_textbox_2),
        widget.Spacer(**widget_spacer_1),
        widget.TextBox(**widget_textbox_1),
        widget.Clock(**widget_clock_2),
        widget.CurrentLayoutIcon(**widget_currentlayouticon_1),
        widget.Spacer(**widget_spacer_2),
    ]
    return main_widgets_list

def other_screen_widgets():
    other_widgets_list = [
        widget.Spacer(**widget_spacer_2),
        widget.GroupBox(**widget_groupbox_1, visible_groups = ("", "")),
        widget.TextBox(**widget_textbox_2),
        widget.Spacer(**widget_spacer_1),
        widget.TextBox(**widget_textbox_1),
        widget.GroupBox(**widget_groupbox_1, visible_groups = ("", "", "", "", "", "", "", "", "", "")),
        widget.TextBox(**widget_textbox_2),
        widget.Spacer(**widget_spacer_1),
        widget.TaskList(**widget_tasklist_1),
        widget.Spacer(**widget_spacer_1),
        widget.TextBox(**widget_textbox_1),
        widget.Clock(**widget_clock_2),
        widget.CurrentLayoutIcon(**widget_currentlayouticon_1),
        widget.Spacer(**widget_spacer_2),
    ]
    return other_widgets_list

screens = [
    Screen(top=bar.Bar(widgets=main_screen_widgets(), size=25, margin=[5,0,0,0], background=grey2)),
    Screen(top=bar.Bar(widgets=other_screen_widgets(), size=25, margin=[5,0,0,0], background=grey2))
    ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = "floating_only"
cursor_warp = False
floating_layout = layout.Floating(
    **layout_theme_2,
    float_rules=[
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'confirmreset'},
        {'wmclass': 'makebranch'},
        {'wmclass': 'maketag'},
        {'wname': 'branchdialog'},
        {'wname': 'pinentry'},
        {'wmclass': 'ssh-askpass'},
        {'wmclass': 'zoom'},
        {"wname": "Confirm File Replacing"},
        {"wmclass": "nm-connection-editor"},
        {"wmclass": "osu!.exe"},
        {"wmclass": "Wine"},
    ]
)
auto_fullscreen = True
focus_on_window_activation = "focus"
wmname = "qtile"