'''Steve/'s West Side Clothing'''
from seasons import ColdWeatherClothing, CoolWeatherClothing, HotWeatherClothing
from clothing import ClothingItem
from store import MensClothing, YoungAdults, WomenClothing, ChildrensClothing

clothing1 = ColdWeatherClothing("Winter Jacket (Men)", 79.99, "M", "Black", "Male", "21+", "High", True)
clothing2 = CoolWeatherClothing("Hoodie (Men)", 39.99, "L", "Blue", "Male", "21+")
clothing3 = HotWeatherClothing("Sunglasses (Women)", 19.99, "One Size", "Black", "Female", "21+")

clothing4 = ColdWeatherClothing("Thermal Leggings (Women)", 29.99, "S", "Gray", "Female", "21+", "Medium", True)
clothing5 = CoolWeatherClothing("Jeans (Men)", 49.99, "M", "Denim", "Male", "21+")
clothing6 = HotWeatherClothing("Swim Shorts (Young Adults)", 34.99, "M", "Red", "Male", "13-21")

clothing7 = CoolWeatherClothing("Trench Coat (Young Adults)", 89.99, "L", "Beige", "Male", "13-21", "Medium")
clothing8 = CoolWeatherClothing("Turtleneck Sweater (Young Adults)", 44.99, "S", "Burgundy", "Male", "13-21", "Medium")
clothing9 = CoolWeatherClothing("Denim Jacket (Young Adults)", 69.99, "M", "Blue", "Male", "13-21", "Medium")
clothing10 = CoolWeatherClothing("Boho Dress (Young Adults)", 59.99, "M", "Floral", "Female", "13-21")
clothing11 = HotWeatherClothing("Sundress (Young Adults)", 34.99, "S", "Yellow", "Female", "13-21")
clothing12 = HotWeatherClothing("Tank Top (Young Adults)", 19.99, "M", "White", "Female", "13-21")
clothing13 = HotWeatherClothing("Shorts (Young Adults)", 24.99, "S", "Khaki", "Female", "13-21")

clothing14 = ColdWeatherClothing("Winter Coat (Boys)", 59.99, "S", "Blue", "Male", "0-12", "High", True)
clothing15 = ColdWeatherClothing("Snow Pants (Boys)", 39.99, "L", "Black", "Male", "0-12", "High", True)
clothing16 = CoolWeatherClothing("Sweatshirt (Boys)", 29.99, "M", "Green", "Male", "0-12", "Medium", True)
clothing17 = CoolWeatherClothing("Jeans (Girls)", 34.99, "S", "Pink", "Female", "0-12", "Medium", True)
clothing18 = HotWeatherClothing("Sundress (Girls)", 24.99, "M", "Floral", "Female", "0-12")

mens_section = MensClothing()
women_section = WomenClothing()
young_adults_section = YoungAdults()
childrens_section = ChildrensClothing()

mens_section.add_clothing(clothing1)
women_section.add_clothing(clothing1)

def print_store_inventory(mens_section, women_section, young_adults_section, childrens_section):
    print("Mens Section:")
    for item in mens_section.clothing_items:
        print(f"- {item.name}")

    print("\nWomen's Section:")
    for item in women_section.clothing_items:
        print(f"- {item.name}")

    print("\nYoung Adults Section:")
    for item in young_adults_section.clothing_items:
        print(f"- {item.name}")

    print("\nChildren's Section:")
    for item in childrens_section.clothing_items:
        print(f"- {item.name}")     
print_store_inventory(mens_section, women_section, young_adults_section, childrens_section)
