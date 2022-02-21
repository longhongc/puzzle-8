# puzzle-8
This program tests different search algorithms to solve the 8 puzzle.

The goal of the 8 puzzle is arrange the number in the puzzle as below.
```
   [1 2 3]  
   [4 5 6]  
   [7 8 0]  
```
Zero stands for an empty tile.   
All the numbers on the puzzle can be move to the empty tile if they are on the side of it.  

## Run
Start random puzzle
```
python3 solve_puzzle.py -a AStar -p
```

Start with specific puzzle
```
python3 solve_puzzle.py -a BFS -i 135470826 -p
```
The initial state is formatted from row to column.   
For example: 135470826 is   
```
   [1 3 5]  
   [4 7 0]  
   [8 2 6]  
```
Check for all options  
```
python3 solve_puzzle.py -h
```
### Options
`-a` select algorithm from BFS, DFS, AStar. Default is BFS.   
`-p` print out all the solution state  
`-i` select a specific initial state, initial state is random if didn't select this option

## Algorithms
### BFS
BFS calculates the optimal solution by traveling all the node and its childs in a queue order. 
### DFS
DFS calculates the solution by traveling all the node and its childs in a stack order.   
### A*
A* star calculates the optimal solution by sorting the nodes with the h-cost value.   
H-cost value equals cost-to-come + cost-to-go  
### Comparison
```
    Start     goal
   [1 3 5]   [1 2 3]
   [4 7 0]   [4 5 6]
   [8 2 6]   [7 8 0]
```
|  | BFS | DFS |A\*|
| ------------ | ------------- |-------------|-------------|
|Searched nodes|  3789  |180357 | 98 |
|Solution steps|  14   |22294| 14 |
