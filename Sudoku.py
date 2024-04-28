import sys
from Board import Board
from sudoku_generator import generate_sudoku
from Cell import Cell
import pygame
pygame.init()

screen = pygame.display.set_mode((Board.SCREEN_WIDTH, Board.SCREEN_HEIGHT + 100))

main_screen = False
game_win_screen = False
game_over_screen = False

selected_difficulty = False
difficulty = ''
removed_cells = 0

board_array = None
board = None

def get_box_pos(pos):
    x, y, = pos
    row = x // Cell.CELL_SIZE
    col = y // Cell.CELL_SIZE
    return row, col
def create_main_screen():
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
    easy_button = pygame.Rect((50, 400, 125, 40))
    screen.blit(first_diff, first_rect)

    second_diff = Board.FONT.render('MEDIUM', 0, Board.BLACK)
    second_rect = second_diff.get_rect(center=(300, 420))
    pygame.draw.rect(screen, (255, 165, 0), (475 / 2, 400, 125, 40))
    medium_button = pygame.Rect((475 / 2, 400, 125, 40))
    screen.blit(second_diff, second_rect)

    third_diff = Board.FONT.render('HARD', 0, Board.BLACK)
    third_rect = third_diff.get_rect(center=(485, 420))
    pygame.draw.rect(screen, (255, 165, 0), (425, 400, 125, 40))
    hard_button = pygame.Rect((425, 400, 125, 40))
    screen.blit(third_diff, third_rect)
    pygame.display.update()

    return easy_button, medium_button, hard_button

def create_game_win_screen(screen):
    g_won = (Board.FONT).render('Game Won!', 0, Board.BLACK)
    g_won_rect = g_won.get_rect(center=(297, 150))
    screen.blit(g_won, g_won_rect)
    exit_diff = Board.FONT.render('Exit', 0, Board.BLACK)
    exit_rect = exit_diff.get_rect(center=(300, 420))
    pygame.draw.rect(screen, (255, 165, 0), (475 / 2, 400, 125, 40))
    screen.blit(exit_diff, exit_rect)

def create_game_over_screen(screen):
    g_over = (Board.FONT).render('Game Over:(', 0, Board.BLACK)
    g_over_rect = g_over.get_rect(center=(297, 150))
    screen.blit(g_over, g_over_rect)

def add_in_game_buttons(screen):
    reset = Board.FONT.render('RESET', 0, Board.BLACK)
    reset_rect = reset.get_rect(center=(110, 650))
    pygame.draw.rect(screen, (255, 165, 0), (50, 630, 125, 40))
    reset_button = pygame.Rect((50, 630, 125, 40))
    screen.blit(reset, reset_rect)

    restart = Board.FONT.render('RESTART', 0, Board.BLACK)
    restart_rect = restart.get_rect(center=(300, 650))
    pygame.draw.rect(screen, (255, 165, 0), (475 / 2, 630, 125, 40))
    restart_button = pygame.Rect((475 / 2, 630, 125, 40))
    screen.blit(restart, restart_rect)

    quit = Board.FONT.render('QUIT', 0, Board.BLACK)
    quit_rect = quit.get_rect(center=(485, 650))
    pygame.draw.rect(screen, (255, 165, 0), (425, 630, 125, 40))
    quit_button = pygame.Rect((425, 630, 125, 40))
    screen.blit(quit, quit_rect)

    return reset_button, restart_button, quit_button
def difficulty_to_removed_cells(difficulty):
    if difficulty == 'easy':
        removed_cells = 30
    elif difficulty == 'medium':
        removed_cells = 40
    elif difficulty == 'hard':
        removed_cells = 50
    else:
        return None
    return removed_cells

def check_if_finished(board_array):
    for i in range(len(board_array)):
        for j in range(len(board_array[i])):
            if board_array[i][j] == 0:
                return False
    return True

def check_if_winner(board, row, col):
    if board.valid_row(row) == True and board.valid_col(col) == True and board.valid_box(row, col) == True:
        return True
    return False

