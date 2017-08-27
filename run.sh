#!/bin/bash

# usage: ./run.sh jobOptions.py useAsyncPrefetching(0/1) athena_log.out free_log.out
rm -f AOD_copy.pool.root  PoolFileCatalog.xml PoolFileCatalog.xml.BAK ntuple.perfmon.summary.txt

echo "TFile.AsyncPrefetching $2" > .rootrc

#free -m -s 1 > $4 &
#top -u gpapadro -d 1 -b > $4 &
#FREE_PID=$!
athena $1 >  $3
#kill $FREE_PID
