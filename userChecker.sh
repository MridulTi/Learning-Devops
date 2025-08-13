#!/bin/bash

# User Checker Script
# Accept a username and print whether the user exists.
# If not, offer to create the user.

read -p "Enter Username: " username

exist = $(grep -i "^$username" /etc/passwd)

if [ -z "$exist"  ]; then
	echo "Creating User $username"
	useradd -s /bin/bash "$username"
else
	echo "User $username already exist"
fi
