
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/annealing.ipynb

from exp.nb_model import *
from torch.utils.data import DataLoader

from functools import partial

def create_learner(model_func, loss_func, data):
    return Learner(*model_func(data), loss_func, data)