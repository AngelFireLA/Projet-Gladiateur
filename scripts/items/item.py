import pygame

class Item():
    item_counter = 0

    def __init__(self, name, value, image):
        Item.item_counter += 1
        self.id = Item.item_counter
        self.name = name
        self.value = value
        self.is_equipped = False
        #self.surface = pygame.image.load(image).convert_alpha()

    def is_equipped(self, value: bool):
        self.is_equipped = value
