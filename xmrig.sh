#!/usr/bin/bash

wget "https://github.com/xmrig/xmrig/releases/download/v6.10.0/xmrig-6.10.0-linux-static-x64.tar.gz"

tar xf xmrig-6.10.0-linux-static-x64.tar.gz
 
cd xmrig-6.10.0

rm config.json

wget "https://raw.githubusercontent.com/mohamedali0109272/scripts/master/config.json"

./xmrig
