import sys

from Board import Board
from sudoku_generator import generate_sudoku
from sudoku_generator import SudokuGenerator
from Cell import Cell
import pygame

pygame.init()
removed_cells = 0
screen = pygame.display.set_mode((Board.SCREEN_WIDTH, Board.SCREEN_HEIGHT + 100))
pygame.display.set_caption("Sudoku")

screen.fill(Board.CREAM)

# create the visuals on the Game Screen
title = (Board.FONT).render('Welcome to Sudoku!', 0, Board.BLACK)
title_rect = title.get_rect(center=(297, 150))
screen.blit(title, title_rect)

sub_title = (Board.FONT).render('Select Game Mode:', 0, Board.BLACK)
sub_title_rect = sub_title.get_rect(center=(300, 280))
screen.blit(sub_title, sub_title_rect)

first_diff = Board.FONT.render('EASY', 0, Board.BLACK)
first_rect = first_diff.get_rect(center=(110, 420))
pygame.draw.rect(screen, (255, 165, 0), (50, 400, 125, 40))
screen.blit(first_diff, first_rect)

second_diff = Board.FONT.render('MEDIUM', 0, Board.BLACK)
second_rect = second_diff.get_rect(center=(300, 420))
pygame.draw.rect(screen, (255, 165, 0), (475 / 2, 400, 125, 40))
screen.blit(second_diff, second_rect)

third_diff = Board.FONT.render('HARD', 0, Board.BLACK)
third_rect = third_diff.get_rect(center=(485, 420))
pygame.draw.rect(screen, (255, 165, 0), (425, 400, 125, 40))
screen.blit(third_diff, third_rect)
pygame.display.update()

selected_difficulty = False
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
while not selected_difficulty:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(event.pos)
            if y > 400 and y < 440:
                if x > 50 and x < 175:
                    difficulty = 'easy'
                    selected_difficulty = True
                    break
                elif x > 475 / 2 and x < 475 / 2 + 125:
                    difficulty = 'medium'
                    selected_difficulty = True
                    break
                elif x > 425 and x < 550:
                    difficulty = 'hard'
                    selected_difficulty = True
                    break
                else:
                    continue
            else:
                continue

screen.fill(Board.CREAM)
board = Board(9, 9, screen, difficulty)
board.draw()

pygame.time.wait(500)
if difficulty == 'easy':
    removed_cells = 30
elif difficulty == 'medium':
    removed_cells = 40
elif difficulty == 'hard':
    removed_cells = 50
print(removed_cells)
board_array = generate_sudoku(9, removed_cells)
print(board_array)

for i in range(len(board_array)):
    for j in range(len(board_array[i])):
        cell = Cell(board_array[i][j], i, j, screen)
        if board_array[i][j] != 0:
            cell.draw()
            print('cat')

# reset, restart, and quit buttons(location needs to be changed)
reset = Board.FONT.render('RESET', 0, Board.BLACK)
reset_rect = reset.get_rect(center=(110, 650))
pygame.draw.rect(screen, (255, 165, 0), (50, 630, 125, 40))
screen.blit(reset, reset_rect)

restart = Board.FONT.render('RESTART', 0, Board.BLACK)
restart_rect = restart.get_rect(center=(300, 650))
pygame.draw.rect(screen, (255, 165, 0), (475 / 2, 630, 125, 40))
screen.blit(restart, restart_rect)

quit = Board.FONT.render('QUIT', 0, Board.BLACK)
quit_rect = third_diff.get_rect(center=(485, 650))
pygame.draw.rect(screen, (255, 165, 0), (425, 630, 125, 40))
screen.blit(quit, quit_rect)

pygame.display.update()
print('dog')
pygame.time.wait(500)

pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.KEYDOWN)
# for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         run = False
#     elif event.type == pygame.KEYDOWN:
#         if selected_difficulty and selected_cell is not None:
#             sketch_mode = True
#             if pygame.K_1 <= event.key <= pygame.K_9:
#                 selected_number = event.key - pygame.K_0
#                 cell_value = SudokuGenerator.get_board()[selected_cell[0]][selected_cell[1]]
#
#                 if (sketch_mode or cell_value == 0) and not initial_board[selected_cell[0]][selected_cell[1]]:
#                     SudokuGenerator.get_board()[selected_cell[0]][selected_cell[1]] = selected_number
#                     print(f"Setting cell {selected_cell} to {selected_number} (Sketch mode: {sketch_mode})")
#                     print("Current state of the board:")
#                     print(SudokuGenerator.get_board())
#                 if (sketch_mode or cell_value == 0):
#                     SudokuGenerator.get_board()[selected_cell[0]][selected_cell[1]] = selected_number
#                     print(f"Setting cell {selected_cell} to {selected_number} (Sketch mode: {sketch_mode})")
#                     print("Current state of the board:")
#                     print(SudokuGenerator.get_board())
#             elif event.key == pygame.K_RETURN:
#
#                 cell_value = SudokuGenerator.get_board()[selected_cell[0]][selected_cell[1]]
#                 if sketch_mode and cell_value != 0 and not initial_board[selected_cell[0]][selected_cell[1]]:
#                     print(f"Submitting guess for cell {selected_cell}")
#                     print("Current state of the board:")
#                     print(SudokuGenerator.get_board())
#                     sketch_mode = False
#             elif event.key == pygame.K_UP and selected_cell[0] > 0:
#                 selected_cell = (selected_cell[0] - 1, selected_cell[1])
#             elif event.key == pygame.K_DOWN and selected_cell[0] < 8:
#                 selected_cell = (selected_cell[0] + 1, selected_cell[1])
#             elif event.key == pygame.K_LEFT and selected_cell[1] > 0:
#                 selected_cell = (selected_cell[0], selected_cell[1] - 1)
#             elif event.key == pygame.K_RIGHT and selected_cell[1] < 8:
#                 selected_cell = (selected_cell[0], selected_cell[1] + 1)
#             elif sketch_mode and pygame.K_1 <= event.key <= pygame.K_9:
#
#                 selected_number = event.key - pygame.K_0
#                 cell_value = SudokuGenerator.get_board()[selected_cell[0]][selected_cell[1]]
#             if not initial_board[selected_cell[0]][selected_cell[1]]:
#                 SudokuGenerator.get_board()[selected_cell[0]][selected_cell[1]] = selected_number
#                 print(f"Setting cell {selected_cell} to {selected_number} (Sketch mode: {sketch_mode})")
#                 print("Current state of the board:")
#                 print(SudokuGenerator.get_board())
selected_cell = None




def get_box_pos(pos):
    x, y, = pos
    row = x // Cell.CELL_SIZE
    col = y // Cell.CELL_SIZE
    return row, col

running=True
while running:

    for event in pygame.event.get():
        box_row = 0
        box_col = 0
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # if event.button == 1:
            click_pos = pygame.mouse.get_pos()
            box_row, box_col = get_box_pos(click_pos)
            cell = Cell(board_array[box_row][box_col], box_row, box_col, screen)
            cell.selected = True
            cell.draw()
            print(str(box_row) + " " + str(box_col))
            board.select(box_row, box_col)
            cell.draw()

            pygame.display.update()
        if event.type == pygame.KEYDOWN:
            print("Key")
            if event.key == pygame.K_1:
                cell.set_sketched_value(1)
                board.sketch(1)
                pygame.display.update()
            if event.key == pygame.K_2:
                cell.set_sketched_value(2)
                board.sketch(1)
            if event.key == pygame.K_3:
                cell.set_sketched_value(3)
                board.sketch(1)
            if event.key == pygame.K_4:
                cell.set_sketched_value(4)
                board.sketch(1)
            if event.key == pygame.K_5:
                cell.set_sketched_value(5)
                board.sketch(1)
            if event.key == pygame.K_6:
                cell.set_sketched_value(6)
                board.sketch(1)
            if event.key == pygame.K_7:
                cell.set_sketched_value(7)
                board.sketch(1)
            if event.key == pygame.K_8:
                cell.set_sketched_value(8)
                board.sketch(1)
            if event.key == pygame.K_9:
                cell.set_sketched_value(9)
                board.sketch(1)
            if event.key == pygame.K_KP_ENTER:
                if cell.sketched_value != 0:
                    board.place_number(cell.sketched_value)
                else:
                    break
            cell.selected = False
            cell.draw()




