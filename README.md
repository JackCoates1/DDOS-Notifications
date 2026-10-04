
<div align="center">

# DDOS-Notifications
**Packet-rate monitoring with Discord alerts**


</div>

---

## Overview

This script monitors network traffic and sends a Discord alert when traffic exceeds a threshold. I built it because I wanted an alternative to a large monitoring stack.

---

## Project Structure

```
DDOS-Notifications/
├── dump.sh             # Collects network/packet data
├── webhook.py          # Sends a Discord alert
├── config.yaml.example # Copy this and fill in your values
└── README.md
```

---

## Setup

**1. Install dependencies**

```bash
sudo apt update && sudo apt install python3-pip screen tcpdump -y
pip3 install discord-webhook pyyaml
```

**2. Clone the repo**

```bash
git clone https://github.com/JackCoates1/DDOS-Notifications.git
cd DDOS-Notifications
```

**3. Configure**

```bash
cp config.yaml.example config.yaml
nano config.yaml
```

Set your Discord webhook URL, server IP, and location.

**4. Check your network interface**

```bash
ip addr
```

Update the `interface` variable in `dump.sh` if needed. Common values are `eth0`, `ens3` and `venet0`.

**5. Run in background with screen**

```bash
chmod +x dump.sh
screen -S ddos-monitor
sudo ./dump.sh
# Ctrl+A, D to detach. Use screen -r ddos-monitor to re-attach.
```

---

## How It Works

`dump.sh` monitors packet rate and checks it against a threshold. When the threshold is exceeded, it calls `webhook.py` to send a Discord alert.

![Discord Webhook Alert](discord_webhook.png)

---

## Roadmap

- [ ] Telegram + email support
- [ ] Rolling average detection to reduce false positives
- [ ] Optional web dashboard

---

MIT License
