# Thingspeak Monitor - Meshtastic CLI

I use this to monitor my solar powered node during development.

* update thingspeak every 15 minutes by cron job
* export node info by meshtastic cli (redirect output to textfile)
* parse nodeinfo from textfile and thingspeak update by python script

## Thinkspeak Channel Settings

* Field 1 = BAT = battery level
* Field 2 = VLT = voltage
* Field 3 = AIR = air utilisation
* Field 4 = CNU = channel utilisation
* Field 5 = SNR = signal-to-noise ratio
* Field 6 = MIN = minutes last update

## Mesh Network

Multiple nodes:

* target node can disable Bluetooth and enable power saving
* indirect monitoring of your target node by other mesh node
* use WiFi of the mesh node to connect your raspberry-pi
* use target short node name for select node info 

## Customize Scripts

meshtastic-thingspeak.sh

* change usenodehost to static IP address of mesh node
* change lognodeshort to short node name of target node
* change thingspeakurl to your thingspeak API key

## Run Monitor

```
sudo crontab -e
*/3 * * * * sudo -u pi -p YourPassword /usr/local/src/meshtastic-thingspeak.sh 1>/dev/null 2>/dev/null
```

* cron starts meshtastic-thingspeak.sh every 3 minutes
* meshtastic cli export node info
* python parse meshtastic cli output and update thingspeak

The procedure works for me in principle, but under Linux on the Raspberry PI there are problems with Bluetooth.
