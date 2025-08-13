#!/bin/bash

cd /home
directory=(*)

listUser=$(cat /etc/passwd | awk -F : '{print $1}')

for user in "${listUser[@]}";do
	if ! echo "$directory" | grep -q "$user"; then
		echo "$user"
	fi
done
