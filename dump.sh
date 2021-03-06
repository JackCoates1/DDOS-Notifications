#!/bin/sh
#!/usr/bin/env python

export pktname
export pkt

interface=venet0
dumpdir=/root/dumps/
 
while /bin/true; do
  pkt_old=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'`
  sleep 1
  pkt_new=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'`
 
  pkt=$(( $pkt_new - $pkt_old ))
  echo -ne "\r$pkt packets/s\033[0K"
 
  if [ $pkt -gt 750 ]; then
  python webhook.py
    echo "\nD\nD\no\nS\n Under Attack, Capturing Packets..."
    pktname="dump_date +"%d-%m-%Y_%H:%M:%S".pcap"
    tcpdump -n -s0 -c 10000 -w $dumpdir/dump_`date +"%d-%m-%Y_%H:%M:%S"`.pcap
    echo "Going to sleep for 1 minute."
    sleep 150
  fi
done
