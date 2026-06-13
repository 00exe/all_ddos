#!/bin/bash
echo "run this with sudo!"
sudo apt install figlet
clear
sudo apt install python3
clear
cd /home/desktop/ddos_files
echo "TCP-1"
echo "ALL-2"
echo "RIPPER-3"
read -p "Choose:" sc
case $sc in
  1)
     clear
     python3 tcp-ddos.py
     ;;
  2)
     clear
     python3 all-ddos.py
     ;;
esac
