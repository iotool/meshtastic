# Meshtastic Device Current Consumption

| Device | Current | Mode | Firmware |
|--------|---------|------|----------|
| T-Lora 2.1_1.6 | 51mA @5V | Client | 2.2.24 |
| T-Lora 2.1_1.6 | 18mA @5V | Client_Mute, PwrSave | 2.2.24 |
| T-Lora 2.1_1.6 | 18mA @5V | Router, PwrSave | 2.2.24 |
| T-Lora 2.1_1.6 | 18mA @5V | Repeater, PwrSave | 2.2.24 |
| Heltec V2 | 70mA @5V | Client | 2.2.24 |
| Heltec V3.1 | 111mA @5V | Client | 2.2.24 |
| Heltec V3.1 | 108mA @5V | Client | 2.3.4 |
| Heltec V3.1 | 28mA @5V | Router (PwrSave) | 2.3.4 |
| Heltec V3.1 | 21mA @5V | Router (PwrMin) | 2.3.4 |
| Heltec WST-V3 | 108mA @5V | Client | 2.3.4 |
| Heltec WST-V3 | 28mA @5V | Router (PwrSave) | 2.3.4 |
| Heltec WST-V3 | 21mA @5V | Router (PwrMin) | 2.3.4 |

* PwrSave (default) ~ wait ble 1s, super 86400s=24h, Light 8640s=24h, min wake 10s
* PwrMin (minimal) ~ default + Bluetooth off, serial debug off, rebroadcast local_only, position off

### Heltec LORA32 and ESP32-C3

[sleep.cpp](https://github.com/meshtastic/firmware/blob/250cf16bf8793aefed95b9cedb9c20b2f2e7a2a7/src/sleep.cpp#L78) - Heltec and ESP32C3 may consume more power because Meshtastic does not reduce the CPU clock for this model from 240 MHz to 80 MHz. Leave CPU at full speed during init, but once loop is called switch to low speed (for a 50% power savings)

### Heltec V2 vs. V3

[discourse](https://meshtastic.discourse.group/t/heltec-wifi-lora-32-v3-is-out-will-it-be-supported/6596/12) - normal operation I am measuring a current draw of about 110 mA on the 3.7V line for V3.
For V2 I am measuring about 60 mA. # suspect there are a bunch of opportunities for power savings on these devices, but ESP32-S3 support in Meshtastic is very fresh. I’m sure we’ll uncover those opportunites as support matures.

## Devices

| Device | MCU | LoRa | Bluetooth | PSRAM | Commend |
|--------|-----|------|-----------|-------|---------|
| T-Lora 2.1_1.6 | ESP32 | SX1276 | 4.2 | n/a | |
| Heltec V2 | ESP32-D0 | SX1276 | 4.2 | n/a | |
| Heltec V3.1 | ESP32-S3 | SX1262 | 5 | n/a | |
| Heltec WST-V3 | ESP32-S3 | SX1262 | 5 | n/a | |

## Interval Time Switching 

Power on for 5 minutes every hour for 1.5mA current consumption or 36mAh per day. 

* Shutdown on battery delay (seconds) = uptime (e.g. 300 seconds ~ 5 minutes)
* ADC multiplier = 0.1 to force shutdown after uptime
* super deep sleep duration (seconds) = downtime (e.g. 3300 seconds ~ 55 minutes)

Power on for 16 minutes every hour for 5.33mA current consumption or 128mAh per day. 

* Shutdown on battery delay (seconds) = uptime (e.g. 960 seconds ~ 15 minutes)
* ADC multiplier = 0.1 to force shutdown after uptime
* super deep sleep duration (seconds) = downtime (e.g. 2640 seconds ~ 44 minutes)
