# https://thingspeak.com/channels/340397

import json
import datetime, time

# --- Parameter ---

meshnode_short_filter  = "rs1" # dRH5, R1PV, f2f8
meshnode_sec_timeout   = 30*60
thingspeak_url_apikey  = "https://api.thingspeak.com/update?api_key=GPU2202SLA5M2SKP"
meshinfo_filename      = "meshtastic-thingspeak-info.txt"
thingspeak_filename    = "meshtastic-thingspeak-upload.cmd"

# ---- Parser ---

thingspeak_file = open(thingspeak_filename, mode="w")
meshinfo_file = open(meshinfo_filename, mode="r", encoding="utf-8")

time_now_sec = (datetime.datetime.now() - datetime.timedelta(hours=2) - datetime.datetime(1970,1,1,0,0,0)).total_seconds()
meshinfo_ok = False

for meshinfo_line in meshinfo_file:
    if meshinfo_line.startswith('Nodes in mesh: '):
        meshinfo_ok = True
        meshinfo_nodes = json.loads(meshinfo_line[len('Nodes in mesh: '):])
        for meshinfo_nodeid in meshinfo_nodes:
            print(meshinfo_nodes[meshinfo_nodeid]['user']['shortName'])
            if meshnode_short_filter in meshinfo_nodes[meshinfo_nodeid]['user']['shortName']:
                print(meshinfo_nodes[meshinfo_nodeid])
                try:
                    time_last_sec = time_now_sec-meshinfo_nodes[meshinfo_nodeid]['lastHeard']
                except:
                    time_last_sec = time_now_sec-60*60
                try:
                    node_bat = str(round(meshinfo_nodes[meshinfo_nodeid]['deviceMetrics']['batteryLevel'],2))
                    node_vlt = str(round(meshinfo_nodes[meshinfo_nodeid]['deviceMetrics']['voltage'],3))
                    node_air = str(round(meshinfo_nodes[meshinfo_nodeid]['deviceMetrics']['airUtilTx'],2))
                    node_cnu = str(round(meshinfo_nodes[meshinfo_nodeid]['deviceMetrics']['channelUtilization'],2))
                    node_snr = str(round(meshinfo_nodes[meshinfo_nodeid]['snr'],2))
                except:
                    node_bat = "-1"
                    node_vlt = "-1"
                    node_air = "0"
                    node_cnu = "0"
                    node_snr = "0"
                node_min = str(round((time_now_sec-time_last_sec)/60,2))
                status = meshnode_short_filter+","+meshinfo_nodes[meshinfo_nodeid]['user']['longName']+","+meshinfo_nodes[meshinfo_nodeid]['user']['id']
                status = meshnode_short_filter+","+meshinfo_nodes[meshinfo_nodeid]['user']['id']
                if float(node_min) > 100:
                    node_min = str(-1)
                if time_last_sec <= meshnode_sec_timeout:
                    print("OK: in-time")
                    thingspeak_file.write("echo OK in-time\r\n")
                    thingspeak_url = thingspeak_url_apikey+"&field1="+node_bat+"&field2="+node_vlt+"&field3="+node_air+"&field4="+node_cnu+"&field5="+node_snr+"&field6="+node_min+"&status="+status
                else:
                    print("WARN: timeout")
                    thingspeak_file.write("echo WARN time-out\r\n")
                    thingspeak_url = thingspeak_url_apikey+"&field4=0&field6="+node_min+"&status="+status
                print(thingspeak_url)
                thingspeak_file.write(ascii("curl \""+thingspeak_url+"\"")[1:-1])

if not meshinfo_ok:
    print("Fehler kein JSON")
    thingspeak_file.write("echo Fehler kein JSON")

meshinfo_file.close()
thingspeak_file.close()
