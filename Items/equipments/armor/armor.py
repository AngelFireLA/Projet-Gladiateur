from Items.item import Item


class Armor(Item):
    quality_levels = ["copper", "bronze", "iron", "steel", "gold"]

    def __init__(self, name, value, image, defense: int, quality):
        super().__init__(name, value, image)
        self.defense = defense
        self.quality_name = quality
        self.quality = self.set_quality(quality)
        self.armor_type = ""

    def set_quality(self, quality):
        if quality in self.quality_levels:
            return self.quality_levels.index(quality)
        else:
            print(f"Error, {quality} is not a valid quality for equipment")
            return 0
