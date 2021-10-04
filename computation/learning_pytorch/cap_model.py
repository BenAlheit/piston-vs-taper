import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset


class CustomCapDataset(Dataset):
    