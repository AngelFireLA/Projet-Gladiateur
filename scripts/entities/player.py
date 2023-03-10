from scripts.items.equipments.hand_held.shields.shield import Shield
from scripts.items.equipments.hand_held.weapons.weapon import Weapon
from scripts.items.equipments.armor.armor import Armor
from scripts.items.potions import Potion
from scripts.items import item


class Player:
    def __init__(self, name, screen, strength, speed, attack_speed, hp, defense, stamina, gold):
        self.name = name
        self.screen = screen
        self.strength = strength
        self.speed = speed
        self.attack_speed = attack_speed
        self.hp = hp
        self.defense = defense
        self.stamina = stamina
        self.money = gold
        self.popularity = 0
        self.league = 1
        self.wins = 0
        self.items = []
        self.equipped = {
            "chestplate": None,
            "leggings": None,
            "boots": None,
            "weapon": None,
            "shield": None,
            "potions": []
        }


    def check_slots(self):
        # check if each of these slots have something equipped in them
        for part, equipment in self.equipped.items():
            if equipment:
                print(f"{part} slot is equipped with {equipment.name} of id {equipment.id}")
            else:
                print(f"{part} slot is empty")

    def train(self):
        # increase player stats through training
        pass

    def rest(self):
        # increase player endurance through rest
        pass

    def level_up(self):
        # increase player level based on stats
        pass


    def add_item(self, item):
        #Add an item to the player's inventory
        if item in self.items:
            print(f"Error, {item.name} with id {item.id} is already in the player's inventory !")
        else:
            self.items.append(item)

    def remove_item(self, item):
        #Remove an item from the player's inventory
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"Error, {item.name} with id {item.id} is not in the player's inventory !")

    def equip_item(self, item):
        #Equip an item from the player's inventory
        if item in self.items:
            if isinstance(item, Weapon):
                self.equipped['weapon'] = item
            elif isinstance(item, Shield):
                self.equipped['shield'] = item
            elif isinstance(item, Armor):
                if item.slot in self.equipped:
                    self.equipped[item.slot] = item
            elif isinstance(item, Potion):
                if len(self.equipped["potions"]) < 3:
                    self.equipped["potions"].append(item)
                else:
                    print("There are already 3 potions equipped.")
            else:
                print(f"{item.name} of id {item.id} is not a valid item to equip in any slot.")
            return True
        return False

    def unequip_item(self, item):
        #Unequip an item
        if item in self.equipped:
            if isinstance(item, Weapon):
                self.equipped['weapon'] = None
            elif isinstance(item, Shield):
                self.equipped['shield'] = None
            elif isinstance(item, Armor):
                self.equipped[item.slot] = None
            else:
                print(f"{item.name} of id {item.id} is not a valid item to equip in any slot.")
            return True
        elif item in self.equipped["potions"]:
            if isinstance(item, Potion):
                self.equipped["potions"].remove(item)
        else:
            print(f"{item.name} of id {item.id} was not equipped.")
        return False

    def show_inventory(self):
        for k, v in self.equipped.items():
            if isinstance(v, item.Item):
                print(f'{k.upper()} : {v.name}')
            else:
                print(f'{k.upper()} : {v}')


