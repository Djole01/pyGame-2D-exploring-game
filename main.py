import pygame
import os
import pySpaceShooter
import random

pygame.display.set_caption("Space Shooter")

pygame.mixer.init()
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join(('Assets'), 'Grenade.wav'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join(('Assets'), 'Gun.wav'))

FPS = 60
MAX_BULLETS = 10
HEIGHT = pySpaceShooter.HEIGHT
WIDTH = pySpaceShooter.WIDTH


def main():
    red = pygame.Rect(750, 500, pySpaceShooter.SPACESHIP_WIDTH, pySpaceShooter.SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, pySpaceShooter.SPACESHIP_WIDTH, pySpaceShooter.SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    direction = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == pySpaceShooter.RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == pySpaceShooter.YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        if winner_text != "":
            pySpaceShooter.draw_winner(winner_text)
            break
        keys_pressed = pygame.key.get_pressed()
        pySpaceShooter.yellow_handle_movement(keys_pressed, yellow)
        '''
        if red.y < 50 and direction == 0:
            direction = 1
        elif red.y > 420 and direction == 1:
            direction = 0
        elif red.y > 50 and direction == 0:
            direction = 0'''

        if red.x < WIDTH//2:
            direction = random.choice([1, 2])
        elif red.x > WIDTH - pySpaceShooter.SPACESHIP_WIDTH:
            direction = random.choice([0, 3])
        elif red.y < 0:
            direction = random.choice([2, 3])
        elif red.y > HEIGHT - pySpaceShooter.SPACESHIP_HEIGHT - 15:
            direction = random.choice([0, 1])

        pySpaceShooter.red_ai_handle_movement(yellow_bullets, red, direction)
        pySpaceShooter.handle_bullets(yellow_bullets, red_bullets, yellow, red)
        pySpaceShooter.draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()


if __name__ == "__main__":
    main()
