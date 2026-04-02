# DSA Studies 📚

This repository is for my personal **Data Structures & Algorithms (DSA)** practice.

I’m using it to:
- Implement algorithms
- Solve problems (e.g., LeetCode)
- Study and practice DSA concepts

## Algorithms
### Quick Sort
Implematation of a [Quick Sort](algorithms/sorting/quick_sort.py).

is a divide-and-conquer sorting algorithm used to sort an array with recursion;
It works by selecting a pivot element, partitioning the array into elements less than and greater than the pivot, and then recursively sorting the subarrays.

* Time complexity: O(n2) or O(n log n) (When using a random pivot or a middle pivot, it is extremely unlikely to fall into the O(n²) case.).
* Space Complexity: O(log n) or O(n) (when recursion becomes highly unbalanced)

### Bubble Sort
Implematation of a [Bubble Sort](algorithms/sorting/bubble_sort.py).

Bubble Sort is a simple sorting algorithm used to sort arrays.
It works by repeatedly passing through the array, comparing adjacent elements and swapping them if they are in the wrong order.
This process continues until the array is fully sorted.

* Time complexity: O(n2)
* Space Complexity: O(n)

## Data Structures
### Hashmap
Implematation of a [Hashmap](data_structures/hashmap.py).

A HashMap is a data structure that stores values using key-value pairs.
Each key is mapped to a value, allowing fast insertion, retrieval and deletion operations.
* Insert: O(1)
* Delete: O(1)
* Get: O(1)

### Linked List
Implementation of a [Linked List](data_structures/linked_list.py)

A Linked List is a linear data strcuture composed of nodes, where each noed stores a value and a reference to the next node in memory.
Unlike arrays, linked lists do not store elements contiguously in memory.

* Insert: O(1)
* Delete: O(n)
* Get: O(n)

## Leetcode
This repository contains my accepted solutions to various **LeetCode problems**, implemented in different programming languages.  
Each problem includes a direct link to the source code and the official submission.

* My account: [leetcode.com/u/yhammes](https://leetcode.com/u/yhammes/)

### 📚 Problems Solved

- **1. Two Sum**  
[Code](algorithms/.leetcode/1.two-sum.java) 

- **9. Palindrome Number**  
[Code](algorithms/.leetcode/9.palindrome-number.cpp) 

- **151. Reverse Words In a String**  
[Code](algorithms/.leetcode/151.reverse-words-in-a-string.py) 

- **345. Reverse Vowels Of a String**  
[Code](algorithms/.leetcode/345.reverse-vowels-of-a-string.py) 

- **557. Reverse Words in a String III**  
[Code](algorithms/.leetcode/557.reverse-words-in-a-string-iii.py) 

- **605. Can Place Flowers**  
[Code](algorithms/.leetcode/605.can-place-flowers.py) 

- **1071. Greatest Common Divisor of Strings**  
[Code](algorithms/.leetcode/1071.greatest-common-divisor-of-strings.cpp) 

- **1431. Kids With the Greatest Number of Candies**  
[Code](algorithms/.leetcode/1431.kids-with-the-greatest-number-of-candies.cpp) 

- **1768. Merge Strings Alternately**  
[Code](algorithms/.leetcode/1768.merge-strings-alternately.cpp) 

- **1935. Maximum Number of Words You Can Type**  
[Code](algorithms/.leetcode/1935.maximum-number-of-words-you-can-type.cpp) 

- **2703. Return Length of Arguments Passed**  
[Code](algorithms/.leetcode/2703.return-length-of-arguments-passed.cpp) 

- **3090. Maximum Length Substring With Two Occurrences**  
[Code](algorithms/.leetcode/3090.maximum-length-substring-with-two-occurrences.cpp)