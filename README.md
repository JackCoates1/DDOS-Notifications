<p align="center">
  <img src="https://raw.githubusercontent.com/shexty/DDOS-Notifications/main/Banner.svg" alt="DDOS-Notifications Banner" width="100%">
</p>

<div align="center">

# 🚨 DDOS-Notifications  
**Lightweight & Fast DDoS Alerting via Webhooks**

![GitHub Repo stars](https://img.shields.io/github/stars/shexty/DDOS-Notifications?style=flat&color=yellow) 
![GitHub forks](https://img.shields.io/github/forks/shexty/DDOS-Notifications?style=flat&color=blue) 
![GitHub issues](https://img.shields.io/github/issues/shexty/DDOS-Notifications?style=flat&color=orange)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Made with Python](https://img.shields.io/badge/made%20with-Python-blue?logo=python)

</div>

---

## 🧠 Overview

**DDOS-Notifications** is a simple, efficient tool designed to **detect suspicious traffic spikes** and **send real-time alerts** via webhooks (e.g., Discord, Slack, MS Teams).

✅ **Lightweight** – Bash + Python, no heavy frameworks  
✅ **Fast** – Detect & notify within seconds  
✅ **Customizable** – Set your own thresholds and webhook targets  
✅ **Extensible** – Integrate with any monitoring setup

---

## 📂 Project Structure

DDOS-Notifications/
├── dump.sh # Bash script to collect network or log data
├── webhook.py # Python script to evaluate and send alerts
├── setup.txt # Setup & configuration notes
└── README.md # This file

yaml
Copy code

---

## 🧰 Requirements

- Python 3.x  
- [`requests`](https://pypi.org/project/requests/) library  
- A shell environment (Linux / macOS)  
- A valid **webhook URL** (Discord, Slack, etc.)  
- Network log or metric access (e.g., netstat, iptables, interface counters)

---

## 🛠️ Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/shexty/DDOS-Notifications.git
cd DDOS-Notifications

# 2️⃣ Install dependencies
pip install requests

# 3️⃣ Make scripts executable (if needed)
chmod +x dump.sh
⚙️ Configuration
You can configure the tool using environment variables or by editing the scripts directly.

Example: Environment Variables
bash
Copy code
export WEBHOOK_URL="https://your-discord-or-slack-webhook-url"
export PACKET_THRESHOLD=100000
Inside webhook.py:

python
Copy code
import os

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
THRESHOLD = int(os.getenv("PACKET_THRESHOLD", "50000"))
🚀 Usage
Manual Run
bash
Copy code
./dump.sh > stats.log
python webhook.py stats.log
Continuous Monitoring (via Cron)
cron
Copy code
* * * * * /path/to/DDOS-Notifications/dump.sh | python /path/to/DDOS-Notifications/webhook.py
Whenever traffic exceeds your threshold, an alert is automatically sent to your webhook channel.
Here’s an example Discord alert message:

⚠️ High Traffic Detected
125,340 packets in the last minute — possible DDoS attack.

🧭 How It Works
lua
Copy code
+-------------+       +----------------+       +----------------------+
|  dump.sh    | --->  |  webhook.py    | --->  |  Webhook (Discord)   |
| (collects   |       | (checks &      |       |  Slack, Teams, etc.) |
|  metrics)   |       |  sends alerts) |       +----------------------+
+-------------+       +----------------+
dump.sh collects traffic stats from logs, firewalls, or interfaces

webhook.py parses the data and compares it against thresholds

If an anomaly is detected → an alert is sent immediately

🧪 Example Threshold Logic
python
Copy code
if packet_count > THRESHOLD:
    payload = {
        "content": f"⚠️ High traffic detected: {packet_count} packets in the last minute."
    }
    requests.post(WEBHOOK_URL, json=payload)
🌟 Roadmap
 Support for additional notification channels (SMS, Email, Telegram)

 YAML / JSON configuration file support

 Rolling average detection (to reduce false positives)

 Dashboard or CLI output mode

 Docker container version

🤝 Contributing
Contributions are welcome! Here’s how:

Fork the repository

Create a new branch (feature/my-feature)

Commit your changes

Push and open a Pull Request 🚀

📜 License
This project is licensed under the MIT License.

sql
Copy code
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
<div align="center">
🔥 Built with Bash, Python, and 💡 simplicity in mind.

</div> ```
