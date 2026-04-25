# Network Performance Lab - Automation Script

This directory contains a Bash script designed to automate the data collection process for the WiFi performance tests as outlined in the lab requirements.

## Deployment Strategy

To correctly measure the Goodput, the experiment requires two distinct roles:

### 1. The Server (Receiver)

The Server machine must be set up first to listen for incoming data.
**Note:** Do NOT run the automation script on this machine. Instead, use the following manual commands in the terminal depending on the protocol you are testing:

**For TCP measurements:**

```bash
iperf -s -i 1
```

**For UDP measurements:**

```bash
iperf -s -u -i 1
```

*This command puts iperf in server mode (`-s`) and provides reports every 1 second (`-i 1`). The `-u` flag is strictly required to instruct the server to listen for UDP traffic instead of TCP.*

### 2. The Client (Sender)

The automation script provided in this folder (`lab_iperf.sh`) must be executed exclusively on the **Client** machine.

**How to run:**

1. Open your terminal in the `scripts` folder.
2. Make the script executable:

   ```bash
   chmod +x lab_iperf.sh
   ```

3. Run the script:

   ```bash
   ./lab_iperf.sh
   ```

## Script Functionality

The script automates the requirement of repeating the test 10 times to extract consistent statistical data (min, max, avg, and standard deviation). It will prompt you for the Server's IP address and the desired protocol (TCP or UDP).

All results will be saved into a `.txt` log file for further analysis in your report.
