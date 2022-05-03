import random
import copy


class Sudoku:
    def __init__(self):
        #any filled board of sudoku
        self.base_board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [4, 5, 6, 7, 8, 9, 1, 2, 3],
                           [7, 8, 9, 1, 2, 3, 4, 5, 6],
                           [2, 3, 1, 5, 6, 4, 8, 9, 7],
                           [5, 6, 4, 8, 9, 7, 2, 3, 1],
                           [8, 9, 7, 2, 3, 1, 5, 6, 4],
                           [3, 1, 2, 6, 4, 5, 9, 7, 8],
                           [6, 4, 5, 9, 7, 8, 3, 1, 2],
                           [9, 7, 8, 3, 1, 2, 6, 4, 5]]
        self.res = None

    #take a random number from range [1 to 9]
    def shuffle_numbers(self):
        for i in range(9):
            ran_num = random.randint(0, 8)
            self.swap_numbers(i, ran_num)

    # traverse the board, swap num with your random number.
    def swap_numbers(self, n1, n2):
        for y in range(9):
            for x in range(9):
                if self.base_board[x][y] == n1:
                    self.base_board[x][y] = n2
                elif self.base_board[x][y] == n2:
                    self.base_board[x][y] = n1

    #Take the first group of 3 rows , shuffle them
    def shuffle_rows(self):
        block_number = None
        for i in range(9):
            ran_num = random.randint(0, 2)
            block_number = i // 3
            self.swap_rows(i, block_number * 3 + ran_num)

    #do it for all rows.
    def swap_rows(self, r1, r2):
        row = self.base_board[r1]
        self.base_board[r1] = self.base_board[r2]
        self.base_board[r2] = row

    #Swap columns, again take block of 3 columns, shuffle them
    def shuffle_cols(self):
        block_number = None
        for i in range(9):
            ran_num = random.randint(0, 2)
            block_number = i // 3
            self.swap_cols(i, block_number * 3 + ran_num)

    #do it for all 3 blocks
    def swap_cols(self, c1, c2):
        col_val = None
        for i in range(9):
            col_val = self.base_board[i][c1]
            self.base_board[i][c1] = self.base_board[i][c2]
            self.base_board[i][c2] = col_val

    #swap the row blocks itself
    def shuffle3X3Rows(self):
        for i in range(3):
            ran_num = random.randint(0, 2)
            self.swap3X3Rows(i, ran_num)

    def swap3X3Rows(self, r1, r2):
        for i in range(3):
            self.swap_rows(r1 * 3 + i, r2 * 3 + i)

    #do the same for columns, swap blockwise
    def shuffle3X3Cols(self):
        for i in range(3):
            ran_num = random.randint(0, 2)
            self.swap3X3Cols(i, ran_num)

    def swap3X3Cols(self, c1, c2):
        for i in range(3):
            self.swap_cols(c1 * 3 + i, c2 * 3 + i)

    #check rows and columns of a valid sudoku
    @staticmethod
    def chkrnc(b):
        for i in range(9):
            dr = {}
            dc = {}
            for j in range(9):
                rv = b[i][j]
                if rv not in dr:
                    dr[rv] = 1
                elif rv in dr or rv == 0:
                    return False
                cv = b[j][i]
                if cv not in dc:
                    dc[cv] = 1
                elif cv in dc or cv == 0:
                    return False
        return True

    @staticmethod
    def checkboxes(b):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                d = {}
                for c in range(i, i + 3):
                    for l in range(j, j + 3):
                        cv = b[l][c]
                        if cv not in d:
                            d[cv] = 1
                        elif cv in d or cv == 0:
                            return False
        return True

    @staticmethod
    def isValidSudoku(b):
        if not Sudoku.chkrnc(b):
            return False
        if not Sudoku.checkboxes(b):
            return False
        return True

    def create_problem(self):
        n = random.randint(15, 30)
        for i in range(n + 1):
            r = random.randint(0, 6)
            c = random.randint(0, 6)
            if self.base_board[r][c] != 0:
                self.base_board[r][c] = 0

    def set_problem(self):
        self.shuffle_rows()
        self.shuffle_cols()
        self.shuffle3X3Rows()
        self.shuffle3X3Cols()
        self.create_problem()

    def possible(self, y, x, n):
        for i in range(0, 9):
            if self.base_board[y][i] == n:
                return False
        for i in range(0, 9):
            if self.base_board[i][x] == n:
                return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.base_board[y0 + i][x0 + j] == n:
                    return False
        return True

    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.base_board[y][x] == 0:
                    for n in range(1, 10):
                        if self.possible(y, x, n):
                            self.base_board[y][x] = n
                            self.solve()
                            self.base_board[y][x] = 0
                    return
        self.res = copy.deepcopy(self.base_board)