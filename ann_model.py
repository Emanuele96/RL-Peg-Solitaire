import torch
import torch.nn as nn 
#import torch.nn.functional as F

class Net(nn.Module):

    def __init__(self,input_size, layers_specs):
        super(Net, self).__init__()
        self.layers = nn.ModuleList()
        self.layers_specs = layers_specs
        self.input_size =  input_size
        current_dim = input_size
        for hidden_dimension in self.layers_specs:
            self.layers.append(nn.Linear(current_dim, hidden_dimension))
            current_dim = hidden_dimension

    def forward(self, x):
        for layer in self.layers:
            x = torch.tanh(layer(x))
        return x

