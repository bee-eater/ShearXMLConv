# ShearXMLConv
This little Python script converts a Shearwater XML file to a Dive Log 6 compatible profile and copies it to your clipboard for direct pasting into Dive Log 6. It helps to import e.g. tank pressure / depth / temperature etc. profiles into existing dives already saved in  Dive Log 6.

# Requirements
- Python 3.8.3 (Should also work with Python 2)
- Python module pyperclip (``pip install pyperclip``)
- Dive Log 6.0.18

# Preparations
Before converting please adjust the time value in the python script. The 10 below states the difference between each record of the file. Default on Shearwater Perdix AI is 10 seconds. If you changed the value on your dive computer, please adjust this value accordingly.

```
s = "DivinglogProfile:10:"
```

# How to use
1. Export your dives from Shearwater Cloud / Desktop in Shearwater xml format
2. Drop a single xml file on the .bat file, this will trigger the script
3. The script will copy the data for Dive Log 6 to your clipboard
4. Open Dive Log 6 and open the dive you want to paste the data to
5. Click on Profile -> Paste Profile, select the data you want to import and confirm

Done! The data should be added to your dive!

# Details
The profile for Dive Log 6 is currently build as follows:

```
DivingLogProfile:10
:
{5} Tiefe [cm] + WarnDeko [bit] + WarnRBT [bit] + WarnAsc [bit] + WarnStop [bit] + WarnWork [bit] + 00
:
{3} Temperatur [0.1°C] + {4} Flaschendruck 1 [0.1bar] + 0000 
:
{4} Flaschendruck 2 [0.1bar] + {4} Flaschendruck 3 [0.1bar] + {3} Heartrate + {3} Compass
:
{3} NDL [min] + {3} StopTime [min] + {3} StopDepth [m]
:
{3} PO2-1 [bar] + {3} PO2-2 [bar] + {3} PO2-3 [bar] + {4} OTU + {4} CNS + {2} Setpoint
```

The sections are divided by ":" and for each section there can be multiple entries written directly behind each other. "{5}" states there should be 5 digits.
