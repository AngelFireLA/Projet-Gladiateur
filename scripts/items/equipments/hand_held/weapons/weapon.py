class Weapon:
    quality_levels = ["copper", "bronze", "iron", "steel", "gold"]

    def __init__(self, name, value, image, damage: int, attack_speed: int, quality, durability_used):
        super().__init__(name, value, image)
        self.damage = damage
        self.attack_speed = attack_speed
        self.quality_name = quality
        self.quality = self.set_quality(quality)
        self.durability_used = durability_used

    def set_quality(self, quality):
        if quality in self.quality_levels:
            return self.quality_levels.index(quality)
        else:
            print(f"Error, {quality} is not a valid quality for equipment")
            return 0