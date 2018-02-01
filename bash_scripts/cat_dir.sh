#!/bin/bash

# Print directory if exists
cat /etc/shadow
if [ "$?" -eq "0" ]
then
  echo "Command succeeded"
  exit 0
else
  echo "Command failed"
  exit 1
fi
