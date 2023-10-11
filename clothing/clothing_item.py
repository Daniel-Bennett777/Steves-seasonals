class ClothingItem:
    def __init__(self, name, price, size, color, gender, marketed_age):
        self.name = name
        self.price = price
        self.size = size
        self.color = color
        self.gender = gender  # "Male" or "Female" (or more options as needed)
        self.marketed_age = marketed_age  # Age range (e.g., "21+", "13-21", "0-12")

    def display_info(self):
        return f"Name: {self.name}\nPrice: ${self.price:.2f}\nSize: {self.size}\nColor: {self.color}"
