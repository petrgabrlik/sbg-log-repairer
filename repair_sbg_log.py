'''
This script repairs the line feed issue in the SBG Ellipse-E NMEA log

SBG Ellipse-E supports 6 types of NMEA messages:
$GPGGA, $GPRMC, $GPZDA, $GPHDT, $GPGST, $PRDID

$PRDID message contains two issues. There is no checksum and there is no line
feed character. This script adds line feed to this message and saves the log
to a new file.

Original NMEA log:
$GPGGA,114604.66,4913.707791,N,01634.297317,E,4,15,0.0,302.440,M,44.831,M,,*69
$GPRMC,114604.66,A,4913.707791,N,01634.297317,E,0.012,129.62,230217,4.25,E,R,S*5D
$GPZDA,114604.66,23,02,2017,,*67
$GPHDT,189.80,T*0D
$GPGST,114604.66,0.000,0.000,0.000,86.42,0.03,0.03,0.03*6A
$PRDID,-000.16,-000.47,185280$GPGGA,114606.90,4913.707794,N,01634.297321,E,4,15,0.0,302.449,M,44.831,M,,*6B

Repaired NMEA log:
$GPGGA,114604.66,4913.707791,N,01634.297317,E,4,15,0.0,302.440,M,44.831,M,,*69
$GPRMC,114604.66,A,4913.707791,N,01634.297317,E,0.012,129.62,230217,4.25,E,R,S*5D
$GPZDA,114604.66,23,02,2017,,*67
$GPHDT,189.80,T*0D
$GPGST,114604.66,0.000,0.000,0.000,86.42,0.03,0.03,0.03*6A
$PRDID,-000.16,-000.47,185280
$GPGGA,114606.90,4913.707794,N,01634.297321,E,4,15,0.0,302.449,M,44.831,M,,*6B
'''

def find(s, ch):
    '''
    This function finds all occurrences of the substring and returns their indexes.
    '''
    return [i for i, ltr in enumerate(s) if ltr == ch]

log = 'ttyS1_2016_05_05_21_34_05_073.txt'
print(find(log, '.')[-1])
source = open(log)
dest = open(log[:find(log, '.')[-1]]+'_repaired'+log[find(log, '.')[-1]:], 'a')

for line in source:
    dollar_pos = find(line, '$')
    if len(dollar_pos) == 2:
        print(line[:dollar_pos[1]] + '\n', line[dollar_pos[1]:], sep='', end='', file=dest)
    else:
        print(line, end='', file=dest)
