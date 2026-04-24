#!/bin/bash

# Controllo che sia stato passato un file come argomento
if [ -z "$1" ]; then
    echo "Uso: $0 <nome_del_file_log>"
    exit 1
fi

LOG_FILE="$1"

# Controllo che il file esista
if [ ! -f "$LOG_FILE" ]; then
    echo "Errore: Il file '$LOG_FILE' non esiste."
    exit 1
fi

echo "Elaborazione del file: $LOG_FILE"
echo "---------------------------------------------------"

# Cerchiamo le righe di riassunto (che contengono "0.0-10." o "0.00-10.")
# e passiamo tutto ad awk per estrarre il valore e fare la statistica.
grep -E "0\.0-10\.|0\.00-10\." "$LOG_FILE" | awk '
BEGIN {
    count = 0;
    sum = 0;
    sum_sq = 0;
    min = 99999999;
    max = 0;
}
{
    val = 0;
    # Cerca in tutte le colonne della riga la parola "bits/sec" (es. Mbits/sec)
    for(i=1; i<=NF; i++) {
        if ($i ~ /bits\/sec/) {
            val = $(i-1); # Prendi il numero prima dell unità di misura
            break;
        }
    }

    if (val > 0) {
        count++;
        sum += val;
        sum_sq += val^2;
        if (val < min) min = val;
        if (val > max) max = val;
        print "Test " count ": " val " Mbits/sec"
    }
}
END {
    if (count > 0) {
        avg = sum / count;
        variance = (sum_sq / count) - (avg^2);
        std_dev = (variance > 0) ? sqrt(variance) : 0;
        
        print "---------------------------------------------------"
        print "RISULTATI STATISTICI SU " count " MISURAZIONI:"
        printf "Average = %.2f Mbits/sec\n", avg
        printf "Min     = %.2f Mbits/sec\n", min
        printf "Max     = %.2f Mbits/sec\n", max
        printf "Std Dev = %.2f Mbits/sec\n", std_dev
    } else {
        print "Attenzione: Nessun dato valido trovato nel log."
    }
}'