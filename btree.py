'''
Binary tree / minimax algorithm
'''

import random

from board import Board
from bnode import BNode


class Btree:
    MAXIMIXER = 1
    DRAW = 0
    MINIMIZER = -1

    def __init__(self, board):
        '''Initializes binary tree'''
        self._root = BNode(board)

    def find_best_move(self):
        '''
        Finds the best move for computer player
        '''
        best_move = None
        case_move = 1
        # Traversing through all positions applying minimax algorithm to each one of them
        for move in self._root.state.get_free_positions():
            self._root.state.set_move(move, "X")
            score = minimax(self._root)
            if score < case_move:
                case_move = score
                best_move = move
            self._root.state.clear_move(move)
        return best_move


def minimax(root, play=Btree.MAXIMIXER):
    # Check condition for finishing tree deploying
    if root.state.check_for_winning() == "win":
        return -play
    elif root.state.check_for_winning() == "draw":
        return Btree.DRAW

    # bulid a tree depending on whose move it is
    # Maximizer is a real player(X)
    # Minimizer is a computer(O)

    if play == Btree.MAXIMIXER:
        # Maximizer is trying to get the highest score
        optimal_move = Btree.MINIMIZER
        
        new_state = root.state.get_random_move("O")
        root.left = BNode(new_state)
        optimal_move = max(optimal_move, minimax(root.left, play=Btree.MINIMIZER))

        if not new_state.is_full():
            new_state = new_state.get_random_move("O")
            root.right = BNode(new_state)
            optimal_move = max(optimal_move, minimax(root.right, play=Btree.MINIMIZER))
        return optimal_move
    else:
        # Minimizer is trying to get the lowest score
        optimal_move = Btree.MAXIMIXER

        new_state = root.state.get_random_move("X")
        root.left = BNode(new_state)
        optimal_move = min(optimal_move, minimax(root.left, play=Btree.MAXIMIXER))

        if not new_state.is_full():
            new_state = new_state.get_random_move("X")
            root.right = BNode(new_state)
            optimal_move = min(optimal_move, minimax(root.right, play=Btree.MAXIMIXER))
        return optimal_move

