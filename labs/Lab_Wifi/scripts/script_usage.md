# Network Bandwidth Testing Scripts

This folder contains Python scripts designed to automate and simplify network bandwidth testing using the `iperf` tool. You can use a combined interactive script or dedicated scripts depending on your setup.

## Prerequisites

- **iperf**: You must have `iperf` (version 2) installed on both machines.
- **Python**: Python 3 must be installed to run these scripts.

## The Scripts Explained

- **`script.py` (All-in-One)**: This is a generic, interactive script. When you run it, it will ask you if you want to operate in "client" or "server" mode. It is perfect if you only want to keep one file on your system.
- **`server.py` (Dedicated Server)**: This script is stripped down to handle only the server-side listening capabilities. It asks for the protocol (TCP or UDP) and then puts the machine in listening mode, waiting for incoming traffic.
- **`client.py` (Dedicated Client)**: This script contains all the logic for the active tests. It asks for the server IP, protocol, and testing mode (standard or reverse). It automatically runs 10 sequential tests, saves the full terminal output to a text log file, and calculates the final statistics (Average, Minimum, Maximum, and Standard Deviation).

## How to Use

### Step 1: Start the Server

You must always start the server first on the machine that will act as the listener.

- Open your terminal and run `python server.py` (or run `script.py` and type "server").
- Choose whether to use TCP or UDP.
- Keep the terminal open and running.

### Step 2: Start the Client

On your second machine, you will run the client to send the traffic and measure the bandwidth.

- Open your terminal and run `python client.py` (or run `script.py` and type "client").
- Enter the IP address of the server machine.
- Select your protocol (TCP or UDP) and mode (standard or reverse).
- The script will automatically run 10 tests. Wait for it to finish to view the statistical results and find your generated log file.