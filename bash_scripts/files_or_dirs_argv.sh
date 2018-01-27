#!/bin/bash

# Check for one or more input args
for FILE in $@
do
  echo
  if [ -f "$FILE" ]
  then
    echo "$FILE is a regular file."
  elif [ -d "$FILE" ]
  then
    echo "$FILE is a directory."
  else
    echo "$FILE is something other than a directory or regular file."
  fi

  ls -l $FILE
done
