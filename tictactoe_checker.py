from enum import Enum


class Content(Enum):
    CROSS = 1
    NOUGHT = 2
    EMPTY = 3

class Status(Enum):
    UNDECIDED = 1
    CROSS_WIN = 2
    NOUGHT_WIN = 3

class Board():
    def __init__(self, dimensionality):
        self.n = dimensionality
        self.grid = [[Content.EMPTY for y in range(0,dimensionality)] for x in range(0,dimensionality)]
    
    
    def set(self, col, row, content):
        self.grid[col][row] = content


    def who_wins(self, row, col):
        if self.grid[col][row] == Content.CROSS:
            return Status.CROSS_WIN
        elif self.grid[col][row] == Content.NOUGHT:
            return Status.NOUGHT_WIN
        else:
            return Status.UNDECIDED
            
   
    def check(self):
        count_rl = 0
        count_lr = 0
        for i in range(0, self.n):
            if self.grid[i][i] == Content.EMPTY:
                if self.grid[self.n-i-1][i] == self.grid[self.n-1][0] and self.grid[self.n-1][0] != Content.EMPTY:
                    count_lr += 1
                continue
            #check row
            row = True
            for j in range(0, self.n):
                row = True
                if self.grid[j][i] != self.grid[i][i]:
                    row = False
                    break
            if row:
                return self.who_wins(i,i)

            #check col
            col = True
            for k in range(0, self.n):
                col = True
                if self.grid[i][k] != self.grid[i][i]:
                    col = False
                    break
            if col:
                return self.who_wins(i,i)

            if self.grid[i][i] == self.grid[0][0]:
                count_rl += 1
            if self.grid[i][self.n-i-1] == self.grid[0][self.n-1] and self.grid[0][self.n-1] != Content.EMPTY:
                count_lr += 1
        #check_diagonals
        if count_rl == self.n:
            return self.who_wins(0,0)
        elif count_lr == self.n:
            return self.who_wins(0, self.n - 1)
        else:
            return Status.UNDECIDED


