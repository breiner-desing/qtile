from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import PowerLineDecoration
from .themes import Dracula
import subprocess
from libqtile import qtile

colors = Dracula
myTerm = "alacritty"  

widget_defaults = dict(font="Ubuntu Bold", fontsize=12, padding=0, background=colors[0])

def init_widgets_list2():
    widgets_list = [
        widget.Image(
                 filename = "~/.config/qtile/icons/logo.png",
                 scale = "False",
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
                 ),
        widget.Prompt(
                 font = "Ubuntu Mono",
                 fontsize=14,
                 foreground = colors[1]
        ),
        widget.GroupBox(
                 fontsize = 11,
                 margin_y = 5,
                 margin_x = 5,
                 padding_y = 0,
                 padding_x = 1,
                 borderwidth = 3,
                 active = colors[8],
                 inactive = colors[1],
                 rounded = False,
                 highlight_color = colors[2],
                 highlight_method = "line",
                 this_current_screen_border = colors[7],
                 this_screen_border = colors [4],
                 other_current_screen_border = colors[7],
                 other_screen_border = colors[4],
                 ),
        widget.TextBox(
                 text = '|',
                 font = "Ubuntu Mono",
                 foreground = colors[1],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.CurrentLayoutIcon(
                 # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                 foreground = colors[1],
                 padding = 4,
                 scale = 0.6
                 ),
        widget.CurrentLayout(
                 foreground = colors[1],
                 padding = 5
                 ),
        widget.TextBox(
                 text = '|',
                 font = "Ubuntu Mono",
                 foreground = colors[1],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.WindowName(
                 foreground = colors[6],
                 max_chars = 40
                 ),
        widget.GenPollText(
                 update_interval = 300,
                 func = lambda: subprocess.check_output("printf $(uname -r)", shell=True, text=True),
                 foreground = colors[3],
                 fmt = '❤  {}',
                 decorations=[
                     BorderDecoration(
                         colour = colors[3],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.CPU(
                 format = '▓  Cpu: {load_percent}%',
                 foreground = colors[4],
                 decorations=[
                     BorderDecoration(
                         colour = colors[4],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.Memory(
                 foreground = colors[8],
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                 format = '{MemUsed: .0f}{mm}',
                 fmt = '🖥  Mem: {} used',
                 decorations=[
                     BorderDecoration(
                         colour = colors[8],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.DF(
                 update_interval = 60,
                 foreground = colors[5],
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e df')},
                 partition = '/',
                 #format = '[{p}] {uf}{m} ({r:.0f}%)',
                 format = '{uf}{m} free',
                 fmt = '🖴  Disk: {}',
                 visible_on_warn = False,
                 decorations=[
                     BorderDecoration(
                         colour = colors[5],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.Volume(
                 foreground = colors[7],
                 fmt = '🕫  Vol: {}',
                 decorations=[
                     BorderDecoration(
                         colour = colors[7],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.KeyboardLayout(
                 foreground = colors[4],
                 fmt = '⌨  Kbd: {}',
                 decorations=[
                     BorderDecoration(
                         colour = colors[4],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.Clock(
                 foreground = colors[8],
                 format = "⏱  %a, %b %d - %H:%M",
                 decorations=[
                     BorderDecoration(
                         colour = colors[8],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.Systray(padding = 3),
        widget.Spacer(length = 8),

        ]
    return widgets_list

def init_widgets_list():
    widgets_list = [
        widget.Image(
                 filename="~/.config/qtile/icons/logo.png",
                 scale="False",
                 mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm)},
                 ),
        widget.Prompt(
                 font="Ubuntu Mono",
                 fontsize=14,
                 foreground=colors[1]
        ),
        widget.GroupBox(
                 fontsize=11,
                 margin_y=5,
                 margin_x=5,
                 padding_y=0,
                 padding_x=1,
                 borderwidth=3,
                 active=colors[8],
                 inactive=colors[1],
                 rounded=False,
                 highlight_color=colors[2],
                 highlight_method="line",
                 this_current_screen_border=colors[7],
                 this_screen_border=colors[4],
                 other_current_screen_border=colors[7],
                 other_screen_border=colors[4],
                 ),
        widget.TextBox(
                 text='|',
                 font="Ubuntu Mono",
                 foreground=colors[1],
                 padding=2,
                 fontsize=14
                 ),
        widget.CurrentLayoutIcon(
                 # custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                 foreground=colors[1],
                 padding=4,
                 scale=0.6
                 ),
        widget.CurrentLayout(
                 foreground=colors[1],
                 padding=5
                 ),
        widget.TextBox(
                 text='|',
                 font="Ubuntu Mono",
                 foreground=colors[1],
                 padding=2,
                 fontsize=14
                 ),
        widget.WindowName(
            foreground=colors[6],
            max_chars=40,
            decorations=[
                PowerLineDecoration(path="arrow_right", colour=colors[1])
            ]
        ),
        widget.GenPollText(
            update_interval=300,
            func=lambda: subprocess.check_output("printf $(uname -r)", shell=True, text=True),
            foreground=colors[0],  # Texto en negro
            background=colors[3],  # Fondo en color terciario
            fmt='❤  {}',
            padding=6,
            decorations=[
                PowerLineDecoration(path="arrow_right")
            ]
        ),
        widget.CPU(
            format='▓  Cpu: {load_percent}%',
            foreground=colors[0],  # Texto en negro
            background=colors[4],  # Fondo en color cuaternario
            padding=6,
            decorations=[
                PowerLineDecoration(path="arrow_right")
            ]
        ),
        widget.Memory(
            foreground=colors[0],  # Texto en negro
            background=colors[8],  # Fondo en color secundario oscuro
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            format='{MemUsed: .0f}{mm}',
            fmt='🖥  Mem: {} used',
            padding=6,
            decorations=[
                PowerLineDecoration(path="arrow_right", colour=colors[8])
            ]
        ),
        widget.DF(
            update_interval=60,
            foreground=colors[0],  # Texto en negro
            background=colors[5],  # Fondo en color terciario oscuro
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e df')},
            partition='/',
            format='{uf}{m} free',
            fmt='🖴  Disk: {}',
            visible_on_warn=False,
            padding=6,
            decorations=[
                PowerLineDecoration(path="arrow_right", colour=colors[5])
            ]
        ),
        widget.Volume(
            foreground=colors[0],  # Texto en negro
            background=colors[7],  # Fondo en color cuaternario oscuro
            fmt='🕫  Vol: {}',
            padding=6,
            decorations=[
                PowerLineDecoration(path="arrow_right", colour=colors[7])
            ]
        ),
        widget.KeyboardLayout(
            foreground=colors[0],  # Texto en negro
            background=colors[4],  # Fondo en color cuaternario
            fmt='⌨  Kbd: {}',
            padding=6,
            configured_keyboards=['us', 'latam'],
            decorations=[
                PowerLineDecoration(path="arrow_right", colour=colors[4])
            ]
        ),
        widget.Clock(
            foreground=colors[0],  # Texto en negro
            background=colors[8],  # Fondo en color secundario oscuro
            format="⏱  %a, %b %d - %H:%M",
            padding=6,
            decorations=[
                PowerLineDecoration(path="arrow_right")
            ]
        ),
        widget.Systray(padding=3),
    ]
    return widgets_list

def init_widgets_screen1():
    return init_widgets_list()

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[22:24]
    return widgets_screen2
