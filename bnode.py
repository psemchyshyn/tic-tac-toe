'''
Contains the Node class for binary tree
'''

class BNode:
    '''Represents node'''

    __slots__ = "state", "left", "right"

    def __init__(self, state, left=None, right=None):
        '''Initializes the node'''
        self.state = state
        self.left = left
        self.right = right
