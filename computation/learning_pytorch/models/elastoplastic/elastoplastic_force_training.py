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

n_in = 3
n_out = 2

line_width = 2
data_markers = None
pred_markers = None


def plot_results(model, x, y, data_set):
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


def train_regression_model(params,
                           data_set=CapElastoplasticDataset('../../data/cap/processed_test_data.csv'),
                           plot=False):
    n_mid, n_hidden = int(params[0]), int(params[1])

    print('-----------------')
    print(f'Params: n_mid={n_mid}, n_hidden={n_hidden}')
    x, y = Variable(data_set.x_data), Variable(data_set.y_data)
    model_path = f"./trained/elastoplastic_mid_dim_{n_mid}_n_hidden_{n_hidden}.pth"

    loss_func = torch.nn.MSELoss()
    model = ElasticRegression1(n_mid=n_mid, n_hidden_layers=n_hidden)

    n_input_weights = n_mid * n_in
    n_input_biases = n_mid

    n_hidden_weights = n_mid * n_mid
    n_hidden_biases = n_mid

    n_output_weights = n_out * n_mid
    n_output_biases = n_out

    n_params = n_input_weights + n_input_biases \
        + (n_hidden_weights + n_hidden_biases) * n_hidden \
        + n_output_weights + n_output_biases

    def set_model_params(model, params):
        start_pt = 0
        end_pt = n_input_weights
        model.input.weight = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt].reshape([n_mid, n_in])))

        start_pt += n_input_weights
        end_pt += n_input_biases
        model.input.bias = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt]))

        start_pt += n_input_biases
        for i in range(n_hidden):
            end_pt += n_hidden_weights
            model.hidden[i].weight = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt].reshape([n_mid, n_mid])))
            start_pt += n_hidden_weights

            end_pt += n_hidden_biases
            model.hidden[i].bias = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt]))
            start_pt += n_hidden_biases

        end_pt += n_output_weights
        model.output.weight = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt].reshape([n_out, n_mid])))

        start_pt += n_output_weights
        end_pt += n_output_biases
        model.output.bias = torch.nn.Parameter(torch.Tensor(params[start_pt:end_pt]))

    def get_loss(x):
        prediction = model(x)

        loss = loss_func(prediction, y)

        return loss.item()

    def obj(params):
        set_model_params(model, params)
        return get_loss(x)

    if os.path.exists(model_path):
        print(f'Loading trained model: {model_path}')
        state_dict = torch.load(model_path)
        model.load_state_dict(state_dict)
        if plot:
            plot_results(model, x, y, data_set)

        return get_loss(x)

    res = op.differential_evolution(obj,
                              bounds=((-3, 3),)*n_params,
                              workers=1,
                              polish=False,
                              updating='deferred',
                              disp=True)

    set_model_params(model, res.x)
    torch.save(model.state_dict(), model_path)
    plot_results(model, x, y, data_set)
    return get_loss(x)


res = op.differential_evolution(train_regression_model,
                          bounds=((3, 10),
                                  (0, 5)),
                          workers=1,
                          polish=False,
                          updating='deferred',
                          disp=True)

print(f'Opt params = {res.x}')

train_regression_model(res.x, plot=True)

