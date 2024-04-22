# Thingspeak Monitor - Meshtastic CLI

I use this to monitor my solar powered node during development.

* update thingspeak every 15 minutes
* export node info by meshtastic cli (redirect output to textfile)
* parse nodeinfo from textfile by python script
* create shellscript with curl for thingspeak update

## Thinkspeak Channel Settings

* Field 1 = BAT = battery level
* Field 2 = VLT = voltage
* Field 3 = AIR = air utilisation
* Field 4 = CNU = channel utilisation
* Field 5 = SNR = signal-to-noise ratio
* Field 6 = MIN = minutes last update

## Mesh Network

Single node:

* target node has Bluetooth enabled and no power saving
* direct monitoring of your target node
* use Bluetooth MAC of the target node to connect your computer
* use target short node name for select node info 

Multiple nodes:

* target node can disable Bluetooth and enable power saving
* indirect monitoring of your target node by other mesh node
* use Bluetooth MAC of the mesh node to connect your computer
* use target short node name for select node info 

## Customize Scripts

meshtastic-thingspeak-loop.cmd

* change Python environment command "active.bat" regarding your installation
* detect Bluetooth MAC of your target node (run meshtastic-thingspeak-loop.cmd)
* change file meshtastic-thingspeak-loop.cmd and set Bluetooth MAC

meshtastic-thingspeak-parse.py

* get Write API Key from thingspeak.com
* change file meshtastic-thingspeak-parse.py and set API Key and short node name

## Run Monitor

I quickly hacked together the process. Not beautiful, but it works:

* after change settings in script files run meshtastic-thingspeak-loop.cmd
* meshtastic cli display Bluetooth scan
* meshtastic cli export node info
* windows start timeout 150 seconds (and maybe kill frozen meshtastic.exe)
* python parse meshtastic cli output
* curl execute thingspeak update

This usually works reliably under Windows. However, the Meshtastic CLI sometimes hangs. That is why I have integrated the timeout and kill the meshtastic.exe if it is still running.