main_screen = True
reset_command = False
sketch_mode = True
finished_game = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
        if main_screen == True:
            if reset_command == False:
                easy_rect, medium_rect, hard_rect = create_main_screen()
            if event.type == pygame.MOUSEBUTTONDOWN or reset_command == True:
                if easy_rect.collidepoint(pygame.mouse.get_pos()):
                    difficulty = 'easy'
                    selected_difficulty = True
                    board = Board(9, 9, screen, difficulty)
                    print('chicken')
                elif medium_rect.collidepoint(pygame.mouse.get_pos()):
                    difficulty = 'medium'
                    selected_difficulty = True
                    board = Board(9, 9, screen, difficulty)
                    print('chicken1')
                elif hard_rect.collidepoint(pygame.mouse.get_pos()):
                    difficulty = 'hard'
                    selected_difficulty = True
                    board = Board(9, 9, screen, difficulty)
                    board.draw()
                    print('chicken2')
                if selected_difficulty == True:
                    print('Tick')
                    board.draw()
                    removed_cells = difficulty_to_removed_cells(difficulty)
                    board_array = generate_sudoku(9, removed_cells)
                    for i in range(len(board_array)):
                        for j in range(len(board_array[i])):
                            cell = Cell(board_array[i][j], i, j, screen)
                            if board_array[i][j] != 0:
                                cell.draw()
                    reset_button, restart_button, quit_button = add_in_game_buttons(screen)
                    pygame.display.update()
                    main_screen = False
                    reset_command = False
        if main_screen == False and game_win_screen == False and game_over_screen == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_button.collidepoint(pygame.mouse.get_pos()):
                    reset_command = True
                    main_screen = True
                    continue
                elif restart_button.collidepoint(pygame.mouse.get_pos()):
                    main_screen = True
                    continue
                elif quit_button.collidepoint(pygame.mouse.get_pos()):
                    game_over_screen = True
                    continue
                # if event.button == 1:
                else:
                    click_pos = pygame.mouse.get_pos()
                    box_row, box_col = get_box_pos(click_pos)
                    cell = Cell(board_array[box_row][box_col], box_row, box_col, screen)
                    cell.selected = True
                    cell.draw()
                    print(str(box_row) + " " + str(box_col))
                    board.select(box_row, box_col)
                    pygame.display.update()
            if event.type == pygame.KEYDOWN and sketch_mode == True:
                print("Key")
                if event.key == pygame.K_1:
                    cell.set_sketched_value(1)
                    board.sketch(1)
                    cell.draw()
                    pygame.display.update()
                elif event.key == pygame.K_2:
                    cell.set_sketched_value(2)
                    board.sketch(2)
                    cell.draw()
                    pygame.display.update()
                elif event.key == pygame.K_3:
                    cell.set_sketched_value(3)
                    board.sketch(3)
                    cell.draw()
                    pygame.display.update()
                elif event.key == pygame.K_4:
                    cell.set_sketched_value(4)
                    board.sketch(4)
                    cell.draw()
                    pygame.display.update()
                elif event.key == pygame.K_5:
                    cell.set_sketched_value(5)
                    board.sketch(5)
                    cell.draw()
                    pygame.display.update()
                elif event.key == pygame.K_6:
                    cell.set_sketched_value(6)
                    board.sketch(6)
                    cell.draw()
                    pygame.display.update()
                elif event.key == pygame.K_7:
                    cell.set_sketched_value(7)
                    board.sketch(7)
                    cell.draw()
                    pygame.display.update()
                elif event.key == pygame.K_8:
                    cell.set_sketched_value(8)
                    board.sketch(8)
                    cell.draw()
                    pygame.display.update()
                elif event.key == pygame.K_9:
                    cell.set_sketched_value(9)
                    board.sketch(9)
                    cell.draw()
                    pygame.display.update()
                sketch_mode = False
            if event.type == pygame.KEYDOWN and sketch_mode == False:
                print('J')
                if event.key == pygame.K_RETURN:
                    print('K')
                    if cell.sketched_value != 0:
                        print('I')
                        board.place_number(cell.sketched_value)
                        cell.set_cell_value(cell.sketched_value)
                        board_array[box_row][box_col] = cell.value
                        for i in range(len(board_array)):
                            for j in range(len(board_array[i])):
                                cell = Cell(board_array[i][j], i, j, screen)
                                if board_array[i][j] != 0:
                                    cell.draw()
                        if check_if_finished(board_array) == True:
                            if check_if_winner(board, box_row, box_col) == True:
                                screen.fill(Board.CREAM)
                                create_game_win_screen(screen)
                                pygame.display.update()
                            else:
                                screen.fill(Board.CREAM)
                                create_game_over_screen(screen)
                                pygame.display.update()
                                pygame.QUIT

                    cell.selected = False
                    pygame.display.update()
                sketch_mode = True
                continue
        if game_over_screen == True:
            screen.fill(Board.CREAM)
            create_game_over_screen(screen)
            pygame.display.update()
            pygame.QUIT
