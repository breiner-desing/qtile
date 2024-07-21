# Qtile Keybindings

Este archivo documenta los atajos de teclado configurados en Qtile.

## Teclas de Modificador

- `mod4`: Tecla SUPER/WINDOWS
- `shift`: Tecla SHIFT
- `control`: Tecla CONTROL

## Atajos de Teclado

| Combinación de Teclas       | Acción                                               | Descripción                                        |
|-----------------------------|------------------------------------------------------|----------------------------------------------------|
| `mod4 + Return`             | `lazy.spawn(myTerm)`                                 | Abrir terminal                                     |
| `mod4 + shift + Return`     | `lazy.spawn("rofi -show drun")`                      | Lanzador de aplicaciones                           |
| `mod4 + b`                  | `lazy.spawn(myBrowser)`                              | Abrir navegador web                                |
| `mod4 + Tab`                | `lazy.next_layout()`                                 | Alternar entre layouts                             |
| `mod4 + shift + c`          | `lazy.window.kill()`                                 | Cerrar ventana enfocada                            |
| `mod4 + shift + r`          | `lazy.reload_config()`                               | Recargar configuración                             |
| `mod4 + shift + q`          | `lazy.spawn("dm-logout -r")`                         | Menú de cierre de sesión                           |
| `mod4 + r`                  | `lazy.spawncmd()`                                    | Ejecutar comando mediante un widget de prompt      |
| `mod4 + h`                  | `lazy.layout.left()`                                 | Mover foco a la izquierda                          |
| `mod4 + l`                  | `lazy.layout.right()`                                | Mover foco a la derecha                            |
| `mod4 + j`                  | `lazy.layout.down()`                                 | Mover foco hacia abajo                             |
| `mod4 + k`                  | `lazy.layout.up()`                                   | Mover foco hacia arriba                            |
| `mod4 + space`              | `lazy.layout.next()`                                 | Mover foco a otra ventana                          |
| `mod4 + shift + s`          | `lazy.spawn("scrot ~/Pictures/screenshot_%Y-%m-%d-%H-%M-%S.png")` | Captura de pantalla completa                       |
| `mod4 + shift + p`          | `lazy.spawn("scrot -s ~/Pictures/screenshot_%Y-%m-%d-%H-%M-%S.png")` | Captura de pantalla de una selección               |
| `mod4 + shift + h`          | `lazy.layout.shuffle_left(), lazy.layout.move_left().when(layout=["treetab"])` | Mover ventana a la izquierda/mover pestaña izquierda en treetab |
| `mod4 + shift + l`          | `lazy.layout.shuffle_right(), lazy.layout.move_right().when(layout=["treetab"])` | Mover ventana a la derecha/mover pestaña derecha en treetab |
| `mod4 + shift + j`          | `lazy.layout.shuffle_down(), lazy.layout.section_down().when(layout=["treetab"])` | Mover ventana hacia abajo/mover sección abajo en treetab |
| `mod4 + shift + k`          | `lazy.layout.shuffle_up(), lazy.layout.section_up().when(layout=["treetab"])` | Mover ventana hacia arriba/mover sección arriba en treetab |
| `mod4 + shift + space`      | `lazy.layout.toggle_split()`                         | Alternar entre lados divididos y no divididos del stack |
| `mod4 + shift + a`          | `add_treetab_section`                                | Agregar nueva sección en treetab                   |
| `mod4 + equal`              | `lazy.layout.grow_left().when(layout=["bsp", "columns"]), lazy.layout.grow().when(layout=["monadtall", "monadwide"])` | Expandir ventana hacia la izquierda                |
| `mod4 + minus`              | `lazy.layout.grow_right().when(layout=["bsp", "columns"]), lazy.layout.shrink().when(layout=["monadtall", "monadwide"])` | Reducir ventana hacia la derecha                   |
| `mod4 + control + h`        | `lazy.layout.grow_left()`                            | Expandir ventana hacia la izquierda                |
| `mod4 + control + l`        | `lazy.layout.grow_right()`                           | Expandir ventana hacia la derecha                  |
| `mod4 + control + j`        | `lazy.layout.grow_down()`                            | Expandir ventana hacia abajo                       |
| `mod4 + control + k`        | `lazy.layout.grow_up()`                              | Expandir ventana hacia arriba                      |
| `mod4 + n`                  | `lazy.layout.normalize()`                            | Resetear tamaños de ventana                        |
| `mod4 + m`                  | `lazy.layout.maximize()`                             | Alternar entre tamaños mínimo y máximo             |
| `mod4 + t`                  | `lazy.window.toggle_floating()`                      | Alternar ventana flotante                          |
| `mod4 + s`                  | `maximize_by_switching_layout(), lazy.window.toggle_fullscreen()` | Alternar pantalla completa                         |
| `mod4 + shift + m`          | `minimize_all()`                                     | Ocultar/mostrar todas las ventanas en el grupo actual |
| `mod4 + period`             | `lazy.next_screen()`                                 | Mover foco al siguiente monitor                    |
| `mod4 + comma`              | `lazy.prev_screen()`                                 | Mover foco al monitor anterior                     |
| `mod4 + e`                  | KeyChord para lanzar programas en Emacs              | Ver siguiente sección                              |

