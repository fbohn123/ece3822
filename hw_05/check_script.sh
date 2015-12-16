#!bin/bash
# process id
PID=4818
# check script
now=$(date)
run_time=$(ps -p $PID -o etime=)
echo "["$now"] ece_3822 run time "$run_time
