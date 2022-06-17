from math import floor
import pygame
from random import randint
import sys

# Grid colours
LIGHT_GREY = (150, 150, 150)    # Lines
DARK_GREY = (50, 50, 50)        # BG

BLACK = (0, 0, 0)               # Pressed

WHITE = (255, 255, 255)

RED = (255, 0, 0)               # Flagged

# Number colours
LIGHT_BLUE = (150, 150, 255)    # 1, 2
BLUE = (0, 0, 255)              # 3, 4
YELLOW = (255, 255, 0)          # 5, 6
ORANGE = (255, 150, 0)          # 7, 8

BLOCKSIZE = 20

GRID_HEIGHT_PX = 500
WIDTH = 500
HEIGHT = 650
SCREEN_SIZE = (WIDTH, HEIGHT)

pygame.font.init()
COMICSANSMS = pygame.font.SysFont("comicsansms", 30)


pygame.init()
WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Alexis' Minesweeper")
clock = pygame.time.Clock()


def draw_grid() -> None:
    """
    Draws a grid on the screen with white space at the bottom 
    that can be used for buttons, score, time etc.

    Grid for loop, thanks to the answer in
    https://stackoverflow.com/questions/61061963/
    """
    WIN.fill(WHITE)
    grid_rect = pygame.Rect((0, 0), (500, 500))
    pygame.draw.rect(WIN, DARK_GREY, grid_rect)

    for x in range(WIDTH // BLOCKSIZE):
        for y in range(GRID_HEIGHT_PX // BLOCKSIZE):
            rect = pygame.Rect(x*BLOCKSIZE, y*BLOCKSIZE,
                               BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(WIN, LIGHT_GREY, rect, 1)


def get_mines(number_of_mines) -> list:
    """
    Returns a list with coordinates of number_of_mines mines.
    """
    grid_width = WIDTH // BLOCKSIZE
    grid_height = GRID_HEIGHT_PX // BLOCKSIZE

    mine_coords = []

    for i in range(number_of_mines):
        rand_x = randint(0, grid_width) * 20
        rand_y = randint(0, grid_height) * 20
        mine_coords.append((rand_x, rand_y))

    return mine_coords


def main() -> None:
    """
    Main game method
    """
    NUM_MINES = 100
    MINES = get_mines(NUM_MINES)

    pressed = []

    while True:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    floor_x = floor(mouse_x / BLOCKSIZE) * BLOCKSIZE
                    floor_y = floor(mouse_y / BLOCKSIZE) * BLOCKSIZE
                    mouse_grid_pos = (floor_x, floor_y)

                    if mouse_grid_pos in MINES:
                        print("BOOM!")          # Testing message
                        pygame.time.wait(1000)  # Wait 1s
                        pygame.quit()
                        sys.exit()
                    else:
                        click_rect = pygame.Rect(
                            mouse_grid_pos, (BLOCKSIZE, BLOCKSIZE)
                            )
                        pressed.append(click_rect)
                        
        draw_grid()
        for pressed_rect in pressed:
            pygame.draw.rect(WIN, BLACK, pressed_rect)
        pygame.display.update()
        clock.tick(12)



if __name__ == "__main__":
    main()