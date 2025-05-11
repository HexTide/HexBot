from hexroot.base import BaseBot

class Bot(BaseBot):
    def __init__(self):
        super().__init__(name="SampleBot")

    def start(self):
        print(f"[{self.name}] Running basic task...")
        print(f"[{self.name}] Done.")
