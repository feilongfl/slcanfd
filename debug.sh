#!/usr/bin/env fish
###
 # @Author: feilong
 # @LastEditors: feilong
 # @Description: 
 # @email: feilongphone@gmail.com
### 

killall slcand
rmmod -f slcanfd
rmmod -f slcan
make install
slcand -o -c -f -s6 $argv
ip link set slcan0 up
echo can dump ...
candump slcan0
