import torch
from torch import functional as F
from torch.optim import Optimizer

class Optimizer_with_eligibility(Optimizer):

    def __init__(self):
        self.one = 1

    @torch.no_grad()
    def step(self, closure=None):
        return -1