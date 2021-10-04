import torch
from torch.utils.data import Dataset
from torch.autograd import Variable
from torch import nn

import os

import scipy.optimize as op

import pandas as pd
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"


def train_nn(params):
    mid_dim, n_hidden = int(params[0]), int(params[1])
    model_path = f"./models/contact/contact_mid_dim_{mid_dim}_n_hidden_{n_hidden}.pth"
    print(model_path)

    class CapDataset(Dataset):

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
            self.x_data = torch.tensor(tmp_x, dtype=torch.float32).to(device)
            self.y_data = torch.tensor(tmp_y.flatten(), dtype=torch.long).to(device)

        def __len__(self):
            return len(self.x_data)

        def __getitem__(self, idx):
            features = self.x_data[idx, :]
            values = self.y_data[idx]
            return features, values

    class NeuralNetwork(nn.Module):
        def __init__(self, input_dim, mid_dim, output_dim, x_translation, x_scale, n_hidden_layers=1):
            super(NeuralNetwork, self).__init__()

            self.x_translation = x_translation
            self.x_scale = x_scale

            self.input = nn.Linear(input_dim, mid_dim)
            torch.nn.init.xavier_uniform_(self.input.weight)
            torch.nn.init.zeros_(self.input.bias)

            self.output = nn.Linear(mid_dim, output_dim)
            torch.nn.init.xavier_uniform_(self.output.weight)
            torch.nn.init.zeros_(self.output.bias)

            self.hidden = [torch.nn.Linear(mid_dim, mid_dim) for i in range(n_hidden_layers)]
            self.n_hidden_layers = n_hidden_layers
            for i in range(n_hidden_layers):
                self.hidden[i].to(device)
                torch.nn.init.xavier_uniform_(self.hidden[i].weight)
                torch.nn.init.zeros_(self.hidden[i].bias)

            self.sigmoid = nn.Sigmoid()
            self.softmax = nn.Softmax(1)

            self.accuracy = 0

        def forward(self, x):
            x = self.input(x)
            x = self.sigmoid(x)

            for i in range(self.n_hidden_layers):
                x = self.hidden[i](x)
                x = self.hidden[i](x)

            x = self.output(x)
            x = self.sigmoid(x)
            x = self.softmax(x)

            return x

        def predict(self, x):
            x = x * self.x_scale + self.x_translation
            return self(x)

    dataset = CapDataset()

    batch_size = 1001
    n_iters = 10000

    check = 30
    epochs = n_iters / (len(dataset) / batch_size)
    input_dim = 3
    output_dim = 3
    lr_rate = 0.1

    n_changes = 5
    accuracies = [1.] * n_changes
    eps = 1e-8

    dset_loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=batch_size, shuffle=False)
    weights = torch.tensor(dataset.n_total / dataset.n_res, dtype=torch.float32)

    model = NeuralNetwork(input_dim,
                          mid_dim,
                          output_dim,
                          dataset.translate,
                          dataset.scale,
                          n_hidden_layers=n_hidden)

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
                          bounds=((3, 300),
                                  (0, 300)),
                          workers=1,
                          polish=False,
                          updating='deferred',
                          disp=True)
