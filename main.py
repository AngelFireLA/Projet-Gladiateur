import pygame, sys, win32gui, win32con

from utils.button import Button
from utils.gamestate import GameState

# Setup la fenêtre Pygame
pygame.init()
video_infos = pygame.display.Info()
width, height = video_infos.current_w, video_infos.current_h
screen = pygame.display.set_mode((10, 10), pygame.RESIZABLE)
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

start_menu = GameState("start_menu", '')
test_battle = GameState("test_battle", '')

clock = pygame.time.Clock()


#Placeholder start menu stuff:
button_img = pygame.image.load("assets/images/ui/buttons/button_placeholder.png").convert_alpha()
normal_button = Button(width / 2, 120, 1.8, "Normal", button_img, screen, taille_texte=40)


def get_screen():
    return screen




def event_manager():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

start_menu.enable()
while True:
    screen.fill((50, 50, 255))
    event_manager()
    if start_menu.is_enabled():
        if normal_button.draw():
            test_battle.enable()

    clock.tick(60)
    pygame.display.flip()

