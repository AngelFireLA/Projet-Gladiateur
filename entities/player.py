import pygame

class Player():
    def __init__(self, name, screen, strength, speed, attack_speed, hp, defense, stamina, gold):
        self.name = name
        self.screen = screen
        self.strength = strength
        self.speed = speed
        self.attack_speed = attack_speed
        self.hp = hp
        self.defense = defense
        self.stamina = stamina
        self.money = 0
        self.popularity = 0
        self.equipment = {}
        self.potions = {}
        self.league = 1
        self.wins = 0

    def move(self, direction):
        # move player sprite in the specified direction
        pass

    def attack(self):
        # handle player attacking
        pass

    def use_potion(self, potion_name):
        # use specified potion
        pass

    def equip(self, equipment_name):
        # equip specified equipment
        pass

    def train(self):
        # increase player stats through training
        pass

    def rest(self):
        # increase player endurance through rest
        pass

    def level_up(self):
        # increase player level based on stats
        pass

    def win(self, prize_money):
        # increase player money and popularity for winning
        self.money += prize_money
        self.popularity += 1
        self.wins += 1

    def lose(self):
        # decrease player popularity for losing
        self.popularity -= 1
