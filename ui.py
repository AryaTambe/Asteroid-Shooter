import pygame
from settings import WHITE


class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.big_font = pygame.font.Font(None, 60)
        self.small_font = pygame.font.Font(None, 25)

    def draw(self, screen, score, lives, level):
        score_text = self.font.render(f"SCORE: {score}", True, WHITE)
        level_text = self.font.render(f"LEVEL: {level}", True, WHITE)
        lives_text = self.font.render(f"LIVES: {lives}", True, WHITE)

        screen.blit(score_text, (20, 15))
        screen.blit(level_text, (360, 15))
        screen.blit(lives_text, (680, 15))

    def level_message(self, screen, level):
        text = self.big_font.render(
            f"LEVEL {level}", True, WHITE
        )
        subtext = self.small_font.render(
            "GET READY!", True, WHITE
        )

        screen.blit(
            text,
            text.get_rect(center=(400, 270))
        )

        screen.blit(
            subtext,
            subtext.get_rect(center=(400, 320))
        )

    def game_over(self, screen, score):
        text = self.big_font.render(
            "GAME OVER", True, WHITE
        )
        score_text = self.font.render(
            f"FINAL SCORE: {score}", True, WHITE
        )
        restart_text = self.small_font.render(
            "PRESS R TO PLAY AGAIN", True, WHITE
        )

        screen.blit(
            text,
            text.get_rect(center=(400, 250))
        )

        screen.blit(
            score_text,
            score_text.get_rect(center=(400, 300))
        )

        screen.blit(
            restart_text,
            restart_text.get_rect(center=(400, 350))
        )

    def win(self, screen, score):
        text = self.big_font.render(
            "YOU WIN!", True, WHITE
        )
        subtext = self.font.render(
            "GALAXY CLEARED", True, WHITE
        )
        score_text = self.font.render(
            f"FINAL SCORE: {score}", True, WHITE
        )
        restart_text = self.small_font.render(
            "PRESS R TO PLAY AGAIN", True, WHITE
        )

        screen.blit(
            text,
            text.get_rect(center=(400, 220))
        )

        screen.blit(
            subtext,
            subtext.get_rect(center=(400, 275))
        )

        screen.blit(
            score_text,
            score_text.get_rect(center=(400, 320))
        )

        screen.blit(
            restart_text,
            restart_text.get_rect(center=(400, 370))
        )