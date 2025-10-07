<p align="center">
  <img src="Banner.svg" alt="DDOS-Notifications Banner" width="100%">
</p>

<div align="center">

# 🚨 DDOS-Notifications  
**Real-Time DDoS Detection & Notifications**

![Stars](https://img.shields.io/github/stars/shexty/DDOS-Notifications?style=flat&color=yellow)
![Forks](https://img.shields.io/github/forks/shexty/DDOS-Notifications?style=flat&color=blue)
![Issues](https://img.shields.io/github/issues/shexty/DDOS-Notifications?style=flat&color=orange)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/made%20with-Python-blue?logo=python)

</div>

---

## 🧠 Overview

**DDOS-Notifications** is a lightweight tool for **real-time detection of suspicious network spikes** and **instant alerting** through webhooks such as Discord, Slack, or Microsoft Teams.  
Perfect for sysadmins and security engineers who want quick alerts without complex monitoring setups.

---

## 📁 Project Structure

```
DDOS-Notifications/
├── dump.sh         # Bash script to collect network/log data
├── webhook.py      # Python script to check & send alerts
├── setup.txt       # Optional setup notes
└── README.md
```

---

## ⚙️ Configuration
![Discord Webhook Alert](discord_webhook.png)

*Screenshot: Discord Webhook Alert*

Set your **webhook URL** and optional **threshold** using environment variables:

```bash
export WEBHOOK_URL="https://your-webhook-url"
export PACKET_THRESHOLD=100000
```

Inside `webhook.py`:

```python
import os

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
THRESHOLD = int(os.getenv("PACKET_THRESHOLD", "50000"))
```

---

## 🚀 Usage

**Manual Run**

```
./dump.sh > stats.log
python webhook.py stats.log
```

**Continuous Monitoring (Cron Example)**

```
* * * * * /path/to/dump.sh | python /path/to/webhook.py
```

When traffic exceeds your threshold, you’ll receive an instant alert via your webhook channel.

---

## 🧭 How It Works

```
+-------------+       +----------------+       +----------------------+
|  dump.sh    | --->  |  webhook.py    | --->  |  Webhook (Discord)   |
| (collects   |       | (checks &      |       |  Slack, Teams, etc.) |
|  metrics)   |       |  sends alerts) |       +----------------------+
+-------------+       +----------------+
```

---

## 🌟 Roadmap

- [ ] YAML/JSON config support  
- [ ] Multiple notification channels (SMS, Telegram, Email)  
- [ ] Smarter detection (rolling averages / anomaly detection)  
- [ ] Optional dashboard view

---

## 🤝 Contributing

Contributions are welcome!

1. **Fork** the repository  
2. Create a new branch (`feature/your-feature`)  
3. Commit your changes  
4. Open a **Pull Request**

Ideas for contributions:
- Add new notification types
- Improve threshold detection logic
- Add tests or CI pipelines

---

## 📜 License

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

<p align="center">
  🛡 Built for security-minded admins • Fast • Simple • Effective
</p>