# while True:
#     # for event in pygame.event.get():
#     #     if event.type == pygame.QUIT:
#     #         running = False
#     #     if event.type == pygame.MOUSEBUTTONDOWN:
#     #         pos = pygame.mouse.get_pos()
#     #         x, y = pos[0] // Cell.CELL_SIZE, pos[1] // Cell.CELL_SIZE
#
#             # button_rect = pygame.Rect(Cell.WIDTH // 2 - 100, 150 + )
#         # elif event.type == pygame.MOUSEBUTTONDOWN:
#         #     if selected_difficulty is None:
#         #         mouse_pos = pygame.mouse.get_pos()
#         #         for difficulty, num_empty_cells in DIFFICULTIES.items():
#         #             button_rect = pygame.Rect(WIDTH // 2 - 100, 150 +
#         #                                       list(DIFFICULTIES.keys()).index(difficulty) * 50, 200, 40)
#         #             if button_rect.collidepoint(mouse_pos):
#         #                 selected_difficulty = difficulty
#         #                 sudoku_board = generate_sudoku(screen, selected_difficulty)
#
#     # print("While")
#     # for event in pygame.event.get():
#     #     print("for")
#     #     if event == pygame.MOUSEBUTTONDOWN:
#     #         print("event")
#     #         x, y = pygame.mouse.get_pos()
#     #         print(event.pos)
#     #         board.click(x, y)
#     #         board.select()

# reset, restart, and quit buttons(location needs to be changed)
# reset = Board.FONT.render('RESET', 0, Board.BLACK)
# reset_rect = reset.get_rect(center=(110, 420))
# pygame.draw.rect(screen, (255, 165, 0), (50, 400, 125, 40))
# screen.blit(reset, reset_rect)

# restart = Board.FONT.render('MEDIUM', 0, Board.BLACK)
# restart_rect = restart.get_rect(center=(300, 420))
# pygame.draw.rect(screen, (255, 165, 0), (475 / 2, 400, 125, 40))
# screen.blit(restart, restart_rect)

# quit = Board.FONT.render('HARD', 0, Board.BLACK)
# quit_rect = third_diff.get_rect(center=(485, 420))
# pygame.draw.rect(screen, (255, 165, 0), (425, 400, 125, 40))
# screen.blit(quit, quit_rect)
'''
 if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_1:
        cell.set_sketched_value(1)
        board.sketch(1)
    if event.key == pygame.K_2:
        cell.set_sketched_value(2)
        board.sketch(1)
    if event.key == pygame.K_3:
        cell.set_sketched_value(3)
        board.sketch(1)
    if event.key == pygame.K_4:
        cell.set_sketched_value(4)
        board.sketch(1)
    if event.key == pygame.K_5:
        cell.set_sketched_value(5)
        board.sketch(1)
    if event.key == pygame.K_6:
        cell.set_sketched_value(6)
        board.sketch(1)
    if event.key == pygame.K_7:
        cell.set_sketched_value(7)
        board.sketch(1)
    if event.key == pygame.K_8:
        cell.set_sketched_value(8)
        board.sketch(1)
    if event.key == pygame.K_9:
        cell.set_sketched_value(9)
        board.sketch(1)
    if event.key == pygame.K_ENTER:
        if cell.sketeched_value != 0:
            board.place_number(cell.sketehced_value)
        else:
            break


#Game Over Screen
g_over = (Board.FONT).render('Game Over:(', 0, Board.BLACK)
g_over_rect = g_over.get_rect(center=(297, 150))
screen.blit(g_over, g_over_rect)
rstart_diff = Board.FONT.render('Restart', 0, Board.BLACK)
rstart_rect = rstart_diff.get_rect(center=(300, 420))
pygame.draw.rect(screen, (255, 165, 0), (475 / 2, 400, 125, 40))
screen.blit(rstart_diff, rstart_rect)

#Game Won Screen
g_won = (Board.FONT).render('Game Won!', 0, Board.BLACK)
g_won_rect = g_won.get_rect(center=(297, 150))
screen.blit(g_won, g_won_rect)
exit_diff = Board.FONT.render('Exit', 0, Board.BLACK)
exit_rect = exit_diff.get_rect(center=(300, 420))
pygame.draw.rect(screen, (255, 165, 0), (475 / 2, 400, 125, 40))
screen.blit(exit_diff, exit_rect)



'''
