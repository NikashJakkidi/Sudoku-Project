from Cell import Cell
import pygame

class Board (Cell):
    pygame.init()
    # Constants
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    GRID_SIZE = 9
    CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
    FONT = pygame.font.Font(size=40)

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    CREAM = (255,255,245)
    RED = (255, 0, 0)
    LIGHT_GRAY = (200, 200, 200)

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i, j, screen) for j in range(9)] for i in range(9)]
        self.selected_cell = None

    def draw(self):
        for row in self.cells:
            for cell in row:
                if cell != 0 and cell is not None:
                    cell.draw()
        # Draw bold lines for 3x3 boxes
        for i in range(0, self.width, Board.CELL_SIZE * 3):
            pygame.draw.line(self.screen, Board.BLACK, (i, 0), (i, self.height), 4)
            pygame.draw.line(self.screen, Board.BLACK, (0, i), (self.width, i), 4)

    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            col = x // Board.CELL_SIZE
            row = y // Board.CELL_SIZE
            self.select(row, col)
            return (row, col)
        return None

    def clear(self):
        if self.selected_cell and self.selected_cell.value != 0:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)

    def sketch(self, value):
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell and self.selected_cell.sketched_value == value:
            self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        for row in self.cells:
            for cell in row:
                cell.set_cell_value(0)  # Assuming initial values are stored somewhere or just reset to 0

    def is_full(self):
        return all(cell.value != 0 for row in self.cells for cell in row)

    def update_board(self):
        for row in self.cells:
            for cell in row:
                # Synchronize the actual board data structure with the displayed values
                pass

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return (i, j)
        return None

    def check_board(self):
        # Check all rows, columns, and boxes
        for i in range(9):
            if not self.valid_row(i) or not self.valid_column(i) or not self.valid_box(i // 3 * 3, (i % 3) * 3):
                return False
        return True

    def valid_row(self, row):
        seen = set()
        for col in range(9):
            value = self.cells[row][col].value
            if value in seen:
                return False
            if value != 0:
                seen.add(value)
        return True

    def valid_column(self, col):
        seen = set()
        for row in range(9):
            value = self.cells[row][col].value
            if value in seen:
                return False
            if value != 0:
                seen.add(value)
        return True

    def valid_box(self, row_start, col_start):
        seen = set()
        for i in range(3):
            for j in range(3):
                value = self.cells[row_start + i][col_start + j].value
                if value in seen:
                    return False
                if value != 0:
                    seen.add(value)
        return True