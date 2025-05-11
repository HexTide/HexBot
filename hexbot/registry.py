from typing import Callable

class BotRegistry:
    def __init__(self):
        self._bots = {}

    def register(self, name: str, loader: Callable):
        self._bots[name] = loader

    def get(self, name: str):
        return self._bots.get(name)

    def list(self):
        return list(self._bots.keys())

# Global instance
registry = BotRegistry()
