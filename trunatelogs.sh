#!/bin/bash

LOG_DIRECTORY="/var/log/trial"
files=("$LOG_DIRECTORY"/*)

echo "FILES: ${files[*]}"

for file in "${files[@]}"; do
	echo "Truncating: $file"
	> "$file"
	echo "Trucated: $file"
done
