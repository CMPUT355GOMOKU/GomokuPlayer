import pygame, tkinter as tk
from tkinter import simpledialog


#!/usr/bin/env python
BLACK = 0
WHITE = 1

LEFT = 0
TOPLEFT = 1
TOP = 2
TOPRIGHT = 3
RIGHT = 4
BOTTOMRIGHT = 5
BOTTOM = 6
BOTTOMLEFT = 7
alpha_index = 'abcdefghijklmnopqrs'

class board():
    #initializes an empty board
    def __init__(self):
        self.board = [[[] for i in range(0,20)] for j in range(0,20)]
        self.cell_size = 800/19
        self.num_rows = 19

    #returns the current board
    def get_board(self):
        return self.board

    #prints out the current board
    def draw_board(self, screen):
        pygame.init()
        font = pygame.font.Font('CONSOLA.TTF', 21)
        increment = self.cell_size
        pygame.draw.rect(screen, (185, 122, 87), [0,0, 1000, 1000], 0)

        for row in range(self.num_rows):
            text = font.render(str(row+1), 1, (0, 0, 0))
            screen.blit(text, (((95 + self.cell_size) + ((increment - 0.5) * row)), 100))
            y = (row + 1) * (800 / 19)
            pygame.draw.line(screen, (0, 0, 0), [100 + self.cell_size, y + 100], [900, y + 100], 2)

        for col in range(self.num_rows):
            text = font.render(str(alpha_index[col]), 1, (0, 0, 0))
            screen.blit(text, (100,(90 + self.cell_size) + ((increment) * col)))
            x = (col + 1) * (800 / 19)
            pygame.draw.line(screen, (0, 0, 0), [x + 100, 100 + self.cell_size], [x + 100, 900], 2)

        for row in range(self.num_rows):
            for col in range(self.num_rows):
                if self.board[row][col]:
                    if self.board[row][col][0] == BLACK:
                        color = (0, 0, 0)
                    else:
                        color = (255, 255, 255)
                    x = col * self.cell_size + 100 + self.cell_size
                    y = row * self.cell_size + 100 + self.cell_size
                    pygame.draw.circle(screen, color, [x,y], 17)

    #returns row index and column index of the given position
    def get_row_col(self,position):
        row = alpha_index.index(position[:1])
        col = int(position[1:]) - 1
        return row,col

    #add a stone of the given colour to the given position 
    def add_stone(self,position,colour):
        row,col = self.get_row_col(position)
        if colour == BLACK:
            self.board[row][col].append(BLACK)
        elif colour == WHITE:
            self.board[row][col].append(WHITE)

    #checks if the given position is empty
    def check_empty(self,position):
        row,col = self.get_row_col(position)
        if not self.board[row][col]:
            return True
        else:
            return False
    #checks if the board is full
    def check_full(self):
        for row_index in range(len(self.board)):
            for col_index in range(len(self.board[row_index])):
                if not self.board[row_index][col_index]:
                    return False
        return True
    
    #checks if there are 5 or more horizontally connected stones of given colour from given position.
    def horizontal_line(self,position,colour):
        row,col = self.get_row_col(position)
        left_connection = self.find_connection(position,colour,LEFT)
        right_connection = self.find_connection(position,colour,RIGHT)
        connection = 1 + left_connection + right_connection
        if connection >= 5:
            return True
        return False

    #checks if there are 5 or more vertically connected stones of given colour from given position.
    def vertical_line(self,position,colour):
        row,col = self.get_row_col(position)
        top_connection = self.find_connection(position,colour,TOP)
        bottom_connection = self.find_connection(position,colour,BOTTOM)
        connection = 1 + top_connection + bottom_connection
        if connection >= 5:
            return True
        return False 

    #checks if there are 5 or more diagonally connected stones of given colour from given position.
    def diagonal_line(self,position,colour):
        row,col = self.get_row_col(position)
        topleft_connection = self.find_connection(position,colour,TOPLEFT)
        topright_connection = self.find_connection(position,colour,TOPRIGHT)
        bottomleft_connection = self.find_connection(position,colour,BOTTOMLEFT)
        bottomright_connection = self.find_connection(position,colour,BOTTOMRIGHT)
        topleft_bottomright_connection = 1 + topleft_connection + bottomright_connection
        topright_bottomleft_connection = 1 + topright_connection + bottomleft_connection
        if topleft_bottomright_connection >= 5 or topright_bottomleft_connection >= 5:
            return True
        return False 

    #for given direction, find number of consecutive stones of given colour 
    def find_connection(self,position,colour, direction):
        row,col = self.get_row_col(position)
        connection = 0
        ith = 1
        while True:
            if direction == LEFT:
                if col - ith >= 0:
                    if self.board[row][col-ith]:
                        if self.board[row][col-ith][0] == colour:
                            connection += 1 
                        else:
                            break
                    else:
                        break
                else:
                    break
            if direction == RIGHT:
                if col + ith >= 0:
                    if self.board[row][col+ith]:
                        if self.board[row][col+ith][0] == colour:
                            connection += 1 
                        else:
                            break
                    else:
                        break
                else:
                    break
            if direction == TOP:
                if row - ith >= 0:
                    if self.board[row-ith][col]:
                        if self.board[row-ith][col][0] == colour:
                            connection += 1 
                        else:
                            break
                    else:
                        break
                else:
                    break
            if direction == BOTTOM:
                if row + ith >= 0:
                    if self.board[row+ith][col]:
                        if self.board[row+ith][col][0] == colour:
                            connection += 1 
                        else:
                            break
                    else:
                        break
                else:
                    break
            if direction == TOPLEFT:
                if row - ith >= 0 and col - ith >= 0:
                    if self.board[row-ith][col-ith]:
                        if self.board[row-ith][col-ith][0] == colour:
                            connection += 1 
                        else:
                            break
                    else:
                        break
                else:
                    break
            if direction == TOPRIGHT:
                if row - ith >= 0 and col + ith < 20:
                    if self.board[row-ith][col+ith]:
                        if self.board[row-ith][col+ith][0] == colour:
                            connection += 1 
                        else:
                            break
                    else:
                        break
                else:
                    break
            if direction == BOTTOMLEFT:
                if row + ith < 20 and col - ith >= 0:
                    if self.board[row+ith][col-ith]:
                        if self.board[row+ith][col-ith][0] == colour:
                            connection += 1
                        else:
                            break
                    else:
                        break
                else:
                    break
            if direction == BOTTOMRIGHT:
                if row + ith < 20 and col + ith < 20:
                    if self.board[row+ith][col+ith]:
                        if self.board[row+ith][col+ith][0] == colour:
                            connection += 1
                        else:
                            break
                    else:
                        break
                else:
                    break
            ith += 1
        return connection


