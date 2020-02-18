# Earliest Ancestor

This is a take-home coding challenge from a top tech company. The spec is providied verbatim.


## Problem

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram and the sample input, 3 is a child of 1 and 2, and 5 is a child of 4:

```
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
```

Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.




/////MY NOTES /////
"Earliest known" tells me 'opposite of a breadth-first traversal'...
Graph is directed b/c I'm only interested in one direction- the parents of whichever node's selected.
Acyclic, and unweighted and sparse.

1) This is a graph problem for sure. 
      My nodes are #'s of each person...edges are the parent/child relationship.

2) build this data into a graph
      ...how? need to wrap each in a node & link to each other...can't remember how

3) traverse the graph
      DFS most likely. Iterative.





```
Example input
  6

  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10
```

Clarifications:
* The input will not be empty.
* There are no cycles in the input.
* There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
* IDs will always be positive integers.
* A parent may have any number of children.

