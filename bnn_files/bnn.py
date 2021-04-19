# ----------------------------------------------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------------------------------------------

import blitz
import numpy as numpy
import torch as t
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from blitz.modules import BayesianLinear, BayesianConv1d
from blitz.utils import variational_estimator

# ----------------------------------------------------------------------------------------------------------------------
# Define Bayesian Neural Network
# ----------------------------------------------------------------------------------------------------------------------

@variational_estimator
class bnn(nn.Module):

    def __init__(self):
        super().__init__()
        
        self.dropout = nn.Dropout(0.5)
        self.conv1 = BayesianConv1d(1,16, 16)
        self.conv2 = BayesianConv1d(16,32, 8)
        self.conv3 = BayesianConv1d(32,64, 8)
        self.fc1   = BayesianLinear(3904, 64)
        self.fc2   = BayesianLinear(64, 1)
        self.batch_norm1 = nn.BatchNorm1d(num_features=16)
        self.batch_norm2 = nn.BatchNorm1d(num_features=32)
        self.batch_norm3 = nn.BatchNorm1d(num_features=64)
        self.batch_norm4 = nn.BatchNorm1d(num_features=64)

    def forward(self, x):
        
        out = self.conv1(x)
        out = F.relu(F.max_pool1d(out,4))
        out = self.batch_norm1(out)   
        out = self.conv2(out)
        out = F.relu(F.max_pool1d(out,4))
        out = self.batch_norm2(out)
        out = self.conv3(out)
        out = F.relu(F.max_pool1d(out,4))
        out = self.batch_norm3(out)
        out = out.view(out.size(0), -1)
        out = self.dropout(out)
        out = F.relu(self.fc1(out))
        out = self.batch_norm4(out)
        out = t.sigmoid(self.fc2(out))
        return out
    
    def reset(self):
        self.conv1.reset_parameters()
        self.conv2.reset_parameters()
        self.conv3.reset_parameters()
        self.fc1.reset_parameters()
        self.fc2.reset_parameters()
        self.fc3.reset_parameters()
