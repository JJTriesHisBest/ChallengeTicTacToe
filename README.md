# Challenge 1 - Tic Tac Toe Checker
Hi again Wingo! So this is the kind of thing I was going for during our chat on Monday. I've added the extra check which lets us know if it was noughts or crosses that have won. The tests in pytest show that it works for rows, cols, and diagonals right-to-left & left-to-right.

The best way to test this yourselves is to run pytest and add further test cases if there's an edge case you think I've missed.

## Limitations I'm aware of
For valid tic-tac-toe games this should be fine. If there was ever the possibility of there being more than one win condition present at a time, then it would just report whichever it found first as the victor. 

## Expand?
If we're reporting wins for each side, and undecided as conditions, then the next step should be to detect stalemates. 


