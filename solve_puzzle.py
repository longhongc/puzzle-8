import numpy as np
import sys
import argparse
from random import *

# My library
from algorithm import *
from utils import *

class Puzzle:
    def __init__(self, init_state=None):
        self.init = init_state
        self.goal = np.array([[1,2,3],
                              [4,5,6],
                              [7,8,0]])

        print("Create puzzle")

        if(type(self.init)==type(None)): 
            self.create_random_puzzle()
        self.print_init_goal()

    def print_init_goal(self):
        print("  Start")
        print(self.init)
        print("   Goal")
        print(self.goal)

    def create_random_puzzle(self):
        self.init = self.goal.copy()
        i, j = np.where(self.init==0)

        # [up, down, left, right]
        actions = [(-1,0), (1,0), (0,-1), (0,1)]

        steps = randrange(30, 50)
        print("Create steps: ", steps)

        for _ in range(0, steps):
            run_spinning_cursor()
            action = actions[randrange(0, 4)]
            new_i = i+action[0] 
            new_j = j+action[1]
            if(new_i<=2 and new_i>=0 and
               new_j<=2 and new_j>=0):
                self.init[(i,j)], self.init[(new_i,new_j)] = \
                    self.init[(new_i,new_j)], self.init[(i,j)]
                i, j = new_i, new_j
        
    def solve(self, algo):
        print("Start puzzle")

        if algo == "BFS": 
            graph = GraphBFS(self.init, self.goal)
        if algo == "DFS": 
            graph = GraphDFS(self.init, self.goal)
        if algo == "AStar": 
            graph = GraphAStar(self.init, self.goal)

        solution = graph.search()

        return solution

def parse_input(input_str):
    input_lst = [int(i) for i in input_str]
    init_state = np.array(input_lst).reshape(3,3)

    return init_state

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algorithm", help="Choose a search algorithm from [BFS, DFS, AStar]", \
                           choices=["BFS", "DFS", "AStar"], default="BFS")
    parser.add_argument("-i", "--initial", help="Choose a initial puzzle state, \
                                                 default is random initial puzzle")
    parser.add_argument("-p", "--print", help="Print out the solution", action="store_true")
    args = parser.parse_args()

    # if (len(sys.argv) != 3):
    #     print("Please enter an argument (column wise)!!")
    #     print("Example: python3 solve_puzzle.py 147028356 BFS")
    #     sys.exit(1)
    #
    # algos = ["BFS", "DFS", "A*"]

    init_state = None
    if args.initial != None:
        init_state = parse_input(args.initial)
    
    algo = args.algorithm

    my_puzzle = Puzzle(init_state)
    sol = my_puzzle.solve(algo)

    if args.print: 
        for state in sol:
            print(state)
        


