from .store_area import StoreArea

class YoungAdults(StoreArea):
    def __init__(self):
        super().__init__("Young Adults", "Back of the store")
        self.age_category = "13-21"
        self.clothing_items = []

    def add_clothing(self, clothing_item):
        if clothing_item.age_category != "13-21":
            print(f"{clothing_item.name} is not suitable for the Young Adults' section.")
            return
        self.clothing_items.append(clothing_item)

class YoungMen:
    def __init__(self):
        self.name = "Young Men's Section"

class YoungWomen:
    def __init__(self):
        self.name = "Young Women's Section"
