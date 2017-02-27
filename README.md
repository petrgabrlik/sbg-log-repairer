# sbg-log-repairer
Script / module for repairing issues in SBG Ellipse-E NMEA log

---
Docstring from repair_sbg_log.py module:
```
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
```
