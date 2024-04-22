#!/usr/bin/sh

# config

export usenodehost=192.168.0.99
export lognodeshort=NODE
export logintervalminutes=15
export tmpnodedata=/tmp/meshtastic-node-data.txt
export thingspeakurl=https://api.thingspeak.com/update?api_key=XXXXXXXXXXXXX

# script

export dumpinfo=false

if [ -f $tmpnodedata ]; then
  echo "note: $tmpnodedata exists"
  export dumpinfo=true
  export newfileexists="$(find $tmpnodedata -cmin -$logintervalminutes -type f)"
  if [ "$newfileexists" = "$tmpnodedata" ]; then
    echo "note: $tmpnodedata < $logintervalminutes minutes"
    export dumpinfo=false
  fi
else
  echo "note: $tmpnodedata not exists"
  export dumpinfo=true
fi

if [ "$dumpinfo" = "true" ]; then
  echo "note: $tmpnodedata dump"
  sudo /usr/local/bin/meshtastic --host $usenodehost --info > $tmpnodedata
  if [ $? -eq 0 ]; then
    echo "info: $tmpnodedata successful"
    cat $tmpnodedata
    python3 /usr/local/src/meshtastic-thingspeak-parse.py $lognodeshort $tmpnodedata $thingspeakurl
  else
    echo "fail: $tmpnodedata timeout" >&2
    rm $tmpnodedata
  fi
fi
