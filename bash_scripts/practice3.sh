#!/bin/bash

# Check if file exists, and if so, whether it is writeable
FILE="/etc/shadow"

if [ -e "$FILE" ]
then
  echo "Shadow passwords are enabled."
  if [ -w "$FILE" ]
  then
    echo "You have permissions to edit ${FILE}."
  else
    echo "You do NOT have permissions to edit ${FILE}."
  fi
else
  echo "No such file ${FILE} exists"
fi
