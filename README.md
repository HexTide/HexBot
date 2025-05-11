
<p align="center">
  <img src="https://github.com/HexTide.png" width="100" alt="Hex Logo"/>
</p>

<h1 align="center">HexBot</h1>
<p align="center"><strong>Orchestrator for the HEX Automation Ecosystem</strong></p>
<p align="center">
Run bots • Manage workflows • CLI integration
</p>
<p align="center">
Created by <a href="https://github.com/HexTide">HexTide</a>
</p>

---

## 🧠 What is HexBot?

HexBot is the orchestrator of the HEX Automation Ecosystem.  
It dynamically loads and runs HEX-compatible bots using the HexRoot framework.

---

## 🚀 How It Works

```bash
python run.py                 # Runs the default bot (configured in config.py)
python hexbot/runner.py bots.sample_bot  # Runs any registered bot
```

Bots must be implemented using HexRoot’s `BaseBot` class and placed under the `bots/` directory or importable module paths.

---

## 🧩 Structure

| File | Description |
|------|-------------|
| `hexbot/runner.py` | Dynamically runs a bot module |
| `hexbot/registry.py` | Registers and manages named bots |
| `hexbot/config.py` | Default settings |
| `bots/sample_bot.py` | Example bot using BaseBot |
| `run.py` | CLI entry point |

---

## 🔐 License

This module is licensed and bound to HEX system modules.  
It may only be used in official HEX bots.  
See LICENSE.txt for usage rules.

<p align="center">
  <strong>© HEX Automation • All Rights Reserved</strong><br/>
  Created by <a href="https://github.com/HexTide">HexTide</a>
</p>
