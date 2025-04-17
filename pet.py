import io
import sys

# Force UTF-8 encoding for stdout in Windows
if sys.stdout.encoding != 'UTF-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

class Pet:
    def __init__(self, name, pet_type="dog"):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.pet_type = pet_type.lower()
        self.emoji = self._get_emoji()
        self.is_sleeping = False 
    
    def _get_emoji(self):
        emojis = {
            "cat": "🐈"
        }
        return emojis.get(self.pet_type, "🐾")

    def eat(self):
        if self.is_sleeping:
            print(f" {self.name} is sleeping. Don't wake him")
            return
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating...")

    def sleep(self):
        self.is_sleeping = True
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...")

    def play(self):
        if self.is_sleeping:
            print(f"{self.name} is sleeping. Maybe play later.")
            return
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing...")
        else:
            print(f"{self.name} is too tired to play")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned {trick}")

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} no tricks")
        else:
            print(f"Tricks: {', '.join(self.tricks)}")

    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"🍖 Hunger: {self.hunger}")
        print(f"😊 Happiness: {self.happiness}")
        print(f"⚡ Energy: {self.energy}")
        print(f"💤 Sleeping: {'Yes' if self.is_sleeping else 'No'}")
        if self.tricks:
            print(f"Tricks: {self.tricks}")
    
    def speak(self):
        sounds = {
            "cat": "Meow"
        }
        sound = sounds.get(self.pet_type, "Hello")
        print(f"{self.emoji} {self.name} says: {sound}")
        return sound
    
    def wake_up(self):
        "Wake the pet up"
        if not self.is_sleeping:
            print(f"{self.name} is already awake")
            return
        self.is_sleeping = False
        print(f"{self.name} woke up! Good morning")

