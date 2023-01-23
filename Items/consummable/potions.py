from Items.item import Item


class Potion(Item):
    potion_types = ["damage", "defense", "hp", "speed", "attack_speed"]
    potion_quality = {"very_bad": 1, "bad":2, "medium": 3, "good": 4, "very_good": 5, "perfect": 6}

    def __init__(self, name, image, durability: int, quality, ptype, boostquantity: int, value=0):
        super().__init__(name, value, image)
        self.durability = durability
        self.quality_name = quality
        self.quality = self.potion_quality[quality]
        self.ptype = ptype
        self.boostquantity = boostquantity
        self.used = False

        if self.ptype not in self.potion_types:
            print(f"Error, {self.ptype} is not a valid potion type")
            self.ptype = "damage"
        if self.quality_name not in self.potion_quality:
            print(f"Error, {self.quality_name} is not a valid potion quality name")
            self.quality_name = "very_bad"

    def use(self):
        if not self.used:
            self.apply_boost()
            self.decrease_durability()
            self.used = True

    def apply_boost(self,player):
        if self.ptype == "damage":
            player.strength += self.boostquantity
        elif self.ptype == "defense":
            player.defense += self.boostquantity
        elif self.ptype == "hp":
            player.hp += self.boostquantity
        elif self.ptype == "speed":
            player.speed += self.boostquantity
        elif self.ptype == "attack_speed":
            player.attack_speed += self.boostquantity

    def decrease_durability(self):
        self.durability -= 1

