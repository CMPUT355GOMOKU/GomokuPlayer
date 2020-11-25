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

    #returns the current board
    def get_board(self):
        return self.board

    #prints out the current board
    def draw_board(self):
        print('  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19')
        for row_index in range(0,19):
            print(alpha_index[row_index], end=' ')
            for col_index in range(0,19):
                if self.board[row_index][col_index]:
                    if self.board[row_index][col_index][0] == BLACK:
                        print('O', end='')
                    elif self.board[row_index][col_index][0] == WHITE:
                        print('X',end='')
                else:
                    print('', end=' ')
                if col_index < 18:
                    print(' ―', end=' ')
                elif col_index == 18:
                    print('')
            if row_index != 18:
                print('  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |')
        print("\n")

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
    p.board.draw_board()

    while True:
        numPlayers = input("type 1 for PvC or type 2 for PvP: ")
        if numPlayers == "1" or numPlayers == "2":
            break
        print("Wrong input. Please try again")

    while True:
        if numPlayers == "1":
            player_colour = input("Would you like to start as black? or white?").upper()        
            if player_colour == "WHITE":
                p.switch_turn()
                break
            elif player_colour == "BLACK":
                break
            else:
                print("\nWrong input. Please try another position.\n")
                continue
        else:
            break

    while not p.check_end():
        if numPlayers == "2":
            
            player_input = input("This is " + p.str_turn() +"'s turn. Enter position to play (Ex.: a1) : ")
            turn = p.check_turn()
            try:
                if (2 > len(player_input) > 3) or (player_input[:1] not in alpha_index) or  (1 > int(player_input[1:])) or (int(player_input[1:]) > 19):
                    print("\nWrong input. Please try another position.\n") 
                    continue
            except ValueError:
                print("\nWrong input. Please try another position.\n")
                continue
            if not p.update_board(player_input):
                print("\nA stone was played at the position. Please try another position.\n")
                continue
            p.board.draw_board()
            if p.check_win(player_input,turn):
                print(p.str_turn() + " HAS WON!")
            elif p.check_full():
                print("Draw")
            p.switch_turn()

        elif numPlayers == "1":
            print("not implemented yet :P")
            break

if __name__ == '__main__':
    main()