# Raspberry PI

## Bluetooth connection pairing

```
sudo bluetoothctl
discoverable on
pairable on
agent on
default-agent
scan on
[xxx] Device xx:xx:xx:xx:xx:xx NODE_xxxx
scan off
pair xx:xx:xx:xx:xx:xx
pin > 123456
[CHG] Device xx:xx:xx:xx:xx:xx Paired: yes
Pairing successful
connect xx:xx:xx:xx:xx:xx
```
