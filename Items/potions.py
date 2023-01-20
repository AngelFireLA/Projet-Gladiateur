from Items.item import Item


class Potion(Item):
    potion_types = ["damage", "defense", "hp", "speed", "attack_speed"]
    potion_quality = {"very_bad": 1, "bad":2, "medium": 3, "good": 4, "very_good": 5, "perfect": 6}

    def __init__(self, name, image, durability: int, quality, type, boostquantity: int, value=0):
        super().__init__(name, value, image)
        self.durability = durability
        self.quality_name = quality
        self.quality = self.potion_quality[quality]
        self.type = type
        self.boostquantity = boostquantity

        if self.type not in self.potion_types:
            print(f"Error, {self.type} is not a valid potion type")
            self.type = "damage"
        if self.quality_name not in self.potion_quality:
            print(f"Error, {self.quality_name} is not a valid potion quality name")
            self.quality_name = "very_bad"
