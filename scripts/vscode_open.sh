#!/bin/bash

# Abrir un cuadro de diálogo de selección de carpetas
DIR=$(zenity --file-selection --directory --title="Select a Folder")

# Verifica si se seleccionó una carpeta
if [ -n "$DIR" ]; then
    # Abre Visual Studio Code con la carpeta seleccionada
    code "$DIR"
fi
