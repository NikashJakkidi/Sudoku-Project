import sys

from Board import Board
from sudoku_generator import generate_sudoku
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
            x,y = event.pos
            print(event.pos)
            if y > 400 and y < 440:
                if x > 50 and x < 175:
                    difficulty = 'easy'
                    selected_difficulty = True
                    break
                elif x > 475/2 and x < 475/2 + 125:
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
board = Board(9, 9,screen,  difficulty)
board.draw()

pygame.time.wait(5000)
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

#reset, restart, and quit buttons(location needs to be changed)
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
pygame.time.wait(10000)





#reset, restart, and quit buttons(location needs to be changed)
    #reset = Board.FONT.render('RESET', 0, Board.BLACK)
    #reset_rect = reset.get_rect(center=(110, 420))
    #pygame.draw.rect(screen, (255, 165, 0), (50, 400, 125, 40))
    #screen.blit(reset, reset_rect)

    #restart = Board.FONT.render('MEDIUM', 0, Board.BLACK)
    #restart_rect = restart.get_rect(center=(300, 420))
    #pygame.draw.rect(screen, (255, 165, 0), (475 / 2, 400, 125, 40))
    #screen.blit(restart, restart_rect)

    #quit = Board.FONT.render('HARD', 0, Board.BLACK)
    #quit_rect = third_diff.get_rect(center=(485, 420))
    #pygame.draw.rect(screen, (255, 165, 0), (425, 400, 125, 40))
    #screen.blit(quit, quit_rect)
'''
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