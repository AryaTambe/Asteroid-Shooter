import pygame
import random
from settings import WIDTH, HEIGHT


class Asteroid:
    def __init__(self, speed, tracking=False):
        self.image = pygame.image.load(
            "assets/images/asteroid.png"
        )
        self.image = pygame.transform.scale(
            self.image, (50, 50)
        )

        x = random.randint(0, WIDTH - 50)

        self.rect = self.image.get_rect(
            topleft=(x, -50)
        )

        self.speed = speed
        self.tracking = tracking

    def update(self, player=None):
        if self.tracking and player:
            if self.rect.centerx < player.rect.centerx:
                self.rect.x += 1

            elif self.rect.centerx > player.rect.centerx:
                self.rect.x -= 1

        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.rect.top > HEIGHT