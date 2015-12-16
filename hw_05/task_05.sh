#!/bin/bash

while [[ true ]]; do
  # date prints the current date and time to standard output
  date
  # suspend executing for 1 hr, measured in seconds
  sleep 1h
done > remote_05.dat
