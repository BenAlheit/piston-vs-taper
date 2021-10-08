import torch
from torch.utils.data import Dataset
from torch.autograd import Variable
from torch import nn

import matplotlib.pyplot as plt
import computation.plotting_config

from computation.learning_pytorch.data_sets import CapElastoplasticDataset
from computation.learning_pytorch.nns import ElasticRegression1

import os

import scipy.optimize as op

import pandas as pd
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"

LR = 0.005
epochs = 100
DECAY_RATE = 0.99999

n_in = 3
n_out = 2
n_mid = 8
n_hidden = 0

line_width = 2
data_markers = None
pred_markers = None

data_set = CapElastoplasticDataset('../../data/cap/processed_test_data.csv')

x, y = Variable(data_set.x_data), Variable(data_set.y_data)
# torch.autograd.set_detect_anomaly(True)
model = ElasticRegression1(n_mid=n_mid, n_hidden_layers=n_hidden)

optimizer = torch.optim.Adam(model.parameters(), lr=LR)
loss_func = torch.nn.MSELoss()

scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer=optimizer, gamma=DECAY_RATE)


n_input_weights = n_mid * n_in
n_input_biases = n_mid

n_hidden_weights = n_mid * n_mid
n_hidden_biases = n_mid

n_output_weights = n_out * n_mid
n_output_biases = n_out


n_params = n_input_weights + n_input_biases \
    + (n_hidden_weights + n_hidden_biases)* n_hidden \
    + n_output_weights + n_output_biases


def set_model_params(params):
    start_pt = 0
    end_pt = n_input_weights
    model.input.weights = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt].reshape([n_mid, n_in])))

    start_pt += n_input_weights
    end_pt += n_input_biases
    model.input.bias = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt]))

    start_pt += n_input_biases
    for i in range(n_hidden):
        end_pt += n_hidden_weights
        model.hidden[i].weights = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt].reshape([n_mid, n_mid])))
        start_pt += n_hidden_weights

        end_pt += n_hidden_biases
        model.hidden[i].bias = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt]))
        start_pt += n_hidden_biases

    end_pt += n_output_weights
    model.output.weight = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt].reshape([n_out, n_mid])))

    start_pt += n_output_weights
    end_pt += n_output_biases
    model.output.bias = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt]))


def obj(params):
    set_model_params(params)
    prediction = model(x)
    loss = loss_func(prediction, y)

    return loss.item()


res = op.differential_evolution(obj,
                          bounds=((-3, 3),)*n_params,
                          workers=1,
                          polish=False,
                          updating='deferred',
                          disp=True)

set_model_params(res.x)

#
# for t in range(epochs):
#     print(f"Epoch {t + 1}\n-------------------------------")
#     prediction = model(x)
#     loss = loss_func(prediction, y)
#     print(f"epoch = {t}   loss = {loss.item():.4e}")
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()
#     scheduler.step()
#
#     print()

model.eval()
pred = model(x).detach().numpy()
y_dat = y.detach().numpy()
data = data_set.elastic_contact_data
plt.plot(data['time (s)'], pred[:, 0], label='Model', linewidth=line_width, marker=pred_markers)
plt.plot(data['time (s)'], y_dat[:, 0], label='Data', linewidth=line_width, marker=data_markers)
plt.ylabel('Force (N)')
plt.xlabel('Time (s)')
plt.grid()
plt.legend()
plt.tight_layout()

plt.figure()
plt.plot(data['time (s)'], pred[:, 1], label='Model', linewidth=line_width, marker=pred_markers)
plt.plot(data['time (s)'], y_dat[:, 1], label='Data', linewidth=line_width, marker=data_markers)
plt.ylabel('PD rate (N)')
plt.xlabel('Time (s)')
plt.grid()
plt.legend()
plt.tight_layout()

plt.show()
a=0
#
# op.differential_evolution(train_nn,
#                           bounds=((3, 10),
#                                   (0, 10)),
#                           workers=1,
#                           polish=False,
#                           updating='deferred',
#                           disp=True)