class play(board):
    #initializes the starting state
    def __init__(self,board):
        self.board = board
        self.turn = BLACK
        self.end = False

    #checks if game ended
    def check_end(self):
        return self.end

    #checks whos turn it is currently
    def check_turn(self):
        return self.turn

    #returns string of turn
    def str_turn(self):
        if self.turn == BLACK:
            return "BLACK"
        elif self.turn == WHITE:
            return "WHITE"

    #updates the board if a player makes a move
    def update_board(self,position):
        if self.board.check_empty(position):
            self.board.add_stone(position, self.turn)
            return True
        else:
            return False

    #changes the current turn to the other colour.
    def switch_turn(self):
        if self.turn == BLACK:
            self.turn = WHITE
        elif self.turn == WHITE:
            self.turn = BLACK

    #checks if a player has won.
    def check_win(self,position,colour):
        if self.board.horizontal_line(position,colour) or self.board.vertical_line(position,colour) or self.board.diagonal_line(position,colour):
            self.end = True
            return True
        return False

    #checks if the board is full
    def check_full(self):
        if self.board.check_full():
            self.end = True
            return True
        else:
            return False



def main():
    b = board()
    p = play(b)
    #white, black = 0, 0
    #continueGame = True

    while True:
        numPlayers = input("Type 1 for PvC or Type 2 for PvP: ")
        if numPlayers == "1" or numPlayers == "2":
            break
        print("Invalid input, Please try again.")
    if numPlayers == "1":
        print("not implemented yet :P")
        return False

    while True:
        if numPlayers == "1":
            startas = input("Would you like to start as black? or white?").upper()
            if startas == "WHITE":
                p.switch_turn()
                break
            elif player_colour == "BLACK":
                break
            else:
                print("\nInvalid input. Please try another position.\n")
                continue
        else:
            break

    pygame.init()
    screen = pygame.display.set_mode((1000,1000))
    white = (255, 255, 255)
    board_color = (185, 122, 87)
    black = (0, 0, 0)
    drawBoard(p, screen)
    ROOT = tk.Tk()
    ROOT.withdraw()
    gameOver = False

    while not gameOver:
        if numPlayers == "2":
            updateGame(p)
            player_input = simpledialog.askstring(title= p.str_turn() +"'s turn.", prompt="Enter a position to play (ex:a1)")
            turn = p.check_turn()
            try:
                if (2 > len(player_input) > 3) or (player_input[:1] not in alpha_index) or (1 > int(player_input[1:])) or (int(player_input[1:]) > 19):
                    tk.messagebox.showerror(title="Wrong input", message="Please try another position.")
                    continue
            except ValueError:
                tk.messagebox.showerror(title="Wrong input", message="Please try another position.")
                continue
            if not p.update_board(player_input):
                tk.messagebox.showerror(title="wrong input", message="A stone was already placed at that position")
                continue
            drawBoard(p, screen)
            if p.check_win(player_input, turn):
                tk.messagebox.showinfo(title="Victory!", message = p.str_turn() + " HAS WON!")
            elif p.check_full():
                tk.messagebox.showinfo(title="Draw", message="Nobody won")
            p.switch_turn()
            gameOver = p.check_end()
        if gameOver:
            replay = tk.messagebox.askquestion(title="Play again?", message="Would you like to play again?").upper()
            if replay == "YES":
                pygame.display.quit()
                main()
                gameOver = False

    pygame.display.quit()
    pygame.quit()

