#!/bin/bash -x

cp ./summary.service /etc/systemd/system/
chmod 700 /home/nononononobuchan/summary/app.py
systemctl daemon-reload

