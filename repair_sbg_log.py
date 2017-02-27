'''
This script repairs the line feed issue in the SBG Ellipse-E NMEA log

SBG Ellipse-E supports 6 types of NMEA messages:
$GPGGA, $GPRMC, $GPZDA, $GPHDT, $GPGST, $PRDID

$PRDID message contains two issues. There is no checksum and there is
no line feed character. Checksum issue can't be repaired.

This script adds line feed to this message and saves the log to a new
file. This script can be usead as a module by calling repair() function
with one argument (log file) from another script/module.

Original NMEA log:
$GPGGA,114604.66,4913.707791,N,01634.297317,E,4,15,0.0,302.440,M,44.831,M,,*69
$GPRMC,114604.66,A,4913.707791,N,01634.297317,E,0.012,129.62,230217,4.25,E,R,S*5D
$GPZDA,114604.66,23,02,2017,,*67
$GPHDT,189.80,T*0D
$GPGST,114604.66,0.000,0.000,0.000,86.42,0.03,0.03,0.03*6A
$PRDID,-000.16,-000.47,185280$GPGGA,114606.90,4913.707794,N,01634.297321,E,4,15,0.0,302.449,M,44.831,M,,*6B
                             ^
                     line feed missing

Repaired NMEA log:
$GPGGA,114604.66,4913.707791,N,01634.297317,E,4,15,0.0,302.440,M,44.831,M,,*69
$GPRMC,114604.66,A,4913.707791,N,01634.297317,E,0.012,129.62,230217,4.25,E,R,S*5D
$GPZDA,114604.66,23,02,2017,,*67
$GPHDT,189.80,T*0D
$GPGST,114604.66,0.000,0.000,0.000,86.42,0.03,0.03,0.03*6A
$PRDID,-000.16,-000.47,185280
$GPGGA,114606.90,4913.707794,N,01634.297321,E,4,15,0.0,302.449,M,44.831,M,,*6B
'''

import sys

def find(s, ch):
    '''
    This function finds all occurrences of the substring and returns
    their indexes.
    '''
    return [i for i, ltr in enumerate(s) if ltr == ch]

def repair(log):
    '''
    Repair SBG NMEA log
    '''
    source = open(log)
    dest = open(log[:find(log, '.')[-1]] + '_repaired'
                + log[find(log, '.')[-1]:], 'a')

    repair_counter = 0
    for line in source:
        dollar_pos = find(line, '$')
        if len(dollar_pos) == 2:
            print(line[:dollar_pos[1]] + '\n', line[dollar_pos[1]:], sep='',
                end='', file=dest)
            repair_counter += 1
        else:
            print(line, end='', file=dest)

    return repair_counter

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("Finished: {:} messages repaired.".format( repair(sys.argv[1]) ))
    else:
        print("Argument missing: pass log file as the argument")
