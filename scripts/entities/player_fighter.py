from scripts.entities.player import Player


class PlayerFighter:

    def __init__(self, player: Player, screen, strength, speed, attack_speed, hp, defense, stamina):

        self.player = player
        self.screen = screen
        self.strength = strength
        self.speed = speed
        self.attack_speed = attack_speed
        self.hp = hp
        self.defense = defense
        self.stamina = stamina

        self.equipped = {
            "chestplate": None,
            "leggings": None,
            "boots": None,
            "weapon": None,
            "shield": None,
            "potions": []
        }


    def use_potion(self, potion_index):
        # use specified potion
        if self.equipments["potions"][potion_index]:
            self.equipments["potions"][potion_index].use()
            self.equipments["potions"][potion_index] = None

    def win(self, prize_money):
        # increase player money and popularity for winning
        self.player.money += prize_money
        self.player.popularity += 1
        self.player.wins += 1

    def lose(self):
        # decrease player popularity for losing
        self.player.popularity -= 1

