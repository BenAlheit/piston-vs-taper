import torch
from torch.utils.data import Dataset
from torch.autograd import Variable
from torch import nn

import os

import pandas as pd
import numpy as np


class CapElastoplasticDataset(Dataset):

    def __init__(self, src_file='./computation/learning_pytorch/data/cap/processed_test_data.csv'):
        print(os.getcwd())
        data = pd.read_csv(src_file)
        data_contact_elastic_logic = (data['contact'] == 1) & (data['elastoplastic'] == 1)
        elastic_contact_data = data.loc[data_contact_elastic_logic]
        self.elastic_contact_data = elastic_contact_data
        tmp_x = elastic_contact_data[['x_t (mm)', 'plastic dissipation (mJ)', 'v_t (mm/s)']].to_numpy().astype(np.float32)
        # tmp_x = data[['x_t (mm)', 'plastic dissipation (mJ)', 'v_t (mm/s)']].to_numpy().astype(np.float32)
        self.translate = np.min(tmp_x, axis=0)
        tmp_x -= self.translate
        self.scale = np.max(tmp_x, axis=0)
        tmp_x /= self.scale
        tmp_y = elastic_contact_data[['force (N)', 'plastic dissipation rate (mJ/s)']].to_numpy().astype(np.float32)
        self.translate_y = np.min(tmp_y, axis=0)
        tmp_y -= self.translate_y
        self.scale_y = np.max(tmp_y, axis=0)
        tmp_y /= self.scale_y
        self.x_data = torch.tensor(tmp_x, dtype=torch.float32)
        self.y_data = torch.tensor(tmp_y, dtype=torch.float32)

    def __len__(self):
        return len(self.x_data)

    def __getitem__(self, idx):
        features = self.x_data[idx, :]
        values = self.y_data[idx, :]
        return features, values


class CapElasticDataset(Dataset):

    def __init__(self, src_file='./computation/learning_pytorch/data/cap/processed_test_data.csv'):
        print(os.getcwd())
        data = pd.read_csv(src_file)
        data_contact_elastic_logic = (data['contact'] == 1) & (data['elastoplastic'] == 0)
        elastic_contact_data = data.loc[data_contact_elastic_logic]
        self.elastic_contact_data = elastic_contact_data
        tmp_x = elastic_contact_data[['x_t (mm)', 'plastic dissipation (mJ)', 'v_t (mm/s)']].to_numpy().astype(np.float32)
        # tmp_x = data[['x_t (mm)', 'plastic dissipation (mJ)', 'v_t (mm/s)']].to_numpy().astype(np.float32)
        self.translate = np.min(tmp_x, axis=0)
        tmp_x -= self.translate
        self.scale = np.max(tmp_x, axis=0)
        tmp_x /= self.scale
        tmp_y = elastic_contact_data[['force (N)', 'plastic dissipation rate (mJ/s)']].to_numpy().astype(np.float32)
        self.translate_y = np.min(tmp_y, axis=0)
        tmp_y -= self.translate_y
        self.scale_y = np.max(tmp_y, axis=0)
        tmp_y /= self.scale_y
        self.x_data = torch.tensor(tmp_x, dtype=torch.float32)
        self.y_data = torch.tensor(tmp_y, dtype=torch.float32)

    def __len__(self):
        return len(self.x_data)

    def __getitem__(self, idx):
        features = self.x_data[idx, :]
        values = self.y_data[idx, :]
        return features, values


class CapContactDataset(Dataset):

        def __init__(self, src_file='./data/cap/processed_test_data.csv'):
            data = pd.read_csv(src_file)
            tmp_x = data[['x_t (mm)', 'plastic dissipation (mJ)', 'v_t (mm/s)']].to_numpy().astype(np.float32)
            self.translate = np.min(tmp_x, axis=0)
            tmp_x -= self.translate
            self.scale = np.max(tmp_x, axis=0)
            tmp_x /= self.scale
            tmp_y = data[['contact', 'elastoplastic']].to_numpy().astype(np.float32)
            tmp_y = tmp_y[:, 0] + tmp_y[:, 1]
            self.n_res = np.array([np.sum(np.isclose(tmp_y, i)) for i in range(3)])
            self.n_total = self.n_res.sum()
            self.x_data = torch.tensor(tmp_x, dtype=torch.float32)
            self.y_data = torch.tensor(tmp_y.flatten(), dtype=torch.long)

        def __len__(self):
            return len(self.x_data)

        def __getitem__(self, idx):
            features = self.x_data[idx, :]
            values = self.y_data[idx]
            return features, values
