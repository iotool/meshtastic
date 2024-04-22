# Meshtastic Documentation

Extension to the official documentation of https://meshtastic.org/docs/introduction/

## Low-Voltage Protection

The firmware try to protect against deep discharge and destruction of the battery. If the voltage falls below 3.10 volts, the node is switched off by a shutdown.

_In the source code [Power.cpp](https://github.com/meshtastic/firmware/blob/master/src/Power.cpp), powerFSM.trigger(EVENT_LOW_BATTERY) is triggering sleep when the battery has less than 0% and is been below 3.10 volts 10 times. After 30 minutes unpowered [PowerFSMThread.h](https://github.com/meshtastic/firmware/blob/master/src/PowerFSMThread.h) the device powerFSM.trigger(EVENT_SHUTDOWN). Shutdown in [PowerFSM.h](https://github.com/meshtastic/firmware/blob/master/src/PowerFSM.h) force a full shutdown now (not just sleep) and [shutdown.h](https://github.com/meshtastic/firmware/blob/master/src/shutdown.h) exec power->shutdown() and [Power.cpp](https://github.com/meshtastic/firmware/blob/master/src/Power.cpp) exec doDeepSleep(DELAY_FOREVER, false)._

Presumption: The "Shutdown after losing power" option in [Power Configuration](https://meshtastic.org/docs/configuration/radio/power/) can be used to set the time after which the device is switched off when the battery is discharged to 0%. With power saving disabled shutdown implements deep sleep of 4.294.967.295 seconds (136 years) "super deep sleep duration" and as router device with power saving enabled shutdown implements deep sleep of 86.400 seconds (24 hours) "super deep sleep duration".

