# Problem 3: Infinite-Toes

T. Anderson recently invented a new name called Infinite Tic Tac Toes.

In Infinite Tic Tac Toes, the grid is **n** by **n**.

All the other rules from Tic Tac Toe applies to Infinite Tic Tac Toes.

Given a 2D array representing the Infinite Tic Tac Toes grid, determine if there is a winner by returning 'YES' or 'NO'.

X = Player 1

O = Player 2

_ = Empty space

Example 1:

[<br>
    &emsp;[ 'X', 'O', '\_' ],<br>
    &emsp;[ '\_', 'X', 'O' ],<br>
    &emsp;[ '\_', 'O', 'X' ]<br>
]

Answer: YES

Explanation: there is a winner, as  the Xs makes a diagonal.

Example 2:

[<br>
    &emsp;[ 'X', 'X', 'X', 'X', 'O'],<br>
    &emsp;[ '\_', 'O', 'O', '\_', '\_' ],<br>
    &emsp;[ '\_', 'O', 'X', '\_', '\_' ]<br>
    &emsp;[ '\_', 'X', 'O', '\_', '\_' ]<br>
    &emsp;[ 'X', 'O', 'O', '\_', '\_' ]<br>
]

Answer: NO

Explanation: there are no completed rows, columns, or diagonals. There are no winners.

Problem credits: Youwei Zhen

# Constraints
1 $\leq$ **n** $\leq$ 10

# Input Format
The function will have one parameter: **board**, a 2D array that represents the game board. 

# Output Format
Return a string "YES" or "NO" to indicate if there is a winner.