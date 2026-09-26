import pygame
import random

from settings import WIDTH, HEIGHT, FPS, STARTING_LIVES
from player import Player
from asteroid import Asteroid
from level import get_level
from collision import bullet_hits_asteroid, player_hits_asteroid
from ui import UI
from sound import Sound


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Asteroid Shooter")

        self.clock = pygame.time.Clock()

        self.background = pygame.image.load(
            "assets/images/space_background.png"
        )
        self.background = pygame.transform.scale(
            self.background, (WIDTH, HEIGHT)
        )

        self.player = Player()
        self.bullets = []
        self.asteroids = []

        self.score = 0
        self.lives = STARTING_LIVES
        self.level = 1
        self.spawn_timer = 0

        self.ui = UI()
        self.sound = Sound()

        self.game_over = False
        self.win = False

        self.level_message_timer = 90
        self.hit_timer = 0

        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    if not self.game_over and not self.win:
                        self.bullets.append(
                            self.player.shoot()
                        )
                        self.sound.play_shoot()

                if event.key == pygame.K_r:
                    if self.game_over or self.win:
                        self.restart()

    def update(self):
        if self.game_over or self.win:
            return

        if self.hit_timer > 0:
            self.hit_timer -= 1

        if self.level_message_timer > 0:
            self.level_message_timer -= 1
            return

        self.player.update()

        target, speed, spawn_delay = get_level(self.level)

        self.spawn_timer += 1

        if self.spawn_timer >= spawn_delay:
            self.asteroids.append(
                Asteroid(speed, self.level == 3)
            )
            self.spawn_timer = 0

        for bullet in self.bullets:
            bullet.update()

        self.bullets = [
            bullet for bullet in self.bullets
            if not bullet.is_off_screen()
        ]

        for asteroid in self.asteroids:
            asteroid.update(self.player)

        self.check_collisions()

        self.asteroids = [
            asteroid for asteroid in self.asteroids
            if not asteroid.is_off_screen()
        ]

        if self.score >= 10 and self.level == 1:
            self.level = 2
            self.level_message_timer = 90
            self.asteroids.clear()

        elif self.score >= 20 and self.level == 2:
            self.level = 3
            self.level_message_timer = 90
            self.asteroids.clear()

        elif self.score >= 30:
            self.win = True
            self.sound.play_win()

        if self.lives <= 0:
            self.game_over = True
            self.sound.play_game_over()

    def check_collisions(self):
        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:

                if bullet_hits_asteroid(
                    bullet, asteroid
                ):
                    self.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)

                    self.score += 1
                    break

        for asteroid in self.asteroids[:]:

            if player_hits_asteroid(
                self.player, asteroid
            ):
                self.asteroids.remove(asteroid)
                self.lives -= 1
                self.hit_timer = 30

    def draw(self):
        self.screen.blit(
            self.background, (0, 0)
        )

        if self.hit_timer > 0:
            flash = pygame.Surface((WIDTH, HEIGHT))
            flash.fill((255, 0, 0))
            flash.set_alpha(80)
            self.screen.blit(flash, (0, 0))

        self.player.draw(self.screen)

        for bullet in self.bullets:
            bullet.draw(self.screen)

        for asteroid in self.asteroids:
            asteroid.draw(self.screen)

        self.ui.draw(
            self.screen,
            self.score,
            self.lives,
            self.level
        )

        if self.level_message_timer > 0:
            self.ui.level_message(
                self.screen,
                self.level
            )

        if self.game_over:
            self.ui.game_over(
                self.screen,
                self.score
            )

        if self.win:
            self.ui.win(
                self.screen,
                self.score
            )

        pygame.display.flip()

    def restart(self):
        self.player = Player()
        self.bullets = []
        self.asteroids = []

        self.score = 0
        self.lives = STARTING_LIVES
        self.level = 1
        self.spawn_timer = 0

        self.game_over = False
        self.win = False
        self.level_message_timer = 90
        self.hit_timer = 0

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(FPS)

        pygame.quit()