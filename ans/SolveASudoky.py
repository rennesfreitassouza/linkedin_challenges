from itertools import product

def solve_sudoku(puzzle): # backtrack approach
    for (row, col) in product(range(0, 9), repeat=2):
        if puzzle[row][col] == 0: # find an unassigned cell
            for num in range(1, 10):
                allowed = True # check if num is allowed in row/col/box
                for i in range(0,9):
                    if (puzzle[i][col ] == num) or (puzzle[row][i] == num):
                        allowed = False; break # not allowd in row or col
                for (i, j) in product(range(0, 3), repeat=2):
                    if puzzle[row-row%3+i][col-col%3+j] == num:
                        allowed = False; break
                if allowed:
                    puzzle[row][col] = num
                    if trial := solve_sudoku(puzzle):  # or if solve_sudoku2(puzzle): return True
                        return trial
                    else:
                        puzzle[row][col] = 0
            return False # could not place a number in this cell
    return puzzle

def main(puzzle = [[]]):
    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]
    solve_sudoku(puzzle) # list is a mutable type
    
    print(puzzle)

if __name__ == '__main__': main()
