import pygame

class Item():
    item_counter = 0

    def __init__(self, name, value, image):
        Item.item_counter += 1
        self.id = Item.item_counter
        self.name = name
        self.value = value
        #self.surface = pygame.image.load(image).convert_alpha()
