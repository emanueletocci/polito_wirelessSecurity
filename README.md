<p align="center">
  <img src="resources/logo_polito.jpg" alt="Politecnico di Torino"/>
</p>

<h1 align="center">Wireless & Device-to-Device Communication Security</h1>
<p align="center">
  <strong>M.Sc. in Cybersecurity Engineering — Politecnico di Torino</strong><br>
  <em>Academic Year 2025/2026</em>
</p>

<p align="center">
  <a href="https://www.polito.it/"><img src="https://img.shields.io/badge/Institution-Politecnico%20di%20Torino-b5121b.svg" alt="PoliTO"></a>
  <a href="#"><img src="https://img.shields.io/badge/Course-WD2DCS-003366.svg" alt="Course"></a>
  <a href="#"><img src="https://img.shields.io/badge/Degree-M.Sc.%20Cybersecurity%20Engineering-blue.svg" alt="Degree"></a>
  <a href="#"><img src="https://img.shields.io/badge/Reports-PDF%20Available-brightgreen.svg" alt="Reports"></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Completed-success.svg" alt="Status"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/MATLAB-R2025b-e16727?logo=mathworks&logoColor=white" alt="MATLAB">
  <img src="https://img.shields.io/badge/Wireshark-Packet%20Analysis-1679A7?logo=wireshark&logoColor=white" alt="Wireshark">
  <img src="https://img.shields.io/badge/Protocol-Wi--Fi%206%20%7C%20BLE%20%7C%20GNSS-blueviolet" alt="Protocols">
</p>

---

## 📌 Executive Summary

This repository contains the experimental methodology, custom automation scripts, packet traces, raw datasets, and comprehensive technical reports developed for the **Wireless and Device-to-Device Communication Security (WD2DCS)** course at **Politecnico di Torino**.

The research investigates the physical and link-layer security, performance limits, and privacy guarantees across three pervasive wireless communication standards:
1. **Global Navigation Satellite Systems (GNSS)**: Susceptibility of consumer smartphone receivers to cellular RF interference and counterfeit signal injection (coordinate & clock delay spoofing).
2. **Wi-Fi Networks (IEEE 802.11ax / Wi-Fi 6)**: Goodput vs. throughput evaluation, half-duplex shared-medium penalties, and empirical transport layer dynamics (TCP/UDP) across wired, wireless, and mixed topologies.
3. **Bluetooth Low Energy (BLE)**: Cryptographic privacy evaluation of Resolvable Private Addresses (RPA) and practical linkability attacks exploiting static advertising payload fingerprints.

---

## 📑 Technical Reports (Quick Access)

The complete, peer-reviewed style laboratory reports detailing mathematical models, experimental testbeds, statistical evaluations, and in-depth discussions are available below:

| Lab Module | Technical Topic | Format | Direct Link |
| :--- | :--- | :---: | :---: |
| **Lab 01** | **GNSS Measurement Analysis, RF Interference & Spoofing Emulation** | PDF | [📄 View Report](labs/01_GNSS/report/WS_GNSS.pdf) |
| **Lab 02** | **Wi-Fi Performance, Bottleneck Identification & Protocol Overheads** | PDF  | [📄 View Report](labs/02_Wifi/report/WS_Wifi_Performance.pdf) |
| **Lab 03** | **BLE MAC Address Randomization & Fingerprint Linkability** | Markdown / Documentation | [📘 View Lab Documentation](labs/03_Bluetooth/README.md) |

---

## 🔬 Research Modules Overview

### [Module 01: GNSS Vulnerability & Spoofing Analysis](labs/01_GNSS/)
* **Testbed**: Samsung Galaxy S25 (Android 16), Google GNSS Logger v2.0.0.2, MATLAB R2025b (Weighted Least Squares PVT solver without inertial filtering).
* **Investigation**:
  * **Baseline Stability**: Empirical Doppler validation demonstrating consistent sub-meter pseudorange derivative tracking ($\Delta \in [-0.90, +0.87] \text{ m/s}$) under nominal sky conditions.
  * **RF Cellular Interference**: An active voice call caused substantial vertical degradation, inducing altitude tracking drops exceeding $-60 \text{ m}$.
  * **Emulated Coordinate Spoofing**: Simulating a trajectory jump to Piazza Castello (`45.076795° N, 7.683674° E`) revealed severe estimator instability, producing horizontal velocity spikes up to $2.36 \text{ m/s}$ and a 38% increase in velocity standard deviation ($\sigma = 0.226 \text{ m/s}$).
  * **Emulated Clock Delay Spoofing**: Injecting an artificial 1 ms delay shifted the receiver clock bias while leaving spatial coordinates unaltered, revealing a key vulnerability for time-critical infrastructure (e.g., 5G synchronization).
* 👉 **Read more**: [Lab 01 Dedicated README](labs/01_GNSS/README.md) • [Full Report (PDF)](labs/01_GNSS/report/WS_GNSS.pdf)

---

