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

EMPTY_POS = 0

def merge(line):
    """
    Helper function that merges a single row or column in 2048.
    """
    merged_line = list(line)
    shift_line(merged_line)
    line_len = len(merged_line)
    if line_len > 1:
        for index in range(1,line_len):
            if merged_line[index]==merged_line[index-1]:
                merged_line[index-1] += merged_line[index-1]
                merged_line[index] = EMPTY_POS
        shift_line(merged_line)
    return merged_line
  
    
def shift_line(line):
    """
    Helper function for merge that shifts all tiles to the left
    """
    num_empty_pos = 0
    while EMPTY_POS in line:
        line.remove(EMPTY_POS)
        num_empty_pos+=1
    for dummy_pos in range(num_empty_pos):
        line.append(EMPTY_POS)
     
    

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    
    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.reset()
        self.initial_tiles={}
        self.initial_tiles[UP]=[(0, col) for col in range(self.width)]
        self.initial_tiles[DOWN]=[(self.height-1,col) for col in range(self.width)]
        self.initial_tiles[LEFT]=[(row,0) for row in range(self.height)]
        self.initial_tiles[RIGHT]=[(row,self.width-1) for row in range(self.height)]
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[ 0 for dummy_i in range(self.width)] for dummy_j in range(self.height)]
        self.new_tile()
        self.new_tile()
        print str(self)

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
        tiles_moved = False
        for initial_pos in self.initial_tiles[direction]:
            row = initial_pos[0]
            col = initial_pos[1]
            temp_line = self.build_temp_line(row,col, direction)
            merged_line = merge(temp_line)
            if temp_line != merged_line:
                self.copy_line_to_grid(row, col, direction, merged_line)
                tiles_moved = True
        if tiles_moved:
            self.new_tile()
        print str(direction)
        print str(self)
    
    def copy_line_to_grid(self, row, col, direction, line):
        for index in range(len(line)):        
            self.set_tile(row, col, line[index])    
            row+=OFFSETS[direction][0]
            col+=OFFSETS[direction][1]
            
    def build_temp_line(self, row, col, direction):
        temp_line = []
        while self.is_in_bounds(row, col):
            temp_line.append(self.grid[row][col])
            row+=OFFSETS[direction][0]
            col+=OFFSETS[direction][1]
        return temp_line
    
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
        empty_pos = []
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col]==EMPTY_POS:
                    empty_pos.append((row,col))
        if len(empty_pos) != 0:
            rand_pos_num = random.randrange(len(empty_pos))
            row = empty_pos[rand_pos_num][0]
            col = empty_pos[rand_pos_num][1]
            rand_num = random.randrange(1,10)
            if rand_num == 1:
                self.set_tile(row, col, 4)
            else:
                self.set_tile(row, col, 2)
  
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value
       
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
#poc_2048_testsuite.run_suite(TwentyFortyEight)