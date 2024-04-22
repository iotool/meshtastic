# Thingspeak Monitor - Meshtastic CLI

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
