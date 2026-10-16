Here is the analysis of the network logs based on your specific questions. The results you uploaded provide a classic view of how UDP behaves over a wireless connection using `iperf`.

### 1. Why are the results different? (Across multiple runs)
Even though the tests were run back-to-back, the results (like Jitter) vary slightly between iterations. This happens because **Wi-Fi is a shared, unguided medium**. 
* The transmission is subject to micro-interferences from other devices, physical obstacles, or environmental noise.
* The Wi-Fi MAC layer uses a protocol called CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance), meaning the sender must wait for the channel to be clear before transmitting. These tiny wait times introduce slight variations in how quickly packets are dispatched and arrive.
* [cite_start]Since the UDP bandwidth is capped at the default ~1 Mbps [cite: 26][cite_start], the throughput remains virtually identical, but the micro-timing (Jitter) reflects the varying wireless conditions[cite: 1, 2, 3, 4, 5].

### 2. Why did the goodput change during the 10s of the experiment?
[cite_start]If you look at the 1-second intervals in the logs, the bandwidth fluctuates slightly (e.g., between 1.05 Mbits/sec and 1.06 Mbits/sec)[cite: 26, 27, 28, 29]. 
* **Operating System Scheduling:** The OS handles network packet dispatching in discrete batches. Sometimes a few datagrams are delayed by a fraction of a millisecond and fall into the next 1-second reporting window.
* **Wi-Fi Frame Aggregation:** The wireless adapter might group multiple packets together before transmitting them over the air. This means data doesn't flow in a perfectly continuous stream, but rather in rapid bursts, causing minor variations in the second-by-second calculation.

### 3. Why are the receiver and the sender measurements different? Which is the correct estimation?
The sender and receiver report different metrics because they measure the traffic from two completely different vantage points:
* [cite_start]**The Sender** measures what is pushed from the application (iperf) into the local operating system's network buffer[cite: 26, 27]. It assumes everything sent will reach the destination.
* [cite_start]**The Receiver** measures what actually arrives after surviving the physical network, routing, and Wi-Fi interference[cite: 1, 2]. 


**The Receiver is the correct measurement** for evaluating network performance and goodput. [cite_start]What the sender pushes into the void is irrelevant if the network drops the packets; the receiver's log tells you the true capacity and health of the link (including Jitter and Lost Datagrams)[cite: 1, 2].

### 4. What changes if we invert the sender and the receiver role?
If you invert the roles (making the `10.21.224.90` machine the server and `10.21.224.97` the client), you test the connection in the **opposite direction**. 
* **Asymmetric Links:** Wi-Fi connections are almost never perfectly symmetrical. A laptop or smartphone often has less transmission power and smaller antennas than a dedicated router or access point. 
* **Interference:** The physical environment at the sender's location might have different interference patterns than the receiver's location.
* Inverting the roles allows you to verify if the "Uplink" performs as well as the "Downlink".

### 5. How to properly choose the data generation rate with the `-b` parameter?
[cite_start]By default, an `iperf` UDP test only generates 1 Mbps of traffic[cite: 26]. To properly test the actual limits of your Wi-Fi network, you must force the sender to push more data than the network can handle.
* **Step-up Method:** Start with a baseline you know the network should handle, e.g., `-b 50M` (50 Mbps). If the receiver reports 0% packet loss, the network handled it perfectly.
* **Saturating the Link:** Keep increasing the value (e.g., `-b 100M`, `-b 300M`, `-b 1000M`) and run the test again. 
* **Finding the Limit:** The correct channel capacity is identified the moment the **receiver** starts reporting a Packet Loss greater than 0%. That exact point represents the bottleneck where the router or access point drops packets because its buffers are full.