#!/bin/bash

# Check whether input is a file or directory
read -p "Enter a filename or directory: " FILE
if [ -f "$FILE" ]
then
  echo "$FILE is a regular file."
elif [ -d "$FILE" ]
then
  echo "$FILE is a directory."
else
  echo "$FILE is something other than a directory or regular file."
fi
