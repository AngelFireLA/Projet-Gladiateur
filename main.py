import pygame, time, sys, win32gui, win32con, button

from pygame import mixer
from pygame.locals import *

from random import randint

# Setup la fenêtre Pygame
pygame.init()
video_infos = pygame.display.Info()
width, height = video_infos.current_w, video_infos.current_h
screen = pygame.display.set_mode((10, 10), pygame.RESIZABLE)
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

mixer.init()

game_state = {"start_menu": True}

def get_screen():
    return screen

def set_game_state(new_game_state):
    global game_state
    if new_game_state in game_state:
        game_state = {key: False if key != new_game_state else True for key in game_state}
    else:
        print("Tried to change to a gamestate that doesn't exist !")


def play_sound(name, volume):
    mixer.music.load(name)
    mixer.music.set_volume(volume)
    mixer.music.play()


def place_text(x, y, text, size, color=None):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    if color:
        text = font.render(text, True, color)
    else:
        text = font.render(text, True, (150, 150, 150))
    fenetre.blit(text, text.get_rect(center=(x, y)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    pygame.display.flip()

