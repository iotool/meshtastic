#!/usr/bin/env python

import sys, json, datetime, time, requests

pname = sys.argv[1]
pfile = sys.argv[2]
plink = sys.argv[3]

print("meshtastic-thingspeak: "+pname+" "+pfile)

meshinfo_file = open(pfile, mode="r") # open(pfile, mode="r", encoding="utf-8")
time_now_sec = (datetime.datetime.now() + datetime.timedelta(hours=6) - datetime.datetime(1970,1,1,0,0,0)).total_seconds()
time_out_sec = 30*60
meshinfo_ok = False

for meshinfo_line in meshinfo_file:
    if meshinfo_line.startswith('Nodes in mesh: '):
        meshinfo_ok = True
        meshinfo_nodes = json.loads(meshinfo_line[len('Nodes in mesh: '):])
        for meshinfo_nodeid in meshinfo_nodes:
            print(meshinfo_nodes[meshinfo_nodeid]['user']['shortName'])
            if pname in meshinfo_nodes[meshinfo_nodeid]['user']['shortName']:
                print(meshinfo_nodes[meshinfo_nodeid])
                time_last_sec = time_now_sec-meshinfo_nodes[meshinfo_nodeid]['lastHeard']
                node_bat = str(round(meshinfo_nodes[meshinfo_nodeid]['deviceMetrics']['batteryLevel'],2))
                node_vlt = str(round(meshinfo_nodes[meshinfo_nodeid]['deviceMetrics']['voltage'],3))
                node_air = str(round(meshinfo_nodes[meshinfo_nodeid]['deviceMetrics']['airUtilTx'],2))
                node_cnu = str(round(meshinfo_nodes[meshinfo_nodeid]['deviceMetrics']['channelUtilization'],2))
                node_snr = str(round(meshinfo_nodes[meshinfo_nodeid]['snr'],2))
                node_min = str(round((time_now_sec-meshinfo_nodes[meshinfo_nodeid]['lastHeard'])/60,2))
                status = pname
                if float(node_min) > 100:
                    node_min = str(-1)
                if time_last_sec <= time_out_sec:
                    print("OK: in-time")
                    thingspeak_url = plink+"&field1="+node_bat+"&field2="+node_vlt+"&field3="+node_air+"&field4="+node_cnu+"&field5="+node_snr+"&field6="+node_min+"&status="+status
                else:
                    print("WARN: timeout")
                    thingspeak_url = plink+"&field4=0&field6="+node_min+"&status="+status
                print(thingspeak_url)
                response = requests.get(thingspeak_url)
                print(response.text)
                # thingspeak_file.write(ascii("curl \""+thingspeak_url+"\"")[1:-1])

if not meshinfo_ok:
    print("Fehler kein JSON")

meshinfo_file.close()