def updateGame(game):
    gameOver = False
    for position in pygame.event.get():
        if position.type == pygame.QUIT:
            gameOver = True
            pygame.quit()
    return gameOver


def drawBoard(game, screen):

    game.board.draw_board(screen)
    font = pygame.font.Font('CONSOLA.TTF', 30)
    text = font.render("Made by Gomovis", 1, (0, 0, 0))
    screen.blit(text, (650,50))
    #scoreText = font.render("Scores\n{}".format('-'* 40) + "\nWhite: {}\nBlack: {}\n\n".format(white, black))
    #screen.blit(scoreText, (150, 50))


    pygame.display.update()
    return game.check_end()
    

'''def main():

    white, black = 0, 0
    continueGame = True
    pygame.init()

    while continueGame:
        win = game()
        
        if win == "WHITE":
            white += 1
        elif win == "BLACK":
            black += 1
        text = font.render("Scores\n{}".format('-'*40) + "\nWhite: {}\nBlack: {}\n".format(white,black), 1, (0, 0, 0))
        screen.blit(text, (50, 50))

    while True:        
        replay = tk.messagebox.askquestion(title="Game Over!", message="Would you like to start a \nnew game of Gomoku? ('yes' or 'no'): ").upper()
        if replay == 'YES' or replay == 'NO':
            break
    if replay == "NO":
        continueGame = False'''

            
if __name__ == '__main__':
    main()
