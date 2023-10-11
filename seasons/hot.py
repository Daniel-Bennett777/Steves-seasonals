from clothing.clothing_item import ClothingItem

class HotWeatherClothing(ClothingItem):
    def __init__(self, name, price, size, color, gender, marketed_age, low_insulation=True):
        super().__init__(name, price, size, color, gender, marketed_age)
        self.low_insulation = low_insulation