## KeyChord para Emacs

| Combinación de Teclas       | Acción                                               | Descripción                                        |
|-----------------------------|------------------------------------------------------|----------------------------------------------------|
| `mod4 + e + e`              | `lazy.spawn(myEmacs)`                                | Emacs Dashboard                                    |
| `mod4 + e + a`              | `lazy.spawn(myEmacs + "--eval '(emms-play-directory-tree \"~/Music/\")'")` | Emacs EMMS                                         |
| `mod4 + e + b`              | `lazy.spawn(myEmacs + "--eval '(ibuffer)'")`         | Emacs Ibuffer                                      |
| `mod4 + e + d`              | `lazy.spawn(myEmacs + "--eval '(dired nil)'")`       | Emacs Dired                                        |
| `mod4 + e + i`              | `lazy.spawn(myEmacs + "--eval '(erc)'")`             | Emacs ERC                                          |
| `mod4 + e + s`              | `lazy.spawn(myEmacs + "--eval '(eshell)'")`          | Emacs Eshell                                       |
| `mod4 + e + v`              | `lazy.spawn(myEmacs + "--eval '(vterm)'")`           | Emacs Vterm                                        |
| `mod4 + e + w`              | `lazy.spawn(myEmacs + "--eval '(eww \"distro.tube\")'")` | Emacs EWW                                       |
| `mod4 + e + F4`             | `lazy.spawn("killall emacs"), lazy.spawn("/usr/bin/emacs --daemon")` | Reiniciar Emacs daemon                  |

## KeyChord para Dmenu/Rofi

| Combinación de Teclas       | Acción                                               | Descripción                                        |
|-----------------------------|------------------------------------------------------|----------------------------------------------------|
| `mod4 + p + h`              | `lazy.spawn("dm-hub -r")`                            | Listar todos los scripts dmscripts                 |
| `mod4 + p + a`              | `lazy.spawn("dm-sounds -r")`                         | Elegir sonido ambiental                            |
| `mod4 + p + b`              | `lazy.spawn("dm-setbg -r")`                          | Establecer fondo de pantalla                       |
| `mod4 + p + c`              | `lazy.spawn("dtos-colorscheme -r")`                  | Elegir esquema de colores                          |
| `mod4 + p + e`              | `lazy.spawn("dm-confedit -r")`                       | Elegir archivo de configuración para editar        |
| `mod4 + p + i`              | `lazy.spawn("dm-maim -r")`                           | Captura de pantalla                                |
| `mod4 + p + k`              | `lazy.spawn("dm-kill -r")`                           | Matar procesos                                     |
| `mod4 + p + m`              | `lazy.spawn("dm-man -r")`                            | Ver páginas del manual                             |
| `mod4 + p + n`              | `lazy.spawn("dm-note -r")`                           | Guardar y copiar notas                             |
| `mod4 + p + o`              | `lazy.spawn("dm-bookman -r")`                        | Marcadores del navegador                           |
| `mod4 + p + p`              | `lazy.spawn("rofi-pass")`                            | Menú de cierre de sesión                           |
| `mod4 + p + q`              | `lazy.spawn("dm-logout -r")`                         | Menú de cierre de sesión                           |
| `mod4 + p + r`              | `lazy.spawn("dm-radio -r")`                          | Escuchar radio en línea                            |
| `mod4 + p + s`              | `lazy.spawn("dm-websearch -r")`                      | Buscar en varios motores                           |
| `mod4 + p + t`              | `lazy.spawn("dm-translate -r")`                      | Traducir texto                                     |
