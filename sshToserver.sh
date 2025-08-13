#!/bin/bash

key=$1
user=$2
shift

for ip in "$@";do
	ssh -i "$key" "$user"@"$ip"
	if [ $? -eq 0 ];then
		echo "SUCCESS SSH"
	else
		echo "FAIL SSH"
	fi
done
