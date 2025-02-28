# Sorting Algorithms Analysis

## Escuela Colombiana de Ingeniería Julio Garavito  
**Author:** Sebastian Cardona Parra  
**Professor:** Rafael Alberto Niquefa Velasquez  
**2025-1**  

## Introduction
Sorting data is a fundamental task in computer science, and multiple algorithms have been developed to optimize this process. This report analyzes five sorting algorithms: **Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, and Counting Sort**, comparing their efficiency in terms of execution time and computational complexity.

## Algorithms

### Bubble Sort
A simple sorting algorithm that compares adjacent elements and swaps them into order. The process repeats until the entire list is sorted.

- **Worst case:** O(n²)  
- **Best case:** O(n)  
- **Average case:** O(n²)  
- **Characteristics:** Easy to understand but inefficient for large lists.

### Merge Sort
A recursive sorting algorithm following the **divide and conquer** paradigm. It splits the list into two parts, sorts them independently, and merges them.

- **Worst case:** O(n log n)  
- **Best case:** O(n log n)  
- **Average case:** O(n log n)  
- **Characteristics:** Efficient for large datasets but requires extra memory for sublists.

### Insertion Sort
Efficient for small lists. It assumes the first element is sorted and inserts subsequent elements correctly.

- **Worst case:** O(n²)  
- **Best case:** O(n)  
- **Average case:** O(n²)  
- **Characteristics:** Simple and effective for small, nearly sorted lists but inefficient for large lists.

### Quick Sort
An efficient sorting algorithm using **divide and conquer**. It selects a pivot, placing smaller elements before it and larger elements after, then sorts recursively.

- **Worst case:** O(n²) (when choosing the worst pivot)  
- **Best case:** O(n log n)  
- **Average case:** O(n log n)  
- **Characteristics:** Efficient for large datasets but depends on pivot selection.

### Counting Sort
Useful for sorting numbers within a **known and non-negative range**. Counts the frequency of elements and reconstructs the list.

- **Worst case:** O(n + k)  
- **Best case:** O(n + k)  
- **Average case:** O(n + k)  
- **Characteristics:** Efficient if the range is small compared to n, but inefficient if k is too large.

## Performance Analysis
The algorithms were implemented in Python, and execution times were measured for different dataset sizes.

***Please refer to the 'SortingAlgorithms.pdf' file for a detailed analysis of the results.***

### Key Observations
- **Bubble Sort and Insertion Sort** perform poorly for large lists due to O(n²) complexity.
- **Merge Sort and Quick Sort** perform better for large datasets with O(n log n) complexity.
- **Counting Sort** is highly efficient when the value range is close to the list size but loses efficiency when k is large.
- **List size directly affects performance**, with inefficient algorithms scaling exponentially in time.

## Conclusions
1. **Algorithm selection is crucial** depending on the dataset size and value distribution.
2. **Bubble Sort and Insertion Sort** should only be used for small datasets.
3. **Quick Sort and Merge Sort** are more suitable for large datasets.
4. **Counting Sort is effective** only if the maximum value is not significantly larger than the dataset size.
5. Understanding **computational complexity** helps in choosing the right algorithm for each case.

## Coverage

```
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
Sort\__init__.py                  0      0   100%
Sort\algorithms.py               59      2    97%   68-69
Sort\constants.py                 2      0   100%
Sort\data_generator.py            4      0   100%
test\__init__.py                  0      0   100%
test\test_algorithms.py          32      1    97%   53
test\test_data_generator.py      25      1    96%   32
-----------------------------------------------------------
TOTAL                           122      4    97%

```

## Repository
This repository contains:
- **Python implementations** of all sorting algorithms.
- **Performance analysis scripts**.
- **Graphs and comparisons in SortingAlgorithms.pdf**.
