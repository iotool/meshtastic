# Meshtastic Documentation

Extension to the official documentation of https://meshtastic.org/docs/introduction/

## Low-Voltage Protection

The firmware try to protect against deep discharge and destruction of the battery. If the voltage falls below 3.10 volts, the node is switched off by a shutdown.

_In the source code [Power.cpp](https://github.com/meshtastic/firmware/blob/master/src/Power.cpp), powerFSM.trigger(EVENT_LOW_BATTERY) is triggering sleep when the battery has less than 0% and is been below 3.10 volts 10 times. After 30 minutes unpowered [PowerFSMThread.h](https://github.com/meshtastic/firmware/blob/master/src/PowerFSMThread.h) the device powerFSM.trigger(EVENT_SHUTDOWN). Shutdown in [PowerFSM.h](https://github.com/meshtastic/firmware/blob/master/src/PowerFSM.h) force a full shutdown now (not just sleep) and [shutdown.h](https://github.com/meshtastic/firmware/blob/master/src/shutdown.h) exec power->shutdown() and [Power.cpp](https://github.com/meshtastic/firmware/blob/master/src/Power.cpp) exec doDeepSleep(DELAY_FOREVER, false)._

Presumption: The "Shutdown after losing power" option in [Power Configuration](https://meshtastic.org/docs/configuration/radio/power/) can be used to set the time after which the device is switched off when the battery is discharged to 0%. With power saving disabled shutdown implements a deep sleep of 4.294.967.295 seconds (136 years) "super deep sleep duration". The power-on or reset button must be used to wake up the device. As router device with power saving enabled shutdown implements deep sleep of 86.400 seconds (24 hours) "super deep sleep duration". After 24 hours, the device wakes up automatically and checks again whether the charge is 0%.

## Solar powered Router Node

The range for the mesh network can be improved with router nodes in an exposed position. The power supply is preferably provided by solar panels.

Reduce power consumption - example TLoRa v2.1_1.6 (reduce 50mA to 18mA current consumption):

* Device Role: "ROUTER" instead of "CLIENT"
* Device Rebroadcast: LOCAL_ONLY (just public and your admin traffic)
* Device Serial: disabled
* Bluetooth: disabled (use admin channel to change config)
* LoRa TX power: 20 dBm ~ 100mW (14 dBm ~ 25 mW)
* LoRa ignore MQTT
* Power saving: enabled (overwrite ADC and duration) 
* Power ADC multiplier: 1.8 (shutdown at 20% battery)
* Power duration: shutdown 0s, bluetooth 1s, super 3600, light 3600, minimum 10s

The ESB32 consumes a lot of energy and is set to sleep mode as far as possible. For LoRa, only the minimum necessary data packets are re-sent in the mesh.

## Time Synchronization

[Feature Request](https://github.com/meshtastic/firmware/issues/3171) Current Time/Clock Functionality #3171 - it gets it from the app, gps or mesh. You also only need one device with time, it should send the time across the mesh to the other devices and they'll sync up - [Screen.cpp](https://github.com/meshtastic/firmware/blob/250cf16bf8793aefed95b9cedb9c20b2f2e7a2a7/src/graphics/Screen.cpp#L1899)

At least 1 node in a private group must have an active GPS in order to generate the system time.
