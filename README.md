# WD2DCS Labs: GNSS, WiFi, and Bluetooth Performance

![](/resources/logo_polito.jpg)

This repository contains all the materials, scripts, datasets, and LaTeX reports for the laboratory experiments conducted as part of the **Wireless and Device-to-Device Communication Security (WD2DCS)** course within the **Cybersecurity Engineering** master's degree program at **Politecnico di Torino**.

## Overview

This repository is divided into three main sections, each dedicated to a specific laboratory experience:

1. **GNSS Lab**: Focuses on processing raw GNSS measurements collected from Android devices using MATLAB. 
2. **WiFi Performance Lab**: Focuses on the analysis, performance evaluation, and security assessment of WiFi networks.
3. **Bluetooth Lab**: Focuses on the analysis of Bluetooth Low Energy (BLE) privacy features, specifically MAC address randomization (RPA) and linkability attacks via payload fingerprinting.

## Note

The detailed lab reports, including all experimental results, theoretical background, and data analysis, can be found in the respective `Report/` directories of each lab.

## Lab Objectives & Requirements

### GNSS Lab Objectives
* Process raw GNSS measurements from Android devices.
* Analyze pseudoranges, C/N₀, and WLS positioning.
* Conduct spoofing experiments and evaluate detection strategies.

### WiFi Performance Lab Objectives
* Capture and analyze WiFi network traffic.
* Evaluate network performance metrics under varying configurations.
* Analyze security implications within wireless communication environments.

### Bluetooth Lab Objectives
* Analyze Bluetooth protocol stack at HCI level.
* Observe pairing procedures and privacy features (RPA).
* Perform linkability attacks using Wireshark to track devices across address changes.

### Requirements
* `MATLAB R2020a` or later for GNSS Lab.
* GNSSLogger App on Android.
* Packet analysis software (e.g., **Wireshark**) for WiFi and Bluetooth captures.
* Linux-based environment (e.g., ParrotOS, Kali) with Bluetooth interface for sniffing.

## Authors

| Name | GitHub |
| :--- | :--- |
| **Antonio Amendolara** | [GitHub Profile](https://github.com/AntonioAmendolara) | 
| **Davide Marin** | [GitHub Profile](https://github.com/MarinDavide) |
| **Alberto Mercurelli** | [GitHub Profile](#) |
| **Emanuele Tocci** | [GitHub Profile](https://github.com/emanueletocci) |
| **Marco Ciucci** | [GitHub Profile](#) |