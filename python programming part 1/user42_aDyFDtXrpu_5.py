"""
Testing Suite for 2048 Assignment
"""

import poc_simpletest

def run_suite(game_class):
    """
    Run test Suite
    """
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    
    suite = poc_simpletest.TestSuite()
    WIDTH_1 = 4
    HEIGHT_1 = 5
    game = game_class(HEIGHT_1, WIDTH_1)
    
    #Test - Getters
    suite.run_test(game.get_grid_height(), HEIGHT_1, "Get Grid Height Incorrect Result")
    suite.run_test(game.get_grid_width(), WIDTH_1, "Get Grid Width Incorrect Result")
    
    #Test - Tile Operations
    game.set_tile(0,0,4)
    game.set_tile(4,3,2)
    game.set_tile(2,2,2)
    suite.run_test(game.get_tile(0,0), 4, "Get/Set Tile is not working" )
    suite.run_test(game.get_tile(2,2), 2, "Get/Set Tile is not working" )
    suite.run_test(game.get_tile(4,3), 2, "Get/Set Tile is not working" )
    
#    #Test - New_Tile.... How to test?
#    #game.new_tile()
#    #Test - Reset
#    #game.reset()
#    print str(game)
#    game.move(UP)
#    print str(game)
#    game.move(DOWN)
#    print str(game)
#    game.move(LEFT)
#    print str(game)
#    game.move(RIGHT)
#    print str(game)
#    #Report Results

    game = game_class(HEIGHT_1, WIDTH_1)
    game.set_tile(0,3,2)
    game.set_tile(1,3,2)
    print str(game)
    game.move(UP)
    suite.run_test(game.get_tile(0,3), 4, "Error get tile after Move UP returned wrong value")
    suite.run_test(game.get_tile(1,3), 0, "Error get tile after Move UP returned wrong value")
    print str(game)
    
    game = game_class(HEIGHT_1, WIDTH_1)
    game.set_tile(0,0,2)
    game.set_tile(0,3,2)
    print str(game)
    game.move(LEFT)
    suite.run_test(game.get_tile(0,0), 4, "Error get tile after Move LEFT returned wrong value")
    print str(game)
    
    game = game_class(HEIGHT_1, WIDTH_1)
    game.set_tile(0,0,8)
    game.set_tile(0,1,4)
    game.set_tile(0,2,4)
    game.set_tile(0,3,2)
    print str(game)
    game.move(LEFT)
    suite.run_test(game.get_tile(0,0), 8, "Error get tile after Move LEFT returned wrong value")
    suite.run_test(game.get_tile(0,1), 8, "Error get tile after Move LEFT returned wrong value")
    suite.run_test(game.get_tile(0,2), 2, "Error get tile after Move LEFT returned wrong value")
    print str(game)
    
    game = game_class(HEIGHT_1, WIDTH_1)
    game.set_tile(0,3,4)
    game.set_tile(1,3,32)
    game.set_tile(2,3,2)
    game.set_tile(3,3,2)
    print str(game)
    game.move(DOWN)
    suite.run_test(game.get_tile(2,3), 4, "Error get tile after Move LEFT returned wrong value")
    suite.run_test(game.get_tile(3,3), 32, "Error get tile after Move LEFT returned wrong value")
    suite.run_test(game.get_tile(4,3), 4, "Error get tile after Move LEFT returned wrong value")
    print str(game)
    suite.report_results()
  