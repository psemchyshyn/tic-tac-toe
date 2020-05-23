'''Main module for deploying the game'''

import re

from btree import Btree, minimax
from board import Board
from itertools import cycle

class Game:
    '''Represents Game class for Tic Tac Toe'''
    REAL_PLAYER = "X"
    COMPUTER_PLAYER = "O"

    def __init__(self):
        '''Initializes Game object'''
        self.board = Board()

    def make_move(self, pos, player):
        '''Make move in the game'''
        self.board.set_move(pos, player)

    def get_computer_move(self):
        '''Calculates computer move'''
        tree = Btree(self.board)
        computer_move = tree.find_best_move()
        return computer_move

    def input_user_move(self):
        '''
        Provides real player input
        '''
        while True:
            real_player_move = input("Make your move: ")
            if re.fullmatch(r"[012] [012]", real_player_move):
                position = list(map(int, real_player_move.split()))
                if self.board.is_position_available(position):
                    return position
                else:
                    print("Position incorrect. It is already taken")
            else:
                print("Position incorrect. It doesn't exist")
            print("Please, type it again")

    def run(self):
        '''
        Runs tic tac toe
        '''
        print("Game started!")
        players = cycle((self.REAL_PLAYER, self.COMPUTER_PLAYER))
        while True:
            player = next(players)
            # Process real player move
            if player == self.REAL_PLAYER:
                move = self.input_user_move()
                print("You made your move")
            # Work with computer move
            else:
                move = self.get_computer_move()
                print("Computer made its move")
            self.make_move(move, player)
            print(self.board)

            # Check possible outcomes
            if self.board.check_for_winning() == "win":
                print(f"{player} won!")
                break
            if self.board.check_for_winning() == "draw":
                print("Draw")
                break
        print("Game finished!")



if __name__ == "__main__":
    game = Game()
    game.run()

