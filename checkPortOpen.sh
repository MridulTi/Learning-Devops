#!/bin/bash

service=$1

result=$(netstat -nltup | grep "$service")
if [ $? -ne 0 ];then
	echo "Error: $result"
	exit 1
else
	echo "$result"
fi
