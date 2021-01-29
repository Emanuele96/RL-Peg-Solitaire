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
        print ("node: " + str(node.coordinates))
        if self.form == "diamond":
            possible_neighbors = ((0,-1),(-1,0),(-1,1),(0,1),(1,0),(1,-1))
            for possible_neighbor in possible_neighbors:
                tmp_coordinate = (node.coordinates[0] + possible_neighbor[0], node.coordinates[1] + possible_neighbor[1])
                print("tmp_coordinates: " + str(tmp_coordinate))
                if tmp_coordinate != node.coordinates and  tmp_coordinate[0] >=0 and tmp_coordinate[0] < self.size and tmp_coordinate[1] >= 0 and tmp_coordinate[1] < self.size:
                    if self.pawns[tmp_coordinate] not in node.neighbours:
                        node.neighbours.append(self.pawns[tmp_coordinate])
                        
        elif self.form == "triangle":
            possible_neighbors = ((-1,-1),(-1,0),(0,1),(1,1),(1,0),(0,-1))
            for possible_neighbor in possible_neighbors:
                tmp_coordinate = (node.coordinates[0] + possible_neighbor[0], node.coordinates[1] + possible_neighbor[1])
                if tmp_coordinate != node.coordinates and tmp_coordinate[0] >=0 and tmp_coordinate[0] < self.size and tmp_coordinate[1] >= 0 and tmp_coordinate[1] <= tmp_coordinate[0]:
                    if self.pawns[tmp_coordinate] not in node.neighbours:
                        node.neighbours.append(self.pawns[tmp_coordinate])

    def populate_board(self):
        for i in range(self.size):
            for j in range(i+1 if self.form == "triangle" else self.size):
                node = Node((i,j))   
                self.pawns[(i,j)] = node
        for coordinate in self.pawns:
            self.find_valid_neighbours(self.pawns[coordinate])
      
    def to_numpy_array(self):
        None



a = np.random.randint(1, 2, size=(10, 10))
print(a)
D = nx.Graph(a)
nx.draw(D, with_labels=True, font_weight='bold')
#plt.show()


board = Board("triangle", 4)
board.populate_board()
print(board.pawns)
for key in board.pawns:
    for neighbour in board.pawns[key].neighbours:
        print(str(key) + " : " + str(neighbour.coordinates))
print(board.pawns[(1,0)].neighbours)