#!/bin/bash -x

cp ./dengonban.service /etc/systemd/system/
chmod 700 /home/nononononobuchan/gcp-compute-engine/app_v1/app.py
systemctl daemon-reload

