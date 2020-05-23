'''
Module for storing the board method
'''

import random
import copy

class Board:
    '''Represents the board class'''
    def __init__(self):
        '''
        Initializees the board with current state
        '''
        self.state = [[" " for ind1 in range(3)] for ind2 in range(3)]
        self.last_position = None
        self.last_symbol = None


    def check_for_winning(self):
        '''Checks the board for winning position'''
        if any(set(row) == {self.last_symbol} for row in self.state) or \
        any(set(col) == {self.last_symbol} for col in zip(*self.state)) or \
        self.state[0][0] == self.state[1][1] == self.state[2][2] != " " or \
        self.state[2][0] == self.state[1][1] == self.state[0][2]!= " " :
            return "win"
        elif self.is_full():
            return "draw"
        else:
            return "continue"

    def get_free_positions(self):
        '''
        Gets all free positions to make a move on the 
        board
        '''
        available_positions = []
        for row_ind, row in enumerate(self.state):
            for col_ind, element in enumerate(row):
                if element == " ":
                    available_positions.append((row_ind, col_ind))
        return available_positions

    def is_full(self):
        '''
        Checks if there are any available positions
        '''
        return self.get_free_positions() == []

    def is_position_available(self, pos):
        '''Checks if current position is available'''
        assert len(pos) == 2, "Invalid pos input"
        assert pos[0] in range(3) or pos[1] in range(3), \
         "Index of pos input is out of table range"
        return self.state[pos[0]][pos[1]] == " "

    def set_move(self, pos, symbol):
        '''Sets a move to pos if is available'''
        if self.is_position_available(pos):
            self.state[pos[0]][pos[1]] = symbol
            self.last_symbol = symbol

    def clear_move(self, pos):
        '''
        Clears the player move
        '''
        if not self.is_position_available(pos):
            self.state[pos[0]][pos[1]] = " "
            if self.last_symbol == "X":
                self.last_symbol = "O"
            else:
                self.last_symbol = "X"

    def get_random_move(self, symbol):
        '''
        Gets a random move from availble ones and returns
        a board with this move entered
        '''
        possible_moves = self.get_free_positions()
        try:
            rnd_move = random.choice(possible_moves)
        except IndexError:
            return

        # Copying a board and adding a randomly chosen move to it
        new_board = copy.deepcopy(self)
        new_board.set_move(rnd_move, symbol)
        return new_board


    def __str__(self):
        '''String representation of board object'''
        string = ''
        for row in self.state:
            for element in row:
                string += element
            string += "\n"
        return string

# a = Board()
# a.set_move((1, 1), "X")
# a.set_move((1, 0), "Y")
# a.set_move((0, 0), "X")
# print(a)

