from .store_area import StoreArea

class WomenClothing(StoreArea):
    def __init__(self):
        super().__init__("Women's", "Front of the store")
        self.age_category = "21+"
        self.clothing_items = []

    def add_clothing(self, clothing_item):
        if clothing_item.gender != "Female":
            print(f"{clothing_item.name} is not suitable for the Women's section.")
            return
        self.clothing_items.append(clothing_item)
