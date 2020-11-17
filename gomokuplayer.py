#!/usr/bin/env python
BLACK = 0
WHITE = 1
alpha_index = 'abcdefghijklmnopqrs'

class board():
    #initializes an empty board
    def __init__(self):
        self.board = [[[] for i in range(0,20)] for j in range(0,20)]

    #return the current board
    def get_board(self):
        return self.board

    #draw the current board
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

    #add a stone of the given colour to the given position 
    def add_stone(self,position,colour):
        row = alpha_index.index(position[:1])
        col = int(position[1:]) - 1
        if colour == BLACK:
            self.board[row][col].append(BLACK)
        elif colour == WHITE:
            self.board[row][col].append(WHITE)

    #checks if the given position is empty
    def check_empty(self,position):
        row = alpha_index.index(position[:1])
        col = int(position[1:]) - 1
        if not self.board[row][col]:
            return True
        else:
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
        if self.turn == BLACK:
            return "BLACK"
        elif self.turn == WHITE:
            return "WHITE"

    #update the board if a player makes a move
    def update_board(self, position):
        if self.board.check_empty(position):
            self.board.add_stone(position, self.turn)
            if self.turn == BLACK:
                self.turn = WHITE
            elif self.turn == WHITE:
                self.turn = BLACK
            return True
        else:
            return False


    
def main():
    b = board()
    p = play(b)
    while not p.check_end():
        p.board.draw_board()

        player_input = input("This is " + p.check_turn() +"'s turn. Enter position to play: ")
        try:
            if (2 > len(player_input) > 3) or (player_input[:1] not in alpha_index) or  (1 > int(player_input[1:])) or (int(player_input[1:]) > 19):
                print("\nWrong input. Please try another position.\n") 
                continue
        except ValueError:
            print("\nWrong input. Please try another position.\n")
            continue
        if not p.update_board(player_input):
            print("\nA stone was played at the position. Please try another position.\n")

if __name__ == '__main__':
    main()