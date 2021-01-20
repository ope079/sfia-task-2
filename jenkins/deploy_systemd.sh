#!/bin/bash

# Install application to /opt/
rm -r /opt/todo-list
mkdir /opt/todo-list
cp -r . /opt/todo-list

# Generate service file
cat << EOF > sfia-task-2.service
[Unit]
Description=SFIA TASK 2
[Service]
User=jenkins
Environment=DATABASE_URI=$DATABASE_URI
Environment=SECRET_KEY=$SECRET_KEY
ExecStart=/bin/bash /opt/sfia-task-2/jenkins/startup.sh
[Install]
WantedBy=multi-user.target
EOF

# Move service file to systemd
sudo cp sfia-task-2.service /etc/systemd/system/sfia-task-2.service

# systemd reload/start/stop
sudo systemctl daemon-reload
sudo systemctl stop sfia-task-2
sudo systemctl start sfia-task-2