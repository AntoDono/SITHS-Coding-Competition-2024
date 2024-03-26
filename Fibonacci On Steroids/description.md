# Problem 6: Fibonacci

The Fibonacci sequence starts with 0 and 1, then each number is the sum of the two before it. 

Given an array of integers, **a**, where each element **i** represents the **i**-th number of the fibonacci sequence, find the sum of those numbers.

Since the answer might be very large, return the answer modulo 10<sup>9</sup>.

Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377

a: [1, 3, 5, 7]

<u>Answer</u>: 12

<u>Explanation</u>:

**1**-st number in Fibonacci sequence: 0

**3**-rd number in Fibonacci sequence: 1

**5**-th number in Fibonacci sequence: 3

**7**-th number in Fibonacci sequence: 8

So, 0 + 1 + 3 + 8 = 12

*Hint: In languages such as C++, a long type might be required to store the large numbers.*

Problem credits: Youwei Zhen

# Constraints

1 $\leq$ **i** $\leq$ 10 <sup>5</sup>

<u>Test cases 1-3</u>:

2 $\leq$ **a.length** $\leq$ 5

<u>Test cases 4-8</u>:

2 $\leq$ **a.length** $\leq$ 10<sup>3</sup>

<u>Test cases 9-15</u>:

2 $\leq$ **a.length** $\leq$ 10<sup>5</sup>

# Input Format
The function will have one parameter: a, which is an array of integers.

# Output Format
Return a the sum of the chosen numbers in the fibonacci sequence modulo 10<sup>9</sup>.