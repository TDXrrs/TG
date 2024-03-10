#!/bin/bash

# turn on bash's job control
set -m

#start the web server
python3 /app/app.py &

#start ssh
/usr/sbin/sshd -D &
# now we bring the primary process back into the foreground
# and leave it there
fg %1