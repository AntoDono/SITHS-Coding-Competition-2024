# Problem 4: Brownies

At a small private university on Rhode Island, brownies are the local favorite snack.

Yaowait is a student in the university celebrating brownie day, he has brownies of different weights in grams.

The university requested Yaowait to find the sum of all the unique brownies' weights.

Given an array, **n**, of the weights of the brownies, help Yaowait find the sum of the unique brownies' weights.

A brownie is considered unique if its weight only appears once in the array.

<u>Example 1:</u>

n: [1,2,3,2]

Answer: 4

Explanation: The unique brownies' weights are 1 and 3. 1 + 3 = 4


<u>Example 2:</u>

n: [3,3,3,3]

Answer: 0

Explanation: There are no unique brownies


<u>Example 3:</u>

n: [1,3,5,9]

Answer: 18

Explanation: The uniques brownies' weights are 1, 3, 5 and 9. 1 + 3 + 5 + 9 = 18

Problem credits: Youwei Zhen

# Constraints
1 $\leq$ **length of n** $\leq$ 1000

1 $\leq$ **brownies' weight** $\leq$ 1000

# Input Format
The function will have one parameter: **brownies**, an array that contains the weights of the brownies in grams.

# Output Format
Return a number indicating the sum of the unique brownies' weights.