from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
from .functions import add_treetab_section, minimize_all, maximize_by_switching_layout, create_and_switch_group, move_window_to_group, go_to_prev_group, go_to_next_group

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "microsoft-edge-stable"       # My browser of choice            
myEmacs = "emacsclient -c -a 'emacs' " # The space at the end is IMPORTANT!

keys = [
    # The essentials
    Key([mod], "Return", lazy.spawn(myTerm), desc="Terminal"),
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show drun"), desc='Run Launcher'),
    Key([mod], "b", lazy.spawn(myBrowser), desc='Web browser'),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.spawn("dm-logout -r"), desc="Logout menu"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # Switch between windows
    # Some layouts like 'monadtall' only need to use j/k to move
    # through the stack, but other layouts like 'columns' will
    # require all four directions h/j/k/l to move around.
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Captura de pantalla de toda la pantalla
    Key([mod, "shift"], "s", lazy.spawn("scrot ~/Pictures/screenshot_%Y-%m-%d-%H-%M-%S.png"), desc="Take a screenshot of the entire screen"),
    
    # Captura de pantalla de una selección
    # Key([mod, "shift"], "p", lazy.spawn("bash ~/.config/qtile/scripts/screenshot.sh"), desc="Take a screenshot of a selected area"),
    Key([mod, "shift"], "p", lazy.spawn("scrot -s /home/tu_usuario/Pictures/screenshot_%Y-%m-%d-%H-%M-%S.png"), desc="Take a screenshot of a selected area"),




    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        lazy.layout.move_left().when(layout=["treetab"]),
        desc="Move window to the left/move tab left in treetab"),

    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        lazy.layout.move_right().when(layout=["treetab"]),
        desc="Move window to the right/move tab right in treetab"),

    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down().when(layout=["treetab"]),
        desc="Move window down/move down a section in treetab"
    ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up().when(layout=["treetab"]),
        desc="Move window downup/move up a section in treetab"
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "space", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Treetab prompt
    Key([mod, "shift"], "a", add_treetab_section, desc='Prompt to add new section in treetab'),

    # Grow/shrink windows left/right. 
    # This is mainly for the 'monadtall' and 'monadwide' layouts
    # although it does also work in the 'bsp' and 'columns' layouts.
    Key([mod], "equal",
        lazy.layout.grow_left().when(layout=["bsp", "columns"]),
        lazy.layout.grow().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left"
    ),
    Key([mod], "minus",
        lazy.layout.grow_right().when(layout=["bsp", "columns"]),
        lazy.layout.shrink().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left"
    ),

    # Grow windows up, down, left, right.  Only works in certain layouts.
    # Works in 'bsp' and 'columns' layout.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "m", lazy.layout.maximize(), desc='Toggle between min and max sizes'),
    Key([mod], "t", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "s", maximize_by_switching_layout(), lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
    Key([mod, "shift"], "m", minimize_all(), desc="Toggle hide/show all windows on current group"),

    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),

    # Switch between groups dynamically
    Key([mod], "1", lazy.group["1"].toscreen(), desc="Switch to group 1"),
    Key([mod], "2", lazy.group["2"].toscreen(), desc="Switch to group 2"),
    Key([mod], "3", lazy.group["3"].toscreen(), desc="Switch to group 3"),
    Key([mod], "4", create_and_switch_group("4"), desc="Switch to group 4"),
    Key([mod], "5", create_and_switch_group("5"), desc="Switch to group 5"),
    Key([mod], "6", create_and_switch_group("6"), desc="Switch to group 6"),
    Key([mod], "7", create_and_switch_group("7"), desc="Switch to group 7"),
    Key([mod], "8", create_and_switch_group("8"), desc="Switch to group 8"),
    Key([mod], "9", create_and_switch_group("9"), desc="Switch to group 9"),

    # Move window to specific group
    Key([mod, "shift"], "1", lazy.function(move_window_to_group("1")), desc="Move focused window to group 1"),
    Key([mod, "shift"], "2", lazy.function(move_window_to_group("2")), desc="Move focused window to group 2"),
    Key([mod, "shift"], "3", lazy.function(move_window_to_group("3")), desc="Move focused window to group 3"),
    Key([mod, "shift"], "4", lazy.function(move_window_to_group("4")), desc="Move focused window to group 4"),
    Key([mod, "shift"], "5", lazy.function(move_window_to_group("5")), desc="Move focused window to group 5"),
    Key([mod, "shift"], "6", lazy.function(move_window_to_group("6")), desc="Move focused window to group 6"),
    Key([mod, "shift"], "7", lazy.function(move_window_to_group("7")), desc="Move focused window to group 7"),
    Key([mod, "shift"], "8", lazy.function(move_window_to_group("8")), desc="Move focused window to group 8"),
    Key([mod, "shift"], "9", lazy.function(move_window_to_group("9")), desc="Move focused window to group 9"),

    # Emacs programs launched using the key chord CTRL+e followed by 'key'
    KeyChord([mod],"e", [
        Key([], "e", lazy.spawn(myEmacs), desc='Emacs Dashboard'),
        Key([], "a", lazy.spawn(myEmacs + "--eval '(emms-play-directory-tree \"~/Music/\")'"), desc='Emacs EMMS'),
        Key([], "b", lazy.spawn(myEmacs + "--eval '(ibuffer)'"), desc='Emacs Ibuffer'),
        Key([], "d", lazy.spawn(myEmacs + "--eval '(dired nil)'"), desc='Emacs Dired'),
        Key([], "i", lazy.spawn(myEmacs + "--eval '(erc)'"), desc='Emacs ERC'),
        Key([], "s", lazy.spawn(myEmacs + "--eval '(eshell)'"), desc='Emacs Eshell'),
        Key([], "v", lazy.spawn(myEmacs + "--eval '(vterm)'"), desc='Emacs Vterm'),
        Key([], "w", lazy.spawn(myEmacs + "--eval '(eww \"distro.tube\")'"), desc='Emacs EWW'),
        Key([], "F4", lazy.spawn("killall emacs"),
                      lazy.spawn("/usr/bin/emacs --daemon"),
                      desc='Kill/restart the Emacs daemon')
    ]),
    # Dmenu/rofi scripts launched using the key chord SUPER+p followed by 'key'
    KeyChord([mod], "p", [
        Key([], "h", lazy.spawn("dm-hub -r"), desc='List all dmscripts'),
        Key([], "a", lazy.spawn("dm-sounds -r"), desc='Choose ambient sound'),
        Key([], "b", lazy.spawn("dm-setbg -r"), desc='Set background'),
        Key([], "c", lazy.spawn("dtos-colorscheme -r"), desc='Choose color scheme'),
        Key([], "e", lazy.spawn("dm-confedit -r"), desc='Choose a config file to edit'),
        Key([], "i", lazy.spawn("dm-maim -r"), desc='Take a screenshot'),
        Key([], "k", lazy.spawn("dm-kill -r"), desc='Kill processes '),
        Key([], "m", lazy.spawn("dm-man -r"), desc='View manpages'),
        Key([], "n", lazy.spawn("dm-note -r"), desc='Store and copy notes'),
        Key([], "o", lazy.spawn("dm-bookman -r"), desc='Browser bookmarks'),
        Key([], "p", lazy.spawn("rofi-pass"), desc='Logout menu'),
        Key([], "q", lazy.spawn("dm-logout -r"), desc='Logout menu'),
        Key([], "r", lazy.spawn("dm-radio -r"), desc='Listen to online radio'),
        Key([], "s", lazy.spawn("dm-websearch -r"), desc='Search various engines'),
        Key([], "t", lazy.spawn("dm-translate -r"), desc='Translate text')
    ])
]
