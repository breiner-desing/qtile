from libqtile.lazy import lazy
from libqtile import hook, qtile
from libqtile.config import Group


@lazy.layout.function
def add_treetab_section(layout):
    prompt = qtile.widgets_map["prompt"]
    prompt.start_input("Section name: ", layout.cmd_add_section)

@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

@lazy.function
def maximize_by_switching_layout(qtile):
    current_layout_name = qtile.current_group.layout.name
    if current_layout_name == 'monadtall':
        qtile.current_group.layout = 'max'
    elif current_layout_name == 'max':
        qtile.current_group.layout = 'monadtall'

def create_group(name):
    # Añadir el grupo si no existe
    if name not in qtile.groups_map:
        group = Group(name)
        qtile.add_group(name, group)

@lazy.function
def create_and_switch_group(qtile, name):
    if name not in qtile.groups_map:
        group = Group(name)
        qtile.add_group(name, group)
    qtile.groups_map[name].toscreen()

@hook.subscribe.setgroup
def add_group_on_switch():
    current_group = qtile.current_group.name
    if current_group not in qtile.groups_map:
        create_group(current_group)

def move_window_to_group(group_name):
    def f(qtile):
        # Verificar si el grupo existe, si no, crearlo
        if group_name not in qtile.groups_map:
            qtile.add_group(group_name)
        
        # Obtener la ventana activa
        window = qtile.current_window
        if window is not None:
            # Mover la ventana al grupo especificado
            window.togroup(group_name)
   return f
