import xml.etree.ElementTree as ET
import pyperclip
import sys
import time
import os.path
from os import path

try:
    droppedFile = sys.argv[1]
    if not path.exists(droppedFile):
        print("invalid path")
        time.sleep(3)
        exit()
except:
    print("nofile!")
    time.sleep(3)
    exit()
   
print(droppedFile)

tree = ET.parse(droppedFile)
root = tree.getroot()

time = list()
depth = list()
ppO2 = list()
ppO2s = list()
firstStopD = list()
firstStopT = list()
currNDL = list()
temp = list()
p0 = list()
warnDeco = list()

for record in root.iter('diveLogRecord'):
    time.append(int(int(record.find('currentTime').text)/1000))
    depth.append(int(float(record.find('currentDepth').text)*100))
    ppO2.append(int(float(record.find('averagePPO2').text)*100))
    ppO2s.append(record.find('fractionO2').text)
    firstStopD.append(int(record.find('firstStopDepth').text))
    firstStopT.append(int(record.find('firstStopTime').text))
    currNDL.append(int(record.find('currentNdl').text))
    temp.append(int(int(record.find('waterTemp').text)*10))
    
    # Set to 0 if no coms
    tmpP = record.find('tank0pressurePSI').text
    try: 
        tmpPi = int(tmpP)  
    except ValueError:
        tmpPi = int(0)
    p0.append(int(tmpPi*0.689475729))
    
    if int(record.find('firstStopDepth').text) != 0:
        warnDeco.append(1)
    else:
        warnDeco.append(0)
        

i = 0
s1 = ""
s2 = ""
s3 = ""
s4 = ""
s5 = ""
for t in time:
    s1 = s1 + "{:05d}".format(depth[i]) + "{:01d}".format(warnDeco[i]) + "000000"
    s2 = s2 + "{:03d}".format(temp[i]) + "{:04d}".format(p0[i]) + "0000"
    s4 = s4 + "{:03d}".format(currNDL[i]) + "{:03d}".format(firstStopT[i]) + "{:03d}".format(firstStopD[i])
    s5 = s5 + "{:03d}".format(ppO2[i]) + "0000000000000000"
    i = i + 1
    
s = "DivinglogProfile:10:" + s1 + ":" + s2 + ":" + s3 + ":" + s4 + ":" + s5

pyperclip.copy(s)