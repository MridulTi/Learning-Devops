#!/bin/bash

directoryToBackup=$1
LOG_FILE=/var/log/bashtest
LOG_NAME="$LOG_FILE/directoryToBackup.log"

if [ ! -d "$LOG_FILE" ];then
	mkdir -p "$LOG_FILE"
	echo "log file created" >> "$LOG_NAME"
fi

if [ ! -d "/opt/backups/$directoryToBackup" ];then
        mkdir -p "/opt/backups/"$directoryToBackup""
        echo "Backup Directory created" >> "$LOG_NAME"
fi

echo "Creating Backup to $directoryToBackup" >> "$LOG_NAME"
cp -r "$directoryToBackup" /opt/backups/"$directoryToBackup"
echo "Backup created..." >> "$LOG_NAME"
