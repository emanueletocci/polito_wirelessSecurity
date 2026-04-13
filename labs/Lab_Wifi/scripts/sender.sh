#!/bin/bash

# Request for the IP address
read -r -p "Enter the server IP address: " SERVER_IP

# Request for the protocol
read -r -p "Do you want to use TCP or UDP? (Type tcp or udp): " PROTOCOL

# Flag configuration based on the choice
if [ "$PROTOCOL" = "udp" ]; then
    FLAG_PROTO="-u"
    echo "You chose UDP. The -u flag will be added."
else
    FLAG_PROTO=""
    echo "You chose TCP."
fi

# Definition of the log file name based on inputs
LOG_FILE="log_${PROTOCOL}_${SERVER_IP}.txt"
echo "Starting the tests. The results will be saved and appended in: $LOG_FILE"
echo "---------------------------------------------------"

# Loop for 10 measurements
for i in {1..10}; do
    echo "--- Test $i of 10 ---" | tee -a "$LOG_FILE"
    iperf -c "$SERVER_IP" -i 1 $FLAG_PROTO | tee -a "$LOG_FILE"
    sleep 1
done

echo "All 10 measurements have been successfully completed!"