import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MONKI")

YELLOW = (226, 201, 41)

music_sfx = pygame.mixer.Sound("assets/sounds/pixelland.mp3")
score_sfx = pygame.mixer.Sound("assets/sounds/score.wav")
boom_sfx = pygame.mixer.Sound("assets/sounds/boom.wav")

music_sfx.set_volume(0.125)
score_sfx.set_volume(0.5)
boom_sfx.set_volume(0.5)

monkey_img = pygame.image.load("assets/sprites/monkey.png")
bg_img = pygame.image.load("assets/sprites/bg.png")
banan_img = pygame.image.load("assets/sprites/banan.png")
bomb_img = pygame.image.load("assets/sprites/bomb.png")
menu_img = pygame.image.load("assets/sprites/menu.png")
lost_img = pygame.image.load("assets/sprites/lost.png")
boom_img = pygame.image.load("assets/sprites/boom.png")
icon_img = pygame.image.load("assets/sprites/icon.png")

bg_img = pygame.transform.scale(bg_img, (960, 636))
bomb_img = pygame.transform.scale(bomb_img, (96, 96))
banan_img = pygame.transform.scale(banan_img, (96, 96))
monkey_img = pygame.transform.scale(monkey_img, (150, 150))
boom_img = pygame.transform.scale(boom_img, (160, 160))

pygame.display.set_icon(icon_img)

score_font = pygame.font.Font("assets/fonts/spellstone.ttf", 35)

clock = pygame.time.Clock()

music_sfx.play(loops=-1)


def scores(point):
    value = score_font.render("Score: " + str(point), True, YELLOW)
    win.blit(value, [10, 10])


def menu():
    game_close = False
    while not game_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game()
                elif event.key == pygame.K_q:
                    game_close = True

        win.blit(menu_img, (0, 0))
        pygame.display.update()
    pygame.quit()
    quit()


def game():
    game_over = False
    game_close = False

    x, y = WIDTH // 2 - 80, 405

    bananas = []
    bombs = []

    score = 0

    banana_interval = 100
    bomb_interval = 200

    monkey_direction = 1

    while not game_over:

        while game_close:
            win.blit(lost_img, [200, 150])
            scores(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game()
                    elif event.key == pygame.K_m:
                        menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > 0 or keys[pygame.K_a] and x:
            x -= 10
            monkey_direction = -1
        elif keys[pygame.K_RIGHT] and x < WIDTH - 150 or keys[pygame.K_d] and x < WIDTH - 150:
            x += 10
            monkey_direction = 1

        if monkey_direction == -1:
            monkey_surface = pygame.transform.flip(monkey_img.subsurface((0, 0, 150, 150)), True, False)
        else:
            monkey_surface = monkey_img.subsurface((0, 0, 150, 150))

        if random.randint(1, banana_interval) == 1:
            banana_x = random.randint(10, WIDTH - 75)
            banana_y = -75
            bananas.append([banana_x, banana_y])

        if random.randint(1, bomb_interval) == 1:
            bomb_x = random.randint(0, WIDTH - 50)
            bomb_y = -75
            bombs.append([bomb_x, bomb_y])

        if score == 50:
            banana_interval = 80
            bomb_interval = 100
        elif score == 100:
            banana_interval = 60
            bomb_interval = 50
        elif score == 150:
            banana_interval = 50
            bomb_interval = 35
        elif score == 200:
            banana_interval = 50
            bomb_interval = 25

        for banana in bananas:
            banana[1] += 10
            if y < banana[1] < y + 150 and x - 50 < banana[0] < x + 100:
                bananas.remove(banana)
                score_sfx.play()
                score += 1

        win.blit(bg_img, (0, 0))
        win.blit(monkey_surface, (x, y))

        for bomb in bombs:
            bomb[1] += 10
            if y < bomb[1] < y + 150 and x - 50 < bomb[0] < x + 80:
                bombs.remove(bomb)
                win.blit(boom_img, (x, y))
                boom_sfx.play()
                game_close = True

        for banana in bananas:
            win.blit(banan_img, (banana[0], banana[1]))

        for bomb in bombs:
            win.blit(bomb_img, (bomb[0], bomb[1]))

        scores(score)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


menu()
