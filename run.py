import sys
import os

# HEX system paths (adjust if needed)
sys.path.append(os.path.abspath("../HexRoot"))

from hexbot.runner import BotRunner
from hexbot.config import DEFAULT_BOT

if __name__ == "__main__":
    print(f"[HexBot] Starting default bot: {DEFAULT_BOT}")
    BotRunner(DEFAULT_BOT).run()
