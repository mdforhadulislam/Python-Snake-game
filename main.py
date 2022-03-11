import pygame
import random
import os

pygame.init()

# using colors defind
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# defind windrow or game output display
WIDTH = 900
HEIGHT = 600
game_windrow = pygame.display.set_mode((WIDTH, HEIGHT))

# game windrow Title
pygame.display.set_caption("Snake Game")
pygame.display.update()


def plot_snack(game_windrow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(game_windrow, color, [x, y, snake_size, snake_size])


# game loop
def game_loop():
    # game looping variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 45
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    fps = 100
    food_x = random.randint(0, WIDTH / 2)
    food_y = random.randint(0, HEIGHT / 2)
    score = 0
    Clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 40)

    def scroe_text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        game_windrow.blit(screen_text, [x, y])

    snake_list = []
    snake_len = 1

    with open("hi score.txt","r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            game_windrow.fill(black)
            scroe_text_screen("Your Score: "+str(score), red, (WIDTH/2)-110, 150)
            scroe_text_screen("Game Is Over! Press Enter To continue", red, 150, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 3
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -3
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -3
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = 3

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                food_x = random.randint(0, WIDTH / 2)
                food_y = random.randint(0, HEIGHT / 2)
                snake_len += 3
            game_windrow.fill(white)

            if score > int(hiscore):
                hiscore = score

            scroe_text_screen('Scroe: ' + str(score)+" "+ " High Score "+str(hiscore), red, 5, 5)
            pygame.draw.rect(game_windrow, black, [snake_x, snake_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_len:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > WIDTH or snake_y < 0 or snake_y > HEIGHT:
                game_over = True

            pygame.draw.rect(game_windrow, red, [food_x, food_y, snake_size, snake_size])
            plot_snack(game_windrow, black, snake_list, snake_size)

        pygame.display.update()
        Clock.tick(fps)

    # quit the program file
    pygame.quit()
    quit()


game_loop()
