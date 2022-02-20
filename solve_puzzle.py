import numpy as np
import sys
from algorithm import *

class Puzzle:
    def __init__(self, init_state):
        self.init = init_state
        self.goal = np.array([[1,2,3],
                              [4,5,6],
                              [7,8,0]])
        
    def solve(self):
        graph = GraphBFS(self.init, self.goal)
        solution = graph.search()

        return solution

def parse_input(input_str):
    input_lst = [int(i) for i in input_str]
    init_state = np.array(input_lst).reshape(3,3)

    return init_state

if __name__ == "__main__":
    print("Start puzzle")
    if (len(sys.argv) != 2):
        print("Please enter an argument (column wise)!!")
        print("Example: python3 solve_puzzle.py 147028356")
        sys.exit(1)

    init_state = parse_input(sys.argv[1])

    # Example init_state
    # init_state = np.array([[1,0,3],
    #                        [4,2,5],
    #                        [7,8,6]])

    # init_state = np.array([[1,5,2],
    #                        [4,0,3],
    #                        [7,8,6]])

    # init_state = np.array([[4,1,3],
    #                        [7,2,5],
    #                        [0,8,6]])

    my_puzzle = Puzzle(init_state)
    sol = my_puzzle.solve()


