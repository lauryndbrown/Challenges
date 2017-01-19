"""
Clone of 2048 game.
"""

import random
import poc_2048_gui
import user42_aDyFDtXrpu_5 as poc_2048_testsuite
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}
OFFSETS2 = {UP: (-1, 0),
           DOWN: (1, 0),
           LEFT: (0, -1),
           RIGHT: (0, 1)}
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    pass
    

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    EMPTY = 0
    
    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.grid = [[ 0 for dummy_i in range(self.width)] for dummy_j in range(self.height)]
        self.empty_pos = [ (row, col) for row in range(self.height) for col in range(self.width) ]
        
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col] = 0
        self.empty_pos = [ (row, col) for row in range(self.height) for col in range(self.width) ]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_string = ""
        for row in self.grid:
            grid_string+=str(row)+"\n"
        return grid_string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        grid_changed = self.shift(direction)
        merge_result = self.merge(direction)
        grid_changed = merge_result or grid_changed
        if merge_result:
            self.shift(direction)
        if grid_changed:
            self.new_tile()
            
    def shift(self, direction):
        """
        Helper function that shifts all tiles in the given direction
        """
        grid_changed = False
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col]!=self.EMPTY:
                    tile_moved = self.shift_helper(row, col, direction)
                    if tile_moved==True:
                        grid_changed = True
        return grid_changed
           

    def shift_helper(self, row, col, direction):
        """
         Helper for move function
        """
        offset = OFFSETS2[direction]
        next_row = row+offset[0]
        next_col = col+offset[1]
        merged_before = False
        while self.is_in_bounds(next_row, next_col):
            if self.grid[next_row][next_col]!=self.EMPTY:
                break
            next_row+=offset[0]
            next_col+=offset[1]
        row_index = next_row-offset[0]
        col_index = next_col-offset[1]
        tile_moved = (row!=row_index or col!=col_index)
        if tile_moved:
            self.set_tile(row_index, col_index, self.grid[row][col])
            self.set_tile(row, col, self.EMPTY)
        return  tile_moved  
    
    def merge(self, direction):
        offset = OFFSETS2[direction]
        next_row = row+offset[0]
        next_col = col+offset[1]
        merged_before = False
        while self.is_in_bounds(next_row, next_col):
            next_value = self.grid[next_row][next_col]
            old_value = self.grid[row][col]
            if next_value==old_value and merged_before==False:
                self.set_tile(old_row, old_col, self.grid[old_row][old_col]*2)
                self.set_tile(next_row, next_col, self.EMPTY)   
                merged_before=True
            if self.grid[next_row][next_col]!=self.EMPTY:
                break
            next_row+=offset[0]
            next_col+=offset[1]
        row_index = next_row-offset[0]
        col_index = next_col-offset[1]
        tile_moved = (row!=row_index or col!=col_index)
        if tile_moved:
            self.set_tile(row_index, col_index, self.grid[row][col])
            self.set_tile(row, col, self.EMPTY)
        return  tile_moved  
    
    def is_in_bounds(self, row, col):
        """
        """
        return  row<self.height and row>=0 and col<self.width and col>=0
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        if self.is_full() != True:
            rand_pos_num = random.randrange(len(self.empty_pos))
            row = self.empty_pos[rand_pos_num][0]
            col = self.empty_pos[rand_pos_num][1]
            rand_num = random.randrange(1,10)
            if rand_num == 1:
                self.set_tile(row, col, 4)
            else:
                self.set_tile(row, col, 2)
            
    def is_full(self):
        """
        Helper Function that checks if all spots in the grid have tiles
        """
        return len(self.empty_pos) == 0
        
    
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        global grid
        self.grid[row][col] = value
        if value==self.EMPTY:
            self.empty_pos.append((row,col))
        else:
            if (row,col) in self.empty_pos:
                self.empty_pos.remove((row,col))

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
poc_2048_testsuite.run_suite(TwentyFortyEight)