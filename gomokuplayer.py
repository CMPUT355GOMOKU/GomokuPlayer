#!/usr/bin/env python
BLACK = 0
WHITE = 1
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
                    print(' ', end='')
                if col_index < 17:
                    print(' ―', end=' ')
                elif col_index == 17: 
                    print(' ―')
            if row_index != 18:
                print(' |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |')
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

    def horizontal_line(self,position,colour):
        row,col = self.get_row_col(position)
        connection = 1
        for ith in range(1,5):
            if col + ith < 20:
                if self.board[row][col+ith]:
                    if self.board[row][col+ith][0] == colour:
                        connection += 1
            if col - ith >= 0:
                if self.board[row][col-ith]:
                    if self.board[row][col-ith][0] == colour:
                        connection +=1
        if connection >= 5:
            return True
        return False

    def vertical_line(self,position,colour):
        row,col = self.get_row_col(position)
        connection = 1
        for ith in range(1,5):
            if row + ith < 20:
                if self.board[row+ith][col]:
                    if self.board[row+ith][col][0] == colour:
                        connection += 1
            if row - ith >= 0:
                if self.board[row-ith][col]:
                    if self.board[row-ith][col][0] == colour:
                        connection +=1
        if connection >= 5:
            return True
        return False 

    def diagonal_line(self,position,colour):
        row,col = self.get_row_col(position)
        connection = 1
        for ith in range(1,5):
            if row - ith >= 0 and col + ith < 20:
                if self.board[row-ith][col+ith]:
                    if self.board[row-ith][col+ith][0] == colour:
                        connection += 1
            if row + ith < 20 and col - ith >= 0:
                if self.board[row+ith][col-ith]:
                    if self.board[row+ith][col-ith][0] == colour:
                        connection +=1
            if row - ith >= 0 and col - ith >= 0:
                if self.board[row-ith][col-ith]:
                    if self.board[row-ith][col-ith][0] == colour:
                        connection += 1
            if row + ith < 20 and col + ith < 20:
                if self.board[row+ith][col+ith]:
                    if self.board[row+ith][col+ith][0] == colour:
                        connection +=1
        if connection >= 5:
            return True
        return False              

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

    #update the board if a player makes a move
    def update_board(self,position):
        if self.board.check_empty(position):
            self.board.add_stone(position, self.turn)
            return True
        else:
            return False

    def switch_turn(self):
        if self.turn == BLACK:
            self.turn = WHITE
        elif self.turn == WHITE:
            self.turn = BLACK

    def check_win(self,position,colour):
        if self.board.horizontal_line(position,colour) or self.board.vertical_line(position,colour) or self.board.diagonal_line(position,colour):
            self.end = True
            return True
        return False


    
def main():
    b = board()
    p = play(b)
    p.board.draw_board()
    while not p.check_end():
        player_input = input("This is " + p.str_turn() +"'s turn. Enter position to play: ")
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
        p.switch_turn()
        

if __name__ == '__main__':
    main()
