from libqtile.config import Screen
import subprocess
import os
from modules.keys import keys
from modules.mouse import mouse
from modules.layouts import layouts, floating_layout
from modules.widgets import init_widgets_screen1, init_widgets_screen2
from modules.themes import Dracula
from libqtile import bar, hook
from modules.groups import groups
from libqtile.config import Key
from libqtile import hook, qtile
from libqtile.lazy import lazy
import os
import psutil

# Colores
colors = Dracula

# Pantallas
def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()

# Configuraciones generales
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# Layouts
layouts = layouts  # Asignar layouts importados

# Floating layout
floating_layout = floating_layout

mouse = mouse  # Asignar mouse importado

groups = groups


# Función para obtener el directorio de trabajo del proceso
def get_process_cwd(pid):
    try:
        p = psutil.Process(pid)
        return p.cwd()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return None

# Hook para manejar nuevas ventanas
@hook.subscribe.client_new
def move_editor_to_group(window):
    editors = ["intellij", "code", "pycharm", "idea"]
    wm_class = window.window.get_wm_class()[0].lower()

    if any(editor in wm_class for editor in editors):
        pid = window.window.get_net_wm_pid()
        cwd = get_process_cwd(pid)

        if cwd:
            group_name = os.path.basename(cwd)
            if group_name not in qtile.groups_map:
                qtile.add_group(group_name, layout='max')
                # Agregar un atajo de teclado para el nuevo grupo
                mod = "mod4"
                keys.extend([
                    Key([mod, "control"], str(i), lazy.group[group_name].toscreen(), desc=f"Switch to group {group_name}")
                    for i in range(1, 10)
                ])
            window.togroup(group_name)
            qtile.groups_map[group_name].toscreen()