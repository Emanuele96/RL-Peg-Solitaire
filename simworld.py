import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import variables
class Node:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.neighbours = list(())

class Board:
    def __init__(self, form, size):
        self.form = form
        self.size = size
        self.pawns = {}
    
    def find_valid_neighbours(self,node):
        #find all possible neighbours using defined direction rules. Save thoose neighbours in the neighboard-list of the node as a tuple (direction, node)  
        print ("node: " + str(node.coordinates))
        if self.form == "diamond":
            possible_neighbors = ((0,-1),(-1,0),(-1,1),(0,1),(1,0),(1,-1))
            for possible_neighbor in possible_neighbors:
                tmp_coordinate = (node.coordinates[0] + possible_neighbor[0], node.coordinates[1] + possible_neighbor[1])
                print("tmp_coordinates: " + str(tmp_coordinate))
                if tmp_coordinate != node.coordinates and  tmp_coordinate[0] >=0 and tmp_coordinate[0] < self.size and tmp_coordinate[1] >= 0 and tmp_coordinate[1] < self.size:
                    if self.pawns[tmp_coordinate] not in node.neighbours:
                        node.neighbours.append((possible_neighbor,self.pawns[tmp_coordinate]))          
        elif self.form == "triangle":
            possible_neighbors = ((-1,-1),(-1,0),(0,1),(1,1),(1,0),(0,-1))
            for possible_neighbor in possible_neighbors:
                tmp_coordinate = (node.coordinates[0] + possible_neighbor[0], node.coordinates[1] + possible_neighbor[1])
                if tmp_coordinate != node.coordinates and tmp_coordinate[0] >=0 and tmp_coordinate[0] < self.size and tmp_coordinate[1] >= 0 and tmp_coordinate[1] <= tmp_coordinate[0]:
                    if self.pawns[tmp_coordinate] not in node.neighbours:
                        node.neighbours.append((possible_neighbor,self.pawns[tmp_coordinate]))

    def populate_board(self):
        for i in range(self.size):
            for j in range(i+1 if self.form == "triangle" else self.size):
                node = Node((i,j))   
                self.pawns[(i,j)] = node
        for coordinate in self.pawns:
            self.find_valid_neighbours(self.pawns[coordinate])
      
    def to_numpy_array(self):
        #Convert the board to a numpy array, so that can be visualized.
        #Generate a list of all nodes, this will be rows and columns for the adjacent matrix
        all_nodes = list(())
        for node in self.pawns.keys():
            all_nodes.append(node)
        print(all_nodes)
        adj_matrix = np.full((len(all_nodes), len(all_nodes)), 0, dtype=int)
        #Then iterate through every node (row) and for each neighbour, find the corrispondent index(column) and fill that box with 1.
        for i in range(len(all_nodes)):
            node = self.pawns[all_nodes[i]]
            for neighbour in node.neighbours:
                j = all_nodes.index(neighbour[1].coordinates)
                adj_matrix[i][j] = 1
        return adj_matrix




board = Board("triangle", 6)
board.populate_board()
print(board.pawns)
for key in board.pawns:
    for neighbour in board.pawns[key].neighbours:
        print(str(key) + " : " + str(neighbour[1].coordinates))
        print(neighbour)
print(board.pawns[(1,0)].neighbours)
a = board.to_numpy_array()
print(a)
D = nx.Graph(a)
nx.draw(D, with_labels=True, font_weight='bold')
plt.show()