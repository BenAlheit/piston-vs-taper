import torch
from torch.utils.data import Dataset
from torch.autograd import Variable
from torch import nn

from computation.learning_pytorch.data_sets import CapContactDataset
from computation.learning_pytorch.nns import ContactClassification

import os

import scipy.optimize as op

import pandas as pd
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"


def train_nn(params):
    mid_dim, n_hidden = int(params[0]), int(params[1])
    model_path = f"./models/contact/contact_mid_dim_{mid_dim}_n_hidden_{n_hidden}.pth"
    print(model_path)

    dataset = CapContactDataset()
    batch_size = 1001
    n_iters = 10000

    check = 30
    epochs = n_iters / (len(dataset) / batch_size)
    input_dim = 3
    output_dim = 3
    lr_rate = 0.05

    n_changes = 5
    accuracies = [1.] * n_changes
    eps = 1e-8

    dset_loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=batch_size, shuffle=False)
    weights = torch.tensor(dataset.n_total / dataset.n_res, dtype=torch.float32)

    model = ContactClassification(input_dim,
                                  mid_dim,
                                  output_dim,
                                  dataset.translate,
                                  dataset.scale,
                                  n_hidden_layers=n_hidden)

    model.to(device)

    if os.path.exists(model_path):
        print('loading trained model')
        model.load_state_dict(torch.load(model_path))

    model.to(device)

    criterion = torch.nn.CrossEntropyLoss(weights).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr_rate)
    decayRate = 0.999
    scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer=optimizer, gamma=decayRate)

    model.train()
    iter = 0
    converged = False

    for epoch in range(int(epochs)):
        for i, (x, y) in enumerate(dset_loader):
            features = Variable(x)
            labels = Variable(y)
            features = features.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            outputs = model(features)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            iter += 1

            if epoch % check == 0:
                # calculate Accuracy
                correct = 0
                total = 0
                for x, y in dset_loader:
                    features = Variable(x)
                    features = features.to(device)
                    y = y.to(device)
                    outputs = model(features)
                    _, predicted = torch.max(outputs.data, 1)
                    total += y.size(0)
                    # for gpu, bring the predicted and labels back to cpu fro python operations to work
                    correct += (predicted == y).sum()
                accuracy = 100 * correct.cpu().detach() / total
                accuracy = accuracy.cpu().detach().numpy()
                model.accuracy = accuracy
                print("Epoch: {}. Loss: {}. Accuracy: {}.".format(epoch, loss.item(), accuracy))
                accuracies.pop()
                accuracies = [accuracy] + accuracies
                if np.all(np.abs(np.array(accuracies) - accuracy) < eps):
                    print("Optimization has converged!")
                    converged = True
        scheduler.step()

        if converged:
            torch.save(model.state_dict(), model_path)
            break

    return (100 - model.accuracy) ** 2


op.differential_evolution(train_nn,
                          bounds=((3, 10),
                                  (0, 10)),
                          workers=1,
                          polish=False,
                          updating='deferred',
                          disp=True)
