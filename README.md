# Sorting Algorithms Analysis

## Escuela Colombiana de Ingeniería Julio Garavito  
**Author:** Sebastian Cardona Parra  
**Professor:** Rafael Alberto Niquefa Velasquez  
**2025-1**  

## Introduction
Finding the shortest path between nodes in a graph is a fundamental problem in computer science, with applications in networking, transportation, artificial intelligence, and more. This report analyzes three shortest path algorithms: Dijkstra, Bellman-Ford, and Floyd-Warshall, comparing their efficiency in terms of execution time and computational complexity.
## Algorithms

### Dijkstra's Algorithm
Dijkstra's algorithm finds the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative weights.
- **Worst case:** O(V^2) (using an adjacency matrix) or O((V + E) log V) (using a priority queue with a binary heap)
- **Best case:** O(V log V)
- **Average case:** O((V + E) log V)
- **Characteristics:** Efficient for graphs with non-negative weights but does not work with negative weight edges.

### Bellman-Ford Algorithm
Bellman-Ford computes the shortest paths from a single source vertex to all other vertices, allowing negative weight edges.
- **Worst case:** O(VE)  
- **Best case:** O(E)  
- **Average case:** O(VE)  
- **Characteristics:** Works with graphs containing negative weights but is slower than Dijkstra for large graphs.

### Floyd-Warshall Algorithm
Floyd-Warshall is an all-pairs shortest path algorithm that computes the shortest distances between every pair of vertices.
- **Worst case:** O(V^3)  
- **Best case:** O(V^3)  
- **Average case:** O(V^3)  
- **Characteristics:** Useful for dense graphs and small to medium-sized datasets but inefficient for large graphs.

## Performance Analysis
The algorithms were implemented in Python, and execution times were measured for different graph sizes. The results are presented in both line charts and bar charts for better visualization.


### Key Observations
- **Dijkstra's algorithm is efficient** for large graphs with non-negative weights, especially when using a priority queue.
- **Bellman-Ford is useful** for graphs with negative weights but scales poorly with large inputs.
- **Floyd-Warshall is useful for dense graphs** where all-pairs shortest paths are needed, but it does not scale well due to O(V^3) complexity.
- **Graph size and edge density significantly affect performance.**

## Conclusions
1. Dijkstra's algorithm is the best choice for finding the shortest path in graphs with non-negative weights.
2. Bellman-Ford is necessary when dealing with graphs that may have negative weights.
3. Floyd-Warshall is suitable for dense graphs or when all-pairs shortest paths are needed.
4. Algorithm selection depends on the problem's constraints, such as graph size, edge weights, and required path computations. 

## Coverage

The coverage of the tests is 97% as shown below:

to see the coverage of the tests, run the following command:
coverage run -m unittest discover
coverage report

```
Name                          Stmts   Miss  Cover
-------------------------------------------------
ShortPath\Graph.py               85      5    94%
ShortPath\__init__.py             0      0   100%
ShortPath\constants.py            4      0   100%
ShortPath\data_generator.py      27      0   100%
test\Test_data_generator.py      40      1    98%
test\__init__.py                  0      0   100%
test\test_graph.py               59      1    98%
-------------------------------------------------
TOTAL                           215      7    97%


```
## Graphics

The following graphics show the performance of the algorithms for different graph sizes:
![img.png](img%2Fimg.png)

![img_1.png](img%2Fimg_1.png)

![img_2.png](img%2Fimg_2.png)

we decided compare only dijkstra and bellman-ford because floyd-warshall is not efficient for large graphs.

![img_3.png](img%2Fimg_3.png)

![img_4.png](img%2Fimg_4.png)

We can see that Dijkstra's algorithm is the most efficient for large graphs with non-negative weights, while Bellman-Ford is slower but necessary for graphs with negative weights. Floyd-Warshall is useful for dense graphs but has higher execution times due to its O(V^3) complexity.

### With greater size of graph

![img_5.png](img%2Fimg_5.png)

![img_6.png](img%2Fimg_6.png)

definitely dijkstra is the best option for large graphs.

## Repository
This repository contains:
- **Python implementations** of Dijkstra, Bellman-Ford, and Floyd-Warshall algorithms.
- **Performance analysis scripts** to measure execution times.
- **Graphical comparisons** illustrating algorithm performance across different graph sizes.
