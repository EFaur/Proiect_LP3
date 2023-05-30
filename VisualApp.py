import pygame
import logic

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensions
WIDTH = 450
HEIGHT = 450
GRID_SIZE = 4
CELL_SIZE = 100
MARGIN = 10

pygame.init()
FONT = pygame.font.SysFont(None, 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 Game")

def draw_grid(mat):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_value = mat[row][col]
            rect = pygame.Rect(
                col * CELL_SIZE + (col + 1) * MARGIN,
                row * CELL_SIZE + (row + 1) * MARGIN,
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(screen, GRAY, rect)
            if cell_value != 0:
                color = get_cell_color(cell_value)
                pygame.draw.rect(screen, color, rect)
                text = FONT.render(str(cell_value), True, WHITE)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

def get_cell_color(value):
    if value == 2:
        return RED
    elif value == 4:
        return GREEN
    else:
        return BLUE

def game_loop():
    mat = logic.start_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    mat, flag = logic.move_up(mat)
                elif event.key == pygame.K_s:
                    mat, flag = logic.move_down(mat)
                elif event.key == pygame.K_a:
                    mat, flag = logic.move_left(mat)
                elif event.key == pygame.K_d:
                    mat, flag = logic.move_right(mat)
                else:
                    continue

                status = logic.get_current_state(mat)
                if status == "GAME NOT OVER":
                    logic.add_new_2(mat)
                else:
                    print(status)
                    return

        screen.fill(BLACK)
        draw_grid(mat)
        pygame.display.flip()

game_loop()
