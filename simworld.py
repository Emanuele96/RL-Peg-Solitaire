import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image
import io
import variables
class Node:
    def __init__(self, coordinates, is_empty):
        self.coordinates = coordinates
        self.neighbours = list(())
        self.is_empty = is_empty
    
    def empty_the_node(self):
        self.is_empty = True
class Board:
    def __init__(self, form, size, empty_nodes):
        self.form = form
        self.size = size
        self.empty_nodes = empty_nodes
        self.pawns = {}
        self.populate_board()
        self.graph = self.generate_graph()
    
    def find_valid_neighbours(self,node):
        #find all possible neighbours using defined direction rules. Save thoose neighbours in the neighboard-list of the node as a tuple (direction, node)  
        if variables.debug:
            print ("node: " + str(node.coordinates))
        if self.form == "diamond":
            possible_neighbors = ((0,-1),(-1,0),(-1,1),(0,1),(1,0),(1,-1))
            for possible_neighbor in possible_neighbors:
                tmp_coordinate = (node.coordinates[0] + possible_neighbor[0], node.coordinates[1] + possible_neighbor[1])
                if variables.debug:
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
                is_empty = False
                if (i,j) in self.empty_nodes:
                    is_empty = True
                node = Node((i,j), is_empty)   
                self.pawns[(i,j)] = node
        for coordinate in self.pawns:
            self.find_valid_neighbours(self.pawns[coordinate])
      
    def to_numpy_array(self):
        #Convert the board to a numpy array, so that can be visualized.
        #Generate a list of all nodes, this will be rows and columns for the adjacent matrix
        all_nodes = list(())
        for node in self.pawns.keys():
            all_nodes.append(node)
        if variables.debug:
            print(all_nodes)
        adj_matrix = np.full((len(all_nodes), len(all_nodes)), 0, dtype=int)
        #Then iterate through every node (row) and for each neighbour, find the corrispondent index(column) and fill that box with 1.
        for i in range(len(all_nodes)):
            node = self.pawns[all_nodes[i]]
            for neighbour in node.neighbours:
                j = all_nodes.index(neighbour[1].coordinates)
                adj_matrix[i][j] = 1
        return adj_matrix

    def generate_graph(self):
        adj_matrix = self.to_numpy_array()
        G = nx.Graph(adj_matrix)
        #Add node attributes for "coordinate" and "is_empty", taken from board "pawns" dictionary
        all_nodes = list(())
        for node in self.pawns.keys():
            all_nodes.append(node)
        for i in range(adj_matrix.shape[0]):
            G.add_node(i, is_empty = self.pawns[all_nodes[i]].is_empty, diamond_plan = all_nodes[i][0] + all_nodes[i][1], triangle_plan =  all_nodes[i][0] )
        if variables.debug:
            print(adj_matrix)
            print(G.nodes.data())
        return G

    def show_board(self):
        #Plot the graph nodes and edges  with regards of plans (1 different plan per row), then do the necessary flipping and rotation for matching the board to the assigment
        if self.form == "diamond":
            rotation = 180
            plan_key = "diamond_plan"
        elif self.form == "triangle":
            rotation = 180
            plan_key = "triangle_plan"
        position = nx.multipartite_layout(self.graph, subset_key=plan_key, align="horizontal", center=[0,5])
        #Decide the color of each node, based on if it is empty or not
        nodes_color = []
        nodes = list(self.graph.nodes.data("is_empty"))
        for node in nodes:
            if node[1] == True:                
                nodes_color.append("#ffffff")
            else:
                nodes_color.append("#000000")
        
        options = {'node_size': 400,'width': 1, 'pos' : position, 'with_labels':False, 'font_weight':'bold', 'node_color': nodes_color, 'linewidths':5}
        nx.draw(self.graph, **options )
        #outline each node and specify linewidt to show an empty node. ax.collection is the path collection of matplotlib.
        # documentation :  https://matplotlib.org/3.3.3/api/collections_api.html
        ax = plt.gca()
        ax.collections[0].set_edgecolor("#000000") 
        ax.collections[0].set_linewidth(2)
        fig = plt.gcf()
        img = self.matplotlib_to_pil(fig)
        img = img.rotate(rotation)
        if self.form == "diamond":
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        plt.clf()
        img.show()
        

    def matplotlib_to_pil(self, fig):
        #Convert a Matplotlib object to an PIL Image   
        bufffer = io.BytesIO()
        fig.savefig(bufffer)
        bufffer.seek(0)
        return Image.open(bufffer)



if variables.debug:
    print(board.pawns)
    for key in board.pawns:
        for neighbour in board.pawns[key].neighbours:
            print(str(key) + " : " + str(neighbour[1].coordinates))
            print(neighbour)
    print(board.pawns[(1,0)].neighbours)
