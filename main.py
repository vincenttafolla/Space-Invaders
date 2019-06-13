import pygame
from player import Player
from bullet import Bullet
from enemy import Enemy
from squadron import Squadron

# Game Settings
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
GAME_SIDE_MARGIN = 20
GAME_TOP_MARGIN = 40
GAME_BOTTOM_MARGIN = GAME_TOP_MARGIN
GAME_BORDER_WIDTH = 3

GAME_WALL_TOP = GAME_TOP_MARGIN + GAME_BORDER_WIDTH
GAME_WALL_RIGHT = WINDOW_WIDTH - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH
GAME_WALL_BOTTOM = WINDOW_HEIGHT - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH
GAME_WALL_LEFT = GAME_SIDE_MARGIN + GAME_BORDER_WIDTH

# Colors
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_BLUE = (0,0,255)

# Setup Pygame Elements
pygame.init()
game_display = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('SPACE INVADERS')
title_font = pygame.font.SysFont('BATMAN', 40, True)
score_font = pygame.font.SysFont('Arial', 28, True)
title_text = title_font.render('SPACE INVADERS', False, COLOR_BLUE)
clock = pygame.time.Clock()

# Load Media
player_img = pygame.image.load('media/si-player.gif')
bullet_img = pygame.image.load('media/si-bullet.gif')
enemy_img = pygame.image.load('media/si-enemy.gif')
background_img = pygame.image.load('media/si-background.gif')


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.is_alive = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_SPACE:
                player.shoot(bullet_img)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop_moving()

player = Player(GAME_WALL_LEFT, GAME_WALL_RIGHT, GAME_WALL_BOTTOM, player_img)
levels = []
levels.append(Squadron(GAME_WALL_LEFT, GAME_WALL_TOP, 3, 5, 2, enemy_img))
levels.append(Squadron(GAME_WALL_LEFT, GAME_WALL_TOP, 3, 5, 4, enemy_img))
levels.append(Squadron(GAME_WALL_LEFT, GAME_WALL_TOP, 5, 6, 2, enemy_img))
levels.append(Squadron(GAME_WALL_LEFT, GAME_WALL_TOP, 5, 6, 4, enemy_img))
levels.append(Squadron(GAME_WALL_LEFT, GAME_WALL_TOP, 6, 6, 4, enemy_img))
levels.append(Squadron(GAME_WALL_LEFT, GAME_WALL_TOP, 7, 7, 3, enemy_img))
levels.append(Squadron(GAME_WALL_LEFT, GAME_WALL_TOP, 8, 8, 4, enemy_img))
levels.append(Squadron(GAME_WALL_LEFT, GAME_WALL_TOP, 9, 9, 4, enemy_img))
levels.append(Squadron(GAME_WALL_LEFT, GAME_WALL_TOP, 10, 10, 4, enemy_img))

level_number = 0

# main game loop
while player.is_alive:

    squadron = levels[level_number]

    if len(squadron.enemies) == 0:
        level_number += 1 

    handle_events()

    game_display.blit(game_display, (0,0))
    game_display.fill(COLOR_BLACK)
    pygame.draw.rect(game_display, COLOR_WHITE, \
         (GAME_SIDE_MARGIN, GAME_TOP_MARGIN, \
         WINDOW_WIDTH - GAME_SIDE_MARGIN * 2, \
         WINDOW_HEIGHT - GAME_TOP_MARGIN - GAME_BOTTOM_MARGIN))
    game_display.blit(background_img, \
        (GAME_WALL_LEFT, GAME_WALL_TOP), \
        (0, 0, GAME_WALL_RIGHT - GAME_WALL_LEFT, GAME_WALL_BOTTOM - GAME_WALL_TOP))
    game_display.blit(title_text, (WINDOW_WIDTH / 2 - title_text.get_width() / 2, 5))
    score_text = score_font.render('SCORE:' + str(player.score), False, COLOR_BLUE)
    game_display.blit(score_text, (GAME_SIDE_MARGIN, WINDOW_HEIGHT - score_text.get_height()))

    squadron.move(GAME_WALL_LEFT, GAME_WALL_RIGHT)

    player.remove_missed_bullets(GAME_WALL_TOP)

    player.kill_enemies_colliding_with_bullets(squadron, game_display)

    player.kill_player_if_invaded(squadron, GAME_WALL_BOTTOM)

    player.show(GAME_WALL_LEFT, GAME_WALL_RIGHT, game_display)
    squadron.show(game_display)

    pygame.display.update()
    clock.tick(60)

pygame.quit()