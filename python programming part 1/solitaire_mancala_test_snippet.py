def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"

    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   

    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]

    print "Testing plan_moves - Computed:", my_game.plan_moves(), "Expected:", str([5,1,2,1,4,1,3,1,2,1])
    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(0), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(1), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(3), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(5), "Expected:", True
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 5
    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    my_game.apply_move(3)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])   
    my_game.apply_move(5)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 4, 2, 2, 1, 1])
    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(0), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(1), "Expected:", True
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(2), "Expected:", True
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(3), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(4), "Expected:", True
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(5), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(6), "Expected:", False
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1
    my_game.apply_move(0)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 4, 2, 2, 1, 1])   
    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 4, 2, 2, 0, 2])   
    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", False 
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 2
    my_game.apply_move(2)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 4, 2, 0, 1, 3])   
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1
    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 4, 2, 0, 0, 4])   
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 4
    my_game.apply_move(4)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 0, 3, 1, 1, 5])   
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1
    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 0, 3, 1, 0, 6])   
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 3
    my_game.apply_move(3)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 0, 0, 2, 1, 7])   
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1
    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 0, 0, 2, 0, 8])   
    my_game.apply_move(2)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 0, 0, 0, 1, 9])   
    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 0, 0, 0, 0, 10])   
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 0 
    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", True 

    my_game2 = SolitaireMancala()
    print "Testing init - Computed:", my_game2, "Expected: [0]"
    config2 = [0, 0, 1, 1, 0, 0, 0]
    my_game2.set_board(config2) 
    print "Testing set_board - Computed:", str(my_game2), "Expected:", str([0, 0, 0, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game2.get_num_seeds(1), "Expected:", config2[1]
    print "Testing get_num_seeds - Computed:", my_game2.get_num_seeds(3), "Expected:", config2[3]
    print "Testing get_num_seeds - Computed:", my_game2.get_num_seeds(5), "Expected:", config2[5]
    print "Testing plan_moves - Computed:", my_game.plan_moves(), "Expected:", str([])
    print "Testing choose_move - Computed:", my_game2.choose_move(), "Expected:", 0 
    print "Testing is_game_won - Computed:", my_game2.is_game_won(), "Expected:", False 

test_mancala()
