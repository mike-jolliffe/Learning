#!/bin/bash

# Show exit status of zero
echo "This script will exit with an exit status of 0"
echo $?

# Read file/dir input, exit with different value depending on type
FILE=$1
if [ -f "$FILE" ]
then
  echo "$FILE is a regular file."
  exit 0
elif [ -d "$FILE"]
then
  echo "$FILE is a directory."
  exit 1
else
  echo "$FILE is not a file or directory."
  exit 2
fi