### [Module 02: Wi-Fi Performance & Network Bottlenecks](labs/02_Wifi/)
* **Testbed**: Dual Linux hosts (CachyOS / Arch and Kubuntu 24.04), Intel Wi-Fi 6 AX211, Arrow Lake CNVi Wi-Fi, TIM Hub+ Wi-Fi 6 Access Point.
* **Investigation**:
  * **Direct Fast Ethernet Baseline**: Auto-negotiated 100 Mbps bottleneck; TCP sustained $93.82 \text{ Mbps}$ average goodput ($\sigma = 0.06$, matching the 94.9 Mbps theoretical bound at 98.8% efficiency).
  * **Purely Wi-Fi 6 (Two-Hop Shared Medium)**: The mandatory two-hop transmission ($\text{STA}_1 \to \text{AP} \to \text{STA}_2$) over half-duplex airtime halved link efficiency (multiplier $0.5$). Forward goodput achieved $413.80 \text{ Mbps}$ ($91.8\%$ of theoretical bound), while reverse mode exhibited high variance ($\sigma = 118.81$) due to channel contention.
  * **Mixed Mode (Gigabit Ethernet + Wi-Fi 6)**: Eliminating the shared-medium airtime penalty boosted goodput to $798.20 \text{ Mbps}$, bounded by the Wi-Fi client interface capacity.
  * **Automation Suite**: Custom Python automation scripts (`client.py`, `server.py`) executing 10-iteration test campaigns with automated statistical aggregation.
* 👉 **Read more**: [Lab 02 Dedicated README](labs/02_Wifi/README.md) • [Full Report (PDF)](labs/02_Wifi/report/WS_Wifi_Performance.pdf)

---

### [Module 03: BLE MAC Address Randomization & Linkability](labs/03_Bluetooth/)
* **Testbed**: Bose QuietComfort 45 (Alice's device, Public MAC `ac:bf:71:81:b2:22`), CachyOS master host, ParrotOS 7.2 passive sniffer (Trudy).
* **Investigation**:
  * **RPA Evaluation**: Evaluated the BLE Resolvable Private Address (RPA) mechanism across 7 sequential connection and power cycles.
  * **Linkability Attack**: Despite 7 distinct MAC address rotations, Trudy achieved **100% correlation** by tracking static upper-layer payload fields (Complete Local Name `LE-Thunder` and Manufacturer Specific Data) inside unencrypted advertising packets.
  * **Countermeasure Analysis**: Highlights the necessity of payload randomization and synchronized identifier rotation alongside Layer 2 MAC address randomization.
* 👉 **Read more**: [Lab 03 Dedicated README](labs/03_Bluetooth/README.md)

---

## 📂 Repository Structure

```text
polito_wirelessSecurity/
├── README.md                                         # Main Project Overview & Navigation
├── .gitignore                                        # Standardized git ignore rules
├── resources/
│   └── logo_polito.jpg                               # Politecnico di Torino emblem
└── labs/
    ├── 01_GNSS/
    │   ├── README.md                                 # Lab 01 Documentation & Methodology
    │   ├── gps-measurement-tools.../                 # MATLAB PVT & spoofing simulation scripts
    │   ├── images/                                   # Baseline, RF interference & spoofing plots
    │   ├── references/                               # Academic guides & slides
    │   └── report/
    │       └── WS_GNSS.pdf                           # Complete GNSS Technical Report
    │
    ├── 02_Wifi/
    │   ├── README.md                                 # Lab 02 Documentation & Benchmark Results
    │   ├── measurements/                             # Raw logs, captures & Wireshark graphs
    │   ├── references/                               # 802.11 standards & Wireshark cheat sheets
    │   ├── report/
    │   │   └── WS_Wifi_Performance.pdf               # Complete Wi-Fi Technical Report
    │   └── scripts/                                  # Automated Python iperf measurement suite
    │
    └── 03_Bluetooth/
        ├── README.md                                 # Lab 03 Documentation & Linkability Attack
        ├── plots/                                    # Wireshark HCI & sniffer capture plots
        └── setup.txt                                 # Capture parameters & Wireshark filters
```

---

## 👥 Authors & Research Team

This laboratory research was conducted by graduate students in the **M.Sc. in Cybersecurity Engineering** at **Politecnico di Torino**:

| Member | Lab Contributions | GitHub Profile |
| :--- | :--- | :---: |
| **Emanuele Tocci** | GNSS, Wi-Fi Performance, Bluetooth Privacy | [@emanueletocci](https://github.com/emanueletocci) |
| **Davide Marin** | GNSS, Wi-Fi Performance | [@MarinDavide](https://github.com/MarinDavide) |
| **Antonio Amendolara** | GNSS, Wi-Fi Performance | [@AntonioAmendolara](https://github.com/AntonioAmendolara) |
| **Alberto Mercurelli** | GNSS, Wi-Fi Performance | [@AlbertoMercurelli](https://github.com/AlbertoMercurelli) |
| **Marco Ciucci** | Bluetooth Privacy | [@MarcoCiucci](https://github.com/MarcoCiucci) |

---

## 📜 Academic Integrity & License

This repository contains educational and research artifacts produced for the **Wireless and Device-to-Device Communication Security (WD2DCS)** course at **Politecnico di Torino**. All experiments were conducted in controlled laboratory settings for academic research and vulnerability demonstration purposes.
