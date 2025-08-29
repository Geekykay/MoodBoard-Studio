# moodboard.py
# This a fun yet practical class that lets you curate visual inspiration across categories like fashion, literature, and design

class MoodBoard:
    def __init__(self, title, category):
        self.title = title
        self.category = category
        self.pins = []

    def add_pin(self, pin):
        self.pins.append(pin)

    def show_board(self):
        print(f"\nMoodBoard: {self.title} ({self.category})")
        for i, pin in enumerate(self.pins, 1):
            print(f"{i}. {pin}")

# Polymorphism: Different types of boards with same method name but different behavior
class FashionBoard(MoodBoard):
    def show_board(self):
        print(f"\n👗 Fashion Inspiration: {self.title}")
        for pin in self.pins:
            print(f"- Style: {pin}")

class InteriorBoard(MoodBoard):
    def show_board(self):
        print(f"\n🛋️ Interior Design Mood: {self.title}")
        for pin in self.pins:
            print(f"- Decor Idea: {pin}")

# Create instances
african_fashion = FashionBoard("AfroChic", "Fashion")
african_fashion.add_pin("Ankara jumpsuit")
african_fashion.add_pin("Kente streetwear")

reading_corner = MoodBoard("Book Nook", "Literature")
reading_corner.add_pin("Chimamanda Ngozi Adichie quote")
reading_corner.add_pin("Cover art of 'The Secret Lives of Baba Segi’s Wives'")

living_space = InteriorBoard("Lagos Loft", "Interior Design")
living_space.add_pin("Rattan furniture")
living_space.add_pin("Earth-tone palette")

# Display boards
african_fashion.show_board()
reading_corner.show_board()
living_space.show_board()