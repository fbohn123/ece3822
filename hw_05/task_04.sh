#!bin/bash
# file: task_04.sh

# initialize hrs
hrs=0
# check script at least 3 times in 8 hrs
while [[ hrs -le 8 ]]; do
  # print out the current time of the test and the total run time.
  now=$(date)
  run_time=$(ps -p 4818 -o etime=)
  echo "[ "$now" ] ece_3822.sh, total run time: "$run_time
  sleep 4h
  ((hrs+=4))
done
