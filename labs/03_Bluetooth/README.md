# Bluetooth Lab: MAC Address Anonymization & Linkability Analysis

Questo progetto documenta l'analisi della privacy in Bluetooth Low Energy (BLE), focalizzandosi sulla rotazione degli indirizzi MAC (RPA) e sulla vulnerabilità di *linkability* tramite fingerprinting del payload.

---

## 👥 Authors
* **Emanuele Tocci** (s363290) - [s363290@studenti.polito.it](mailto:s363290@studenti.polito.it)
* **Marco Ciucci** (s358656) - [s358656@studenti.polito.it](mailto:s358656@studenti.polito.it)

---

## 🛠 Setup
* **Alice's PC**: CachyOS (Kernel: 7.0.8-1-cachyos-bore)
* **Alice's Device**: Bose QuietComfort 45 (QC-45) Bluetooth headphones
* **Trudy's PC**: ParrotOS 7.2 (Live USB, Kernel: 6.19.13-parrot7-amd64)

---

## ⏱ Timeline
Alice ha collegato e scollegato manualmente il dispositivo dal PC per 7 volte durante la sessione di cattura. Ogni ciclo di connessione/accensione ha forzato le cuffie a iniziare una nuova fase di advertising, causando la rotazione dell'RPA. Trudy, agendo come osservatore passivo, ha monitorato il traffico sniffing BLE e ha tracciato con successo tutte le 7 rotazioni utilizzando il nome del dispositivo come fingerprint statico.

---

## 🔍 Traces

### Trudy's Observed RPA Addresses
`(bthci_evt.bd_addr == 5f:5c:0f:06:8a:a3) || (bthci_evt.bd_addr == 41:ad:22:28:d7:dd) || (bthci_evt.bd_addr == 6b:6d:c1:09:07:89) || (bthci_evt.bd_addr == 7f:fa:1c:29:08:09) || (bthci_evt.bd_addr == 4c:3d:66:fb:b3:2d) || (bthci_evt.bd_addr == 53:7c:ae:93:48:e2) || (bthci_evt.bd_addr == 46:76:f6:33:0a:e2)`

### Alice's Device Public Address
`(bthci_evt.bd_addr == ac:bf:71:81:b2:22)`

---

## 💡 Useful Wireshark Filters
Questi filtri possono essere utilizzati per isolare il traffico target all'interno dei file `.pcapng`:

* **Raw Payload Filter**: `frame[29:12] == 0b:09:4c:45:2d:54:68:75:6e:64:65:72`
* **Device Name Filter**: `btcommon.eir_ad.entry.device_name == "LE-Thunder"`
* **Manufacturer Data Filter**: `btcommon.eir_ad.entry.data == 51:10:ac:83:6e:59:e5:46:0b:59:13`