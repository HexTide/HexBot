import importlib
import sys
from hexroot.base import BaseBot

class BotRunner:
    def __init__(self, bot_path: str):
        self.bot_path = bot_path

    def run(self):
        print(f"[HexBot] Trying to load: {self.bot_path}")
        try:
            module = importlib.import_module(self.bot_path)
            if hasattr(module, "Bot"):
                bot_instance = module.Bot()
                if isinstance(bot_instance, BaseBot):
                    print(f"[HexBot] Starting bot: {bot_instance.name}")
                    bot_instance.start()
                else:
                    raise TypeError("Loaded object is not a subclass of BaseBot")
            else:
                raise AttributeError("Module has no 'Bot' class")
        except Exception as e:
            print(f"[HexBot] Failed to run bot: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python runner.py <module.path.to.bot>")
    else:
        path = sys.argv[1]
        runner = BotRunner(path)
        runner.run()
