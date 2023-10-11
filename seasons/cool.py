from clothing.clothing_item import ClothingItem
from shared_attributes.shared_attributes import SharedAttributes

class CoolWeatherClothing(ClothingItem, SharedAttributes):
    def __init__(self, name, price, size, color, gender, marketed_age, full_skin_coverage=True, insulation_level="Medium"):
        super().__init__(name, price, size, color, gender, marketed_age)
        self.full_skin_coverage = full_skin_coverage
        self.insulation_level = insulation_level
        