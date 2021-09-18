#!bin/bash
# kills picom on specified steam game launches
CHECK=$0
SERVICE=$1
 if pgrep -x "42832" > /dev/null
 then
    echo "CSGO running, killing picom..."
    pkill picom
 else 
    echo "no process identified. Exiting..."
 fi 
     