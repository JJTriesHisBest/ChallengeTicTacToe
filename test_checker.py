import pytest
from tictactoe_checker import Board, Content, Status



def test_x_row_one():
    board = Board(3)
    for i in range(0,3): 
        board.set(0,i,Content.CROSS)
    assert(board.check() == Status.CROSS_WIN)

def test_x_row_one_fail():
    board = Board(3)
    for i in range(0,2): 
        board.set(0,i,Content.CROSS)
    assert(board.check() == Status.UNDECIDED)


def test_o_row_two_four_by_four():
    board = Board(4)
    for i in range(0,4): 
        board.set(1,i,Content.NOUGHT)
    assert(board.check() == Status.NOUGHT_WIN)

def test_o_col_3_forty_by_forty():
    board = Board(40)
    for i in range(0,40):
        board.set(i,2,Content.NOUGHT)
    assert(board.check() == Status.NOUGHT_WIN)

def test_empty_board():
    board = Board(22)
    assert(board.check() == Status.UNDECIDED)

def test_one_cell():
    board = Board(1)
    assert(board.check() == Status.UNDECIDED)
    board.set(0,0,Content.CROSS)
    assert(board.check() == Status.CROSS_WIN)

def test_two_by_two():
    board = Board(2)
    assert(board.check() == Status.UNDECIDED)
    board.set(0,0,Content.CROSS)
    assert(board.check() == Status.UNDECIDED)
    board.set(1,1,Content.CROSS)
    assert(board.check() == Status.CROSS_WIN)
 
def test_lr_dia():
    board = Board(13)
    for i in range(0,13):
        board.set(i,i,Content.NOUGHT)
    assert(board.check() == Status.NOUGHT_WIN)

def test_rl_dia():
    board = Board(3)
    for i in range(0,3):
        board.set(i, 2 - i, Content.NOUGHT)
    print(board.grid)
    assert(board.check() == Status.NOUGHT_WIN)
