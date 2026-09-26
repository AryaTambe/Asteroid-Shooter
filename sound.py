import pygame


class Sound:
    def __init__(self):
        self.shoot = pygame.mixer.Sound("assets/sounds/shoot.wav")
        self.game_over = pygame.mixer.Sound("assets/sounds/game_over.wav")
        self.win = pygame.mixer.Sound("assets/sounds/win.wav")

    def play_shoot(self):
        self.shoot.play()

    def play_game_over(self):
        self.game_over.play()

    def play_win(self):
        self.win.play()