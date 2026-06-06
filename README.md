#  NetViz: Real-Time Network Traffic Analyzer

 Overview
NetViz is a custom-built, full-stack network packet sniffing and visualization tool. Designed in a Kali Linux environment, it captures live network traffic at the data link layer and streams it asynchronously to a web-based dashboard. 

This project demonstrates core cybersecurity competencies, including low-level network protocol analysis, packet interception, and real-time security telemetry visualization.

 Key Features
*   **Live Packet Sniffing:** Utilizes Scapy to intercept and analyze live TCP/IP network traffic directly from the network interface card (NIC).
*   **Asynchronous Telemetry:** Implements WebSockets (Socket.IO) to push packet data from the backend to the frontend with zero latency.
*   **Network Reconnaissance Visualization:** Extracts and dynamically displays Source IPs, Destination IPs, and payload sizes in a terminal-themed UI, mimicking Security Operations Center (SOC) alert triage.
*   **Local Subnet Monitoring:** Capable of mapping localized traffic and communications across WSL/Virtual setups and local Wi-Fi networks.

 Technologies & Frameworks
*   **Backend:** Python 3, Flask
*   **Networking & Security:** Scapy (Packet manipulation/sniffing), TCP/IP mapping
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Real-Time Comms:** Flask-SocketIO (WebSockets)
*   **Environment:** Kali Linux / Windows Subsystem for Linux (WSL)

 Installation & Usage

 Prerequisites
*   Linux environment (Kali Linux recommended)
*   Root privileges (required for packet sniffing)
*   Python 3 installed

 Setup Instructions
1. **Clone the repository:**
```bash
   git clone [https://github.com/YOUR_USERNAME/NetViz.git](https://github.com/YOUR_USERNAME/NetViz.git)
   cd NetViz'''
