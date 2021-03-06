from typing import List  # noqa: F401
import getpass
import socket
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import random

colors = []
path = '/home/andrija/.config/qtile/wallpapers'
cache='/home/andrija/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)
alt='mod1'
mod = "mod4"
terminal = 'kitty'
username=getpass.getuser()
hostname=socket.gethostname()
browser='google-chrome-stable'
wallplight='bash /home/andrija/.config/qtile/colors -l'
wallpdark='bash /home/andrija/.config/qtile/colors -d'
rofi=f'rofi -show run -lines 5 -eh 2 -width 50 -padding 800 -opacity "85" -bw 0 -bc "{colors[0]}" -bg "$bg-color" -fg "$text-color" -hlbg "$bg-color" -hlfg "#9575cd"'
keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

	Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 5%+ unmute")),
	Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%- unmute")),
	Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),

	# Brightness
	Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
	Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),
    Key([mod], "q", lazy.window.toggle_floating(),
        desc="toggle floating layout"),
#os.system('bash /home/andrija/.config/qtile/colors')
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([alt], "l", lazy.spawn(browser), desc="Launch firefox"),
    Key([mod], "r", lazy.spawn(rofi), desc="Launch rofi"),
    Key([mod], "p", lazy.spawn(wallpdark), desc="Launch wallpaper changer"),
    Key([mod, "control"], "p", lazy.spawn(wallplight), desc="Launch wallpaper changer"),


    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([alt], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]
groups = [
        Group('1',label='\uf269'),
        Group('2',label='\uf121'),
        Group('3',label='\uf1c9'),
        Group('4',label='\uf09b'),
        Group('5',label='\uf87c'),
        Group('6',label='\uf085'),
        Group('7',label='\uf1ea'),
        Group('8',label='\uf133'),
        Group('9',label='\uf392')]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2),
      layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(border_focus='#fafafa',align='right',ratio=0.55),
    # layout.MonadWide(border_focus='#fafafa'),
      layout.RatioTile(margin=3),
      layout.Tile(margin=5,border_focus='#db105e'),
      layout.TreeTab(),
    # layout.VerticalTile(),
      layout.Zoomy(),
]

widget_defaults = dict(
    font='hack',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
screens = [
    Screen()
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
main = None  # WARNING: this is deprecated and will be removed soon
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
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
