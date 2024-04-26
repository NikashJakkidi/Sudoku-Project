import pygame

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 9
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
FONT = pygame.font.Font(None, 40)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GRAY = (200, 200, 200)
class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE
        pygame.draw.rect(self.screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))

        if self.selected:
            pygame.draw.rect(self.screen, RED, (x, y, CELL_SIZE, CELL_SIZE), 3)
        else:
            pygame.draw.rect(self.screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

        text = FONT.render(str(self.value), True, BLACK) if self.value != 0 else None
        if text:
            text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
            self.screen.blit(text, text_rect)