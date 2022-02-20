import numpy as np
import sys

class Node:
    def __init__(self, state=None, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = 0

    def __str__(self):
        return str(self.state)

class GraphBFS:
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

    def search(self):
        while(len(self.queue) != 0):
            current = self.queue.pop(0)
            # check if arrive goal
            if(current.state == self.goal_state).all():
                print("Success")
                return self.generate_path(current)

            childs = self.find_child_nodes(current)
            for child in childs:
                # eliminate visited state
                if(str(child) not in self.visited):
                    self.add_node(child)
        else:
            print("Search fails")
            sys.exit(1)

    # after finding the goal, backtrack to find the path
    def generate_path(self, node):
        path = []
        # backtrack
        while(node.parent != None):
            path.append(node.state)
            node = node.parent
        path.append(self.init_state)
        path.reverse()

        for state in path:
            print(state)

        return path


