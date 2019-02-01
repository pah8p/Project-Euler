import pickle
import copy
import time

SOLVED_VECTOR = list(range(1, 10))

class Sudoku(object):

    def __init__(self, puzzle):
        self.puzzle = puzzle
        assert 9 == len(self.puzzle)
        for row in self.puzzle:
            assert(9 == len(row))

    def _check_vector(self, x):
        return sorted([y for y in x if y]) == SOLVED_VECTOR

    def _available(self, x):
        return [y for y in SOLVED_VECTOR if y not in x]

    def _get_box_index(self, n):
        if n < 3:
            return [0, 1, 2]
        elif n < 6:
            return [3, 4, 5]
        elif n < 9:
            return [6, 7, 8] 

    def _get_box(self, i, j):
        box = []
        for row in self._get_box_index(i):
            for col in self._get_box_index(j):
                box.append(self.puzzle[row][col])
        return box

    def check_row(self, i):
        return self._check_vector(self.puzzle[i])

    def check_col(self, j):
        return self._check_vector([row[j] for row in self.puzzle])

    def check_box(self, i, j):
        return self._check_vector(self._get_box(i, j))

    def check_cell(self, i, j):
        return self.check_row(i) and self.check_col(j) and self.check_box(i, j)

    def available_choices(self, i, j):
        row_choices = self._available(self.puzzle[i])
        col_choices = self._available([row[j] for row in self.puzzle])
        box_choices = self._available(self._get_box(i, j))
        return list(set(row_choices) & set(col_choices) & set(box_choices))

    def _print(self):
        for row in self.puzzle: print(row)

    def solved(self):
        for i in range(9):
            for j in range(9):
                if not self.check_cell(i, j):
                    return False
        return True

    def _brute_dupe_check(self, row, col):
        clean = lambda x: [y for y in x if y]
        row_check = len(set(clean(self.puzzle[row]))) == len(clean(self.puzzle[row]))
        col_check = len(set(clean([r[col] for r in self.puzzle]))) == len(clean([r[col] for r in self.puzzle]))
        box_check = len(set(clean(self._get_box(row, col)))) == len(clean(self._get_box(row, col)))
        return row_check and col_check and box_check

    def _brute_force(self):
        blanks = []
        for i in range(9):
            for j in range(9):
                if not self.puzzle[i][j]:
                    blanks.append((i, j))

        b = 0
        cycle = 0
        while b < len(blanks):

            if b < 0:
                break

            row = blanks[b][0]
            col = blanks[b][1]

            if self.puzzle[row][col] == 9:
                self.puzzle[row][col] = None
                b -= 1
                continue
                
            elif self.puzzle[row][col]:
                self.puzzle[row][col] += 1

            else:
                self.puzzle[row][col] = 1

            if self._brute_dupe_check(row, col):
                b += 1
                
            else:
                if self.puzzle[row][col] < 9:
                    b += 0

                else:
                    self.puzzle[row][col] = None
                    b -= 1
                
            cycle += 1
            
        return True
        

    def _deduce(self):

        keep_running = True
        passes = 0

        while keep_running:

            updated = False
            
            for i in range(9):
                for j in range(9):
                    if not self.puzzle[i][j]:
                        choices = self.available_choices(i, j)
                        if len(choices) == 1:
                            self.puzzle[i][j] = choices[0]
                            updated = True

            passes += 1
            solved = self.solved()

            if solved:
                keep_running = False

            if updated or passes < 100:
                keep_running = True
            else:
                keep_running = False
                
        return solved

    def _guess(self, num_choices):
        for i in range(9):
            for j in range(9):
                if not self.puzzle[i][j]:
                    choices = self.available_choices(i, j)
                    if len(choices) == num_choices:
                        for choice in choices:
                            _puzzle = copy.deepcopy(self.puzzle)
                            _puzzle[i][j] = choice
                            _sudoku = Sudoku(_puzzle)
                            solved = _sudoku._deduce()
                            if solved:
                                self.puzzle = _sudoku.puzzle
                                return solved
        return False

    def solve(self):
        solved_deduce = self._deduce()
        if solved_deduce:
            #self._print()
            return self.puzzle

        else:
            solved_brute = self._brute_force()
            #self._print()
            return self.puzzle
##            for n in range(2, 10):
##                solved_guess = self._guess(n)
##                if solved_guess:
##                    self._print()
##                    return self.puzzle

        #self._print()

        return None

def load_puzzles():
    file = 'C:/Users/Pete/AppData/Local/Programs/Python/Python36-32/Scripts/euler/p096_sudoku.txt'
    with open(file, 'r') as f:
        raw_puzzles = f.readlines()
        
    def clean(n):
        try:
            if int(n) == 0:
                return None
            else:
                return int(n)
        except ValueError:
            return n
        
    puzzles = []
    for line_num, line in enumerate(raw_puzzles):
        if 'Grid' in line:
            puzzle = []
            for n in range(1, 10):
                row = [clean(n) for n in raw_puzzles[line_num+n]]
                puzzle.append(row[:9])

            puzzles.append(puzzle)

    return puzzles

puzzles = load_puzzles()
             
puzzle = [
    [None, None, 3, None, 2, None, 6, None, None],
    [9, None, None, 3, None, 5, None, None, 1],
    [None, None, 1, 8, None, 6, 4, None, None],
    [None, None, 8, 1, None, 2, 9, None, None],
    [7, None, None, None, None, None, None, None, 8],
    [None, None, 6, 7, None, 8, 2, None, None],
    [None, None, 2, 6, None, 9, 5, None, None],
    [8, None, None, 2, None, 3, None, None, 9],
    [None, None, 5, None, 1, None, 3, None, None],
]

puzzle_wiki = [
    [5, 3, None, None, 7, None, None, None, None],
    [6, None, None, 1, 9, 5, None, None, None],
    [None, 9, 8, None, None, None, None, 6, None],
    [8, None, None, None, 6, None, None, None, 3],
    [4, None, None, 8, None, 3, None, None, 1],
    [7, None, None, None, 2, None, None, None, 6],
    [None, 6, None, None, None, None, 2, 8, None],
    [None, None, None, 4, 1, 9, None, None, 5],
    [None, None, None, None, 8, None, None, 7, 9],
]
    

s = 0
ss = 0
for n, puzzle in enumerate(puzzles):
    #print(n)
    sudoku = Sudoku(puzzle)
    s = time.time()
    sudoku.solve()
    print('%s ---- %s' % (n, time.time()-s))
    #print(sudoku.solved())
    if sudoku.solved():
        s += 1
        print(100*sudoku.puzzle[0][0] + 10*sudoku.puzzle[0][1] + sudoku.puzzle[0][2])
        ss += 100*sudoku.puzzle[0][0] + 10*sudoku.puzzle[0][1] + sudoku.puzzle[0][2]

print(s)
print(ss)

#sudoku = Sudoku(puzzles[1])
#sudoku._brute_force()
#print([row[0] for row in sudoku.puzzle])
#print(sudoku._get_box(0, 0))
#print(sudoku._get_box(1, 1))
#print(sudoku._get_box(0, 7))
#print(sudoku.available_choices(0, 0))
