import pygame


class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 5, y - 20, 10, 20)
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def is_off_screen(self):
        return self.rect.bottom < 0