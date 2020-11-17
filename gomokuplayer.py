#!/usr/bin/env python

class board():
    def __init__(self):
        self.board = [[[] for i in range(0,20)] for j in range(0,20)]
    
    def get_board(self):
        return self.board

    def draw_board(self):
        print('  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19')
        alpha_index = 'abcdefghijklmnopqrs'
        for index in alpha_index:
            print(index, end=' ')
            for i in range(0,18):
                if i != 17:
                    print('  ―', end=' ')
                else: 
                    print('  ―')
            if index != alpha_index[-1]:
                print('  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |')

def main():
    b = board()
    b.draw_board()
if __name__ == '__main__':
    main()