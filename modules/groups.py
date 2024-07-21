from libqtile.config import Group
from .keys import keys, mod
from libqtile.lazy import lazy
from libqtile.config import Group, Key
from libqtile import qtile

#group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#group_layouts = ["monadtall", "monadtall", "tile", "tile", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

group_names = ["1", "2", "3"]
group_labels = ["1", "2", "3"]
group_layouts = ["monadtall", "monadtall", "tile"]

groups = [Group(name=group_names[i], layout=group_layouts[i].lower(), label=group_labels[i]) for i in range(len(group_names))]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False), desc="Move focused window to group {}".format(i.name))
    ])

