from scripts.items.item import Item

class Shield(Item):
    quality_levels = ["copper", "bronze", "iron", "steel", "gold"]

    def __init__(self, name, value, image, block_amount: int, block_delay: int, quality: int, durability: int):
        super().__init__(name, value, image)
        self.quality_name = quality
        self.quality = self.set_quality(quality)
        #How much damage is blocked :
        self.block_amount = block_amount
        #Time between blocks when durability is broken :
        self.block_delay = block_delay
        #How much hits can the shield handle before being unusable :
        self.durability = durability

    def set_quality(self, quality):
        if quality in self.quality_levels:
            return self.quality_levels.index(quality)
        else:
            print(f"Error, {quality} is not a valid quality for equipment")
            return 0
