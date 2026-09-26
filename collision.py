def bullet_hits_asteroid(bullet, asteroid):
    return bullet.rect.colliderect(asteroid.rect)


def player_hits_asteroid(player, asteroid):
    return player.rect.colliderect(asteroid.rect)