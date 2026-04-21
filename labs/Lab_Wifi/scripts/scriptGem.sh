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

# Request for the method
read -r -p "Do you want to use standard or reverse mode? (Type standard or reverse): " METHOD

# Flag configuration based on the choice
if [ "$METHOD" = "reverse" ]; then
    FLAG_METHOD="-R"
    echo "You chose reverse mode. The -R flag will be added."
else
    FLAG_METHOD=""
    echo "You chose standard mode."
fi

# Definition of the log files
LOG_FILE="log_${PROTOCOL}_${SERVER_IP}.txt"
TMP_DAT="temp_gput.dat"
# Pulisco il file temporaneo se esiste da test precedenti [cite: 794]
rm -f "$TMP_DAT" 

echo "Starting the tests. The results will be saved and appended in: $LOG_FILE"
echo "---------------------------------------------------"

# Loop for 10 measurements
for i in {1..10}; do
    echo "--- Test $i of 10 ---" | tee -a "$LOG_FILE"
    
    # Eseguo iperf, salvo nel log e in parallelo estraggo il valore del Throughput
    # Nota: corretto -R con $FLAG_METHOD
    iperf -c "$SERVER_IP" -i 1 $FLAG_PROTO $FLAG_METHOD | tee -a "$LOG_FILE" | \
    grep -E "0\.0-10\." | awk '{print $8}' >> "$TMP_DAT"
    
    sleep 1
done

echo "---------------------------------------------------"
echo "All 10 measurements have been successfully completed!"
echo "--- STATISTICAL RESULTS (Mbits/sec) ---"

# Calcolo di Max, Min, Media e Deviazione Standard usando awk 
cat "$TMP_DAT" | awk '
BEGIN {max=0; min=99999999}
{
    x += $1; 
    y += $1^2; 
    if ($1 < min) {min = $1}; 
    if ($1 > max) {max = $1}
}
END {
    print "Average = " x/NR
    print "Min     = " min
    print "Max     = " max
    print "Std Dev = " sqrt(y/NR - (x/NR)^2)
}'

# Pulizia del file temporaneo
rm -f "$TMP_DAT"