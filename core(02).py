actual_grid = [
    [' ', ' ', ' ', 'h', 'y', 'p', 'e', 'r', 't', 'u', 'n', 'i', 'n', 'g', ' '], 
    [' ', ' ', ' ', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', 'd', ' ', 'c', 'o', 'd', 'e', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', 'e', ' ', ' ', ' ', ' ', ' ', 'a', ' ', ' ', 'o', ' ', ' '], 
    [' ', ' ', ' ', 'b', 'b', ' ', ' ', ' ', ' ', 'l', ' ', ' ', 'v', ' ', ' '], 
    [' ', 'j', ' ', 'u', 'i', ' ', 'j', ' ', ' ', 'g', ' ', ' ', 'e', ' ', ' '], 
    [' ', 'a', ' ', 'g', 'n', ' ', 'a', ' ', ' ', 'o', ' ', 'h', 'r', 'p', ' '], 
    [' ', 'v', ' ', ' ', 'a', ' ', 'v', ' ', ' ', 'r', ' ', 't', 'f', 'y', ' '], 
    ['c', 'a', ' ', ' ', 'r', ' ', 'a', ' ', ' ', 'i', ' ', 'm', 'i', 't', ' '], 
    ['s', ' ', ' ', ' ', 'y', ' ', 's', ' ', ' ', 't', ' ', 'l', 't', 'h', ' '], 
    ['s', ' ', ' ', ' ', ' ', ' ', 'c', ' ', ' ', 'h', ' ', ' ', 't', 'o', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', 'r', ' ', ' ', 'm', ' ', ' ', 'i', 'n', 'r'], 
    [' ', ' ', ' ', ' ', ' ', ' ', 'i', ' ', ' ', ' ', ' ', ' ', 'n', ' ', 'u'], 
    [' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', 'g', ' ', 'b'], 
    [' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'y']]


current_grid = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', 'D', ' ', 'c', 'o', 'd', 'e', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', '', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

current_pos = [2, 5]

current_grid_SIZE = 15

def check_word(current, horizontal):
    given_word = ""
    actual_word = ""
    for i in range(current[1], current_grid_SIZE):
        if actual_grid[current[0]][i] != ' ':
            given_word += current_grid[current[0]][i]
            actual_word += actual_grid[current[0]][i]
        else:
            break
    print(given_word + actual_word)
    return given_word == actual_word


print(check_word(current_pos, horizontal=True))