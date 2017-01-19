"""
Merge function for 2048 game.
http://www.codeskulptor.org/#user42_VXqZnQwTEI_17.py
"""
EMPTY_POS = 0

def merge(line):
    """
    Function that merges a single row or column in 2048.
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
     
    
def test_merge(input_line, expected_line):
    """
    Function that tests the merge function
    """
    original_line = list(input_line)
    merged_line = merge(input_line)
    
    if original_line != input_line:
        print "Error: Changed original line"
        print "Input:",input_line
    print "Original:",original_line,"Expected:",expected_line,"Actual Result:", merged_line   

def test_shift_line(input_line, expected_line):
    """
    Function that tests the shift_line function
    """
    original_line = list(input_line)
    shift_line(input_line)
    print "Input: ",original_line,"Expected: ",expected_line,"Actual: ", input_line   

def shift_line_tests():
    """
    Function that runs the tests for the shift_line function
    """
    print "Testing shift_line"
    test_shift_line([2, 0, 2, 4], [2, 2, 4, 0])
    test_shift_line([2, 2, 0, 0], [2, 2, 0, 0])
    test_shift_line([0, 0, 2, 2], [2, 2, 0, 0])
    test_shift_line([2, 2, 2, 2, 2], [2, 2, 2, 2, 2])
    test_shift_line([8, 16, 16, 8], [8, 16, 16, 8])    

print "\nTesting merge"   
test_merge([2, 0, 2, 4], [4, 4, 0, 0])
test_merge([0, 0, 2, 2], [4, 0, 0, 0])
test_merge([2, 2, 0, 0], [4, 0, 0, 0])
test_merge([2, 2, 2, 2, 2], [4, 4, 2, 0, 0])
test_merge([8, 16, 16, 8], [8, 32, 8, 0])

