# Problem 5: Skibidi Whalen

Mr. Whalen is stuck in a maze and needs to use the bathroom, but he cannot find the exit. Help him determine if there is a valid solution to the maze.

Given an integer **n**, and a maze that is **n** by **n** in size. Determine if the maze can be solved.

0 represents Mr. Whalen's current position

1 represents the exit

\# represents a wall

. represents a valid space that Mr. Whalen can travel to.



Example:

n: 5

0 . ###<br>
\# . ###<br>
\# . ###<br>
\# . . . .<br>
\####1<br>

Representation of the maze in a 2D Array:

[<br>
    &emsp;
['0', '.' , '#', '#', '#'],<br>
    &emsp;
['#', '.' , '#', '#', '#'],<br>
    &emsp;
['#', '.' , '#', '#', '#'],<br>
    &emsp;
['#', '.' , '.', '.', '.'],<br>
    &emsp;
['#', '.' , '.', '.', '1']<br>
]


Answer: "YES"

Explanation: There is a valid solution to this maze.

Problem credits: Youwei Zhen

# Constraints
<u>Test case 1-3:</u> 

3 $\leq$ **n** $\leq$ 5

<u>Test case 4-15:</u>

5 $\leq$ **n** $\leq$ 15

# Input Format
The function will have two parameters: **n**, the size of the maze; **N** the representation of the maze in a 2D Array.

# Output Format
Return a string "YES" or "NO" to indicate if the maze has a solution.