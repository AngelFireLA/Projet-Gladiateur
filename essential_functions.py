import pygame
from pygame import mixer
mixer.init()
def play_sound(name, volume):
    mixer.music.load(name)
    mixer.music.set_volume(volume)
    mixer.music.play()


def place_text(x, y, text, size, screen, color=(0, 0, 0)):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text = font.render(text, True, color)
    screen.blit(text, text.get_rect(center=(x, y)))