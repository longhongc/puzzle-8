import numpy as np
import sys
from utils import *

class Node:
    def __init__(self, state=None, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __str__(self):
        return str(self.state)

    def __lt__(self, other): 
        return self.cost < other.cost

    def __gt__(self, other): 
        return self.cost > other.cost

class Graph: 
    def __init__(self, init_state, goal_state):
        self.queue = []
        # use set for faster checking visited 
        self.visited = set()

        init_node = Node(state=init_state)
        self.add_node(init_node)

        self.init_state = init_state
        self.goal_state = goal_state

    def add_node(self, node):
        self.queue.append(node)
        self.visited.add(str(node))

    def find_child_nodes(self, node):
        # find the position of blank tile
        i, j = np.where(node.state==0)

        # [up, down, left, right]
        actions = [(-1,0), (1,0), (0,-1), (0,1)]

        childs = []
        for action in actions:
            new_i = i+action[0] 
            new_j = j+action[1]
            if(new_i<=2 and new_i>=0 and
               new_j<=2 and new_j>=0):
                child_state = node.state.copy()
                child_state[(i,j)], child_state[(new_i,new_j)] = \
                    child_state[(new_i,new_j)], child_state[(i,j)]
                child = Node(state=child_state, parent=node, cost=node.cost+1)
                childs.append(child)

        return childs

    # after finding the goal, backtrack to find the path
    def generate_path(self, node):
        path = []
        # backtrack
        while(node.parent != None):
            path.append(node.state)
            node = node.parent
        path.append(self.init_state)
        path.reverse()

        print("Solution steps: ", len(path))

        # for state in path:
        #     print(state)
        #

        return path

class GraphBFS(Graph):
    def __init__(self, init_state, goal_state):
        Graph.__init__(self, init_state, goal_state)

    def search(self):
        while(len(self.queue) != 0):
            run_spinning_cursor()
            # BFS use queue
            current = self.queue.pop(0)
            # check if arrive goal
            if(current.state == self.goal_state).all():
                print("Success")
                print("Search nodes: ", len(self.visited))
                return self.generate_path(current)

            childs = self.find_child_nodes(current)
            for child in childs:
                # eliminate visited state
                if(str(child) not in self.visited):
                    self.add_node(child)
        else:
            print("Search fails")
            sys.exit(1)

class GraphDFS(Graph):
    def __init__(self, init_state, goal_state):
        Graph.__init__(self, init_state, goal_state)

    def search(self):
        while(len(self.queue) != 0):
            run_spinning_cursor()
            # DFS use stack
            current = self.queue.pop()
            # check if arrive goal
            if(current.state == self.goal_state).all():
                print("\nSuccess")
                print("Search nodes: ", len(self.visited))
                return self.generate_path(current)

            childs = self.find_child_nodes(current)
            for child in childs:
                # eliminate visited state
                if(str(child) not in self.visited):
                    self.add_node(child)
        else:
            print("Search fails")
            sys.exit(1)

class GraphAStar(Graph):
    def __init__(self, init_state, goal_state):
        Graph.__init__(self, init_state, goal_state)

    def add_node(self, node, h_cost=0):
        self.queue.append((h_cost, node))
        self.visited.add(str(node))

    def heuristic(self, node): 
        C = node.cost
        G = 0
        for num in range(1, 6):  
            i, j = np.where(node.state==num)
            gi, gj = np.where(self.goal_state==num)
            G += abs(gi-i) + abs(gj-j)

        return C + G

    def search(self):
        while(len(self.queue) != 0):
            run_spinning_cursor()

            # AStar pick the loweset C+G cost 
            self.queue = sorted(self.queue)
            current = self.queue.pop(0)[1]

            # check if arrive goal
            if(current.state == self.goal_state).all():
                print("\nSuccess")
                print("Search nodes: ", len(self.visited))
                return self.generate_path(current)

            childs = self.find_child_nodes(current)
            for child in childs:
                # eliminate visited state
                if(str(child) not in self.visited):
                    h_cost = self.heuristic(child)
                    self.add_node(child, h_cost)
        else:
            print("Search fails")
            sys.exit(1)


