#!/bin/bash

# Terminar instancias de barra que ya se encuentran en ejecución
killall -q polybar
# Si todas tus barras tienen ipc habilitado, también puedes usar
# polybar-msg cmd salir

# Inicie Polybar, utilizando la ubicación de configuración predeterminada ~/.config/polybar/config.ini
polybar mybar 2>&1 | tee -a /tmp/polybar.log & disown

echo "Polybar lanzado..."