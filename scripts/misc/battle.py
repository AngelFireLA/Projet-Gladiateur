from scripts.entities.player_fighter import PlayerFighter
from scripts.entities.enemy import Enemy


class Battle:
    battle_counter = 0

    def __init__(self, screen, background, standing_y, prize_money, playerfighter: PlayerFighter, enemy: Enemy):
        Battle.battle_counter += 1
        self.id = Battle.battle_counter
        self.screen = screen
        self.background = background
        self.standing_y = standing_y
        self.prize_money = prize_money
        self.player = playerfighter
        self.enemy = enemy
