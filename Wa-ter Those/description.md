# Problem 3: Wa-ter Those!?

Harvey loves to drink sodas. 

On the floor, there are **n** soft drinks of different volumes placed in a row.

Harvey can pick up at most **m** consecutive bottles of soft drinks. 

Given an array **s**, and **v**, the volume  of each soft drinks in order, help Harvey determine the maximum volume of soft drinks he can pick to to drink.

Example:

n: 5<br>
m: 3<br>
s: [ 1, 3, 5, 7, 9 ]

Answer: 21

Explanation: The 3 consecutive soft drinks that makes up the maximum volume is 5, 7, and 9.

*Hint: In languages such as C++, a long type might be required to store the large numbers.*

Problem credits: Youwei Zhen & Special Thanks to Harvey Jiang

# Constraints

1 $\leq$ **v** $\leq$ 10 <sup>3</sup>

<u>Test case 1-3:</u> 

1 $\leq$ **n** $\leq$ 10

1 $\leq$ **m** $\leq$ 3

<u>Test case 4-7:</u>

1 $\leq$ **n** $\leq$ 10 <sup>5</sup>

1 $\leq$ **m** $\leq$ 10 <sup>3</sup>

<u>Test case 8-15:</u>

1 $\leq$ **n** $\leq$ 10 <sup>5</sup>

1 $\leq$ **m** $\leq$ 10 <sup>5</sup>

# Input Format
The function will have three parameters: **n**, the number of soft drinks; **m** the amount of bottles Harvey can pick up consecutively; **s** an array that represents the volumes of each soft drinks.


# Output Format
Return a single integer indicating the maximum volume of soft drinks Harvey can drink.