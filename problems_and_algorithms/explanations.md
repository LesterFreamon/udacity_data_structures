# Explanations

## Problem 1: Square Root of an Integer

### Description:

Find the square root of the integer without using any Python library. You have to find the floor value of the square
root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:

### Algorithm:

There are two special cases where $n = \sqrt{n}$, and that's when $n=1, 2$. We will deal with these two cases right off
the bat.

For the rest of the natural numbers, we will start with a space consisting $[1, \frac{n}{2}]$ since for all other
natural numbers, the square root is at most $\frac{n}{2}$. From that point we will preform a binary search that would
either increase the lower bound, if the square is too small, or decrease the upper bound if it is too big.

We will also check (n + 1)^2 and (n - 1)^2 when the square is either smaller or bigger from the target, respectively, to
avoid bugs.

### Time Complexity:

This is a binary search, so the number of loop is $O(log(n))$. It's not entirely accurate for very large number because
of the squaring that's preformed in every loop, but I ignore that for the problem.

### Space Complexity:

$O(1)$ since there are just three numbers stored (min_num, run_num and top_num).

## Problem 2: Search in a Rotated Sorted Array

### Description:

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(
log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

### Algorithm:

If we have a sorted list, then the problem can be solved with a simple binary search in time $O(log(n))$ and space $O(
log(n))$, due to recursion.

So the strategy here is to

* Find the pivot in $O(log(n))$ time and $O(1)$ space.
* Then apply a binary search on the two sorted sub-arrays.
* The runtime would then be $3*O(log(n))$, which is $O(log(n))$.

### Time Complexity:

Essentially 3 times binary search, so $O(log(n))$.

### Space Complexity:

$O(log(n))$, because of the recursion stack.

## Problem 3: Rearrange Array Elements

### Description:

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can
assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more
than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(
n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there
are more than one possible answers, return any one.

### Algorithm:

All we need to do is create two number that add digits, from smallest to bigget, while keeping track of their decimal
place. We can simply add the digit multiplied by 10 ^ (loop number - 1). In other words, we can create a min priority
queue be heapifying the input (that would take O(n) time) and then, for $\frac{n}{2}$ loops we can pop the two min
elements, multiply them by $$10^{loop\space num - 1}$$ and add them to the numbers we inted to output. Then end result
would be the two numbers that will give the maximum sum. The total time will be $$O(n) + \frac{n}{2} \cdot O(\log(n))=O(
n\log(n))$$

### Time Complexity:

As written in the description of the algorithm, the runtime would be $O(n\cdot\log(n))$

### Space Complexity:

Since we are heapifying the input array inplace, and there are no recursion steps, the additional space required is $O(
1)$

## Problem 4: Dutch National Flag Problem

### Description:

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any
sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an
O(n) solution but it will not count as single traversal.

### Algorithm:

We can keep count of the number of zeros and ones encountered and that way we can deduce what swaps we need to do for
every 0, 1 or 2 value for the array we traverse.

* If we encounter a 0, first swap i with num_zeros_found + num_ones_found, then num_zeros_found + num_ones_found,
  num_zeros_found
* If we encounter a 1 swap i with num_zeros_found + num_ones_found
* If we encounter a 2 then swap nothing

### Time Complexity:

Since we are doing one traversal, the runtime is $O(n)$

### Space Complexity:

Since we are swapping in place, then additional space needed is $O(1)$

## Problem 5: Autocomplete with Tries

### Algorithm:

Using a dictionry to store the letters of the words. build a graph with that dictionary to find later letters.

### Time Complexity:

Worst case is $O(n)$ where $n$ is the number of letters in a string

### Space Complexity:

Worst case is $O(n)$ where $n$ is the number of letters in the longest string.

## Problem 6: Max and Min in a Unsorted Array

### Description:

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in
O(n) time. Do not use Python's inbuilt functions to find min and max.

### Algorithm:

We can initialize a min number $=\infty$ and a max number =-$\infty$. Then, we traverse the list and compare take
assign, each iteration $maxNumber=max(maxNumber, thisNumber)$ and $minNumber=min(minNumber, thisNumber)$. In case the
list is empty, we will return a tuple of None.

### Time Complexity:

We traverse the list once, so the runtime is $O(n)$

### Space Complexity:

We only keep track of min_num and max_num, so the additional space needed is $O(1)$

## Problem 7:

### Description:

Long description, but essentially build a trie tree to store and look for paths tha lead to handlers.

### Algorithm:

As the problem statement configured:
Three classes:

* Router trie node
* Router trie
* Router

### Time Complexity:

Worst case is $O(n)$ where $n$ is the number of url parts in the path

### Space Complexity:

Worst case is $O(n)$ where $n$ is the number of url parts in the longest path.
