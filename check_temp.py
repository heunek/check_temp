#!/usr/bin/python
# coding=utf-8
#----------------
#https://www.do-it-smart.de/2018/01/14/how-to-temperaturueberwachung-mit-icinga2-und-raspberry-pi/
 
import os, sys, time
import argparse

def aktuelleTemperatur() -> float:
    '''Liest aktuelle Temperatur aus und gibt sie als float zurück''' 
    temp_read = os.popen('vcgencmd measure_temp').readline()
    temp_list = list(temp_read)
    temperature = float(''.join(temp_list[5:-3]))

    # Temperatur ausgeben
    rueckgabewert = '%6.1f' % temperature
    return(rueckgabewert)
 
temp = float(aktuelleTemperatur())
 
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--warning', type=int, help='Warning', required=True)
parser.add_argument('-c', '--critical', type=int, help='Critical', required=True)
 
args = parser.parse_args()
 
warn = float(args.warning)
crit = float(args.critical)
 
if temp > crit:
    print("CRITICAL - Die Temperatur liegt bei: " + str(temp) + '° | ' + "temp=" + str(temp) + ';' + str(warn) + ';' + str(crit) + ';')
    sys.exit(2)
elif temp > warn:
    print("WARNING - Die Temperatur liegt bei: " + str(temp) + '° | ' + "temp=" + str(temp) + ';' + str(warn) + ';' + str(crit) + ';')
    sys.exit(1)
elif temp < warn:
    print("OK - Die Temperatur liegt bei: " + str(temp) + '° | ' + "temp=" + str(temp) + ';' + str(warn) + ';' + str(crit) + ';')
    sys.exit(0)
else:
    print("UNKNOWN")
    sys.exit(3)
