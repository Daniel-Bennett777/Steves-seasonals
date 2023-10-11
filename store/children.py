from .store_area import StoreArea

class ChildrensClothing(StoreArea):
    def __init__(self):
        super().__init__("Children's", "Middle of the store")
        self.age_category = "0-12"
        self.clothing_items = []
        self.boys_section = BoysSection()
        self.girls_section = GirlsSection()

    def add_clothing(self, clothing_item):
        if clothing_item.age_category != "0-12":
            print(f"{clothing_item.name} is not suitable for the Children's section.")
            return

        # Check the gender of the clothing item
        if clothing_item.gender == "Male":
            # Add it to the Boys Section
            self.boys_section.clothing_items.append(clothing_item)
        elif clothing_item.gender == "Female":
            # Add it to the Girls Section
            self.girls_section.clothing_items.append(clothing_item)
        else:
            print(f"{clothing_item.name} has an unspecified gender and cannot be added to the Children's section.")

class BoysSection:
    def __init__(self):
        self.name = "Boys Section"
        self.clothing_items = []  # List to store clothing items specific to boys

class GirlsSection:
    def __init__(self):
        self.name = "Girls Section"
        self.clothing_items = []
