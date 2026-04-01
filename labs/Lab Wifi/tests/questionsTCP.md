Ecco l'analisi dei due file di log generati tramite `iperf` per il test TCP su rete Wi-Fi. [cite_start]Il file del destinatario (server `10.21.224.97` gestito da Antonio [cite: 1][cite_start]) e il file del mittente (client `10.21.224.90` gestito da Davide [cite: 16]) mostrano il comportamento tipico di una connessione di questo tipo.

Di seguito le risposte alle tue domande:

### 1) Why are the results different? (Perché i risultati variano tra le diverse esecuzioni?)
Le prestazioni variano tra i diversi test da 10 secondi a causa della natura instabile del mezzo trasmissivo Wi-Fi e del protocollo TCP:
* **Mezzo condiviso e interferenze:** Il Wi-Fi utilizza onde radio, un mezzo condiviso vulnerabile a interferenze ambientali (es. altri dispositivi elettronici, reti vicine), ostacoli fisici e degradazione del segnale (fading).
* **Protocollo MAC (CSMA/CA):** Il Wi-Fi utilizza il meccanismo CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance), che impone ai dispositivi di ascoltare il canale e attendere che sia libero prima di trasmettere. Se il canale è trafficato o si verificano collisioni, vengono introdotti ritardi variabili.
* **Adattamento del TCP:** Il protocollo TCP percepisce questi ritardi e le eventuali perdite di pacchetti tipiche del Wi-Fi come "congestione", modificando di conseguenza la sua velocità di trasmissione in modo dinamico.

### 2) Why did the goodput change during the 10s of the experiment? (Perché il goodput cambia durante i 10 secondi del singolo esperimento?)
All'interno di una singola sessione da 10 secondi, la larghezza di banda subisce forti variazioni (spesso partendo da valori molto bassi per poi crescere). Questo è causato dal meccanismo di **TCP Slow Start** e dal controllo della congestione del TCP. 
Il protocollo TCP non invia immediatamente i dati alla massima velocità supportata dalla rete. Al contrario, "sonda" la capacità del canale partendo con una finestra di trasmissione piccola, per poi aumentarla esponenzialmente finché non rileva la perdita di un pacchetto (spesso dovuta a interferenze Wi-Fi o buffer pieni). Quando rileva una perdita, dimezza o riduce drasticamente la velocità, per poi ricominciare a salire.
Questo è evidentissimo nel test sulla porta `35248`:
* [cite_start]Nel primo secondo (0.0 - 1.0 sec), il mittente ha inviato solo 512 KBytes a 4.19 Mbits/sec[cite: 27].
* [cite_start]Nello stesso lasso di tempo, il ricevitore ha registrato solo 408 KBytes a 3.34 Mbits/sec[cite: 11].
* [cite_start]Dal terzo secondo in poi, la connessione si stabilizza sopra i 260 Mbits/sec nel lato mittente[cite: 28].

### 3) Why are the receiver and the sender measurements different? Which is the correct goodput estimation? (Perché le misurazioni di mittente e destinatario sono diverse? Qual è la stima corretta?)
Confrontando i due log sulla stessa porta, notiamo leggere differenze sui tempi totali e sulla banda calcolata. [cite_start]Ad esempio, per la porta `45962`, il mittente riporta un trasferimento di 236 MBytes in 10.1048 secondi a 196 Mbits/sec [cite: 17][cite_start], mentre il ricevitore riporta gli stessi 236 MBytes ricevuti in 9.9812 secondi a 198 Mbits/sec[cite: 2].

* **Perché sono diverse:** Il mittente (client) misura la velocità con cui i dati vengono *scritti* nel buffer del sistema operativo per essere inviati alla scheda di rete. Il destinatario (server) misura la velocità con cui i dati vengono effettivamente *ricevuti e letti* dal livello applicativo. Eventuali re-trasmissioni TCP per pacchetti persi nell'aria, latenze di rete e il tempo in cui i dati risiedono nei buffer di trasmissione/ricezione creano questa discrepanza temporale.
* **Qual è corretta:** La stima corretta del **goodput** (ovvero la quantità di dati utili effettivamente fruibili dall'applicazione) è quella del **destinatario (receiver)**. Questa misurazione attesta che i dati hanno attraversato con successo l'intero percorso di rete e sono stati ricomposti correttamente a destinazione.

### 4) What changes if we invert the sender and the receiver role? (Cosa cambia se invertiamo il ruolo di mittente e destinatario?)
Invertendo i ruoli (facendo trasmettere "antonio" verso "davide"), le prestazioni potrebbero essere notevolmente diverse. Le connessioni Wi-Fi sono spesso **asimmetriche** per i seguenti motivi:
* [cite_start]**Differenze Hardware:** I dispositivi (il PC "MSI" di Davide e la macchina "Kubuntu" di Antonio [cite: 1, 16]) potrebbero avere antenne Wi-Fi diverse (es. uno ha un'antenna 2x2 MIMO e l'altro una 3x3 MIMO) o capacità di potenza di trasmissione differenti. Un dispositivo potrebbe essere in grado di inviare il segnale molto più forte di quanto riesca a riceverlo.
* **Interferenze Locali (Hidden Node):** Le interferenze elettromagnetiche sono localizzate. Potrebbe esserci una fonte di forte rumore (un altro router, un microonde, muri spessi) vicina al computer di Antonio ma non a quello di Davide, rendendo la ricezione in una direzione molto più frammentata rispetto all'altra.
* **Elaborazione OS:** I due diversi sistemi operativi e i rispettivi stack di rete TCP/IP gestiscono il buffering e gli offload hardware in modi differenti, impattando in modo asimmetrico le velocità massime di invio e ricezione.
