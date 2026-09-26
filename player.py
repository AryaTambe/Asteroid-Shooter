import pygame
from settings import WIDTH, HEIGHT
from bullet import Bullet


class Player:
    def __init__(self):
        self.width = 50
        self.height = 40

        # Start near the bottom-center of the screen
        self.rect = pygame.Rect(
            WIDTH // 2 - self.width // 2,
            HEIGHT - 70,
            self.width,
            self.height
        )

        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Keep player inside the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
        return Bullet(
            self.rect.centerx,
            self.rect.top
        )

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            (50, 200, 255),
            [
                (self.rect.centerx, self.rect.top),
                (self.rect.left, self.rect.bottom),
                (self.rect.right, self.rect.bottom)
            ]
        )