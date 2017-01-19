"""
http://www.codeskulptor.org/#user42_7LnciyWt61_18.py
100/100

Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = list(configuration)
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        temp = list(self._board)
        temp.reverse()
        return str(temp)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        if len(self._board)>1:
            for index in range(1, len(self._board)):
                if self._board[index]!=0:
                    return False
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        is_legal = False
        if house_num > 0 and self._board[house_num]==house_num:
            is_legal = True
        return is_legal

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            for index in range(house_num+1):
                self._board[index]+=1
            self._board[house_num] = 0

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for index in range(0,len(self._board)):
            if self.is_legal_move(index):
                return index
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        temp_board = SolitaireMancala()
        temp_board.set_board(list(self._board))
        moves = []
        next_move = temp_board.choose_move()
        while next_move != 0:
            moves.append(next_move)
            temp_board.apply_move(next_move)
            next_move = temp_board.choose_move()
        return moves





#import poc_mancala_gui 
#poc_mancala_gui.run_gui(SolitaireMancala()) 
# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())
