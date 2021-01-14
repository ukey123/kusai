#!/bin/sh

hub-ctrl -b 1 -d 2 -P 2 -p 0
hub-ctrl -b 1 -d 2 -P 1 -p 0
/opt/vc/bin/tvservice --off
echo "powersave"|tee /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
