import torch
from torch.utils.data import Dataset
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import os

# device = "cuda" if torch.cuda.is_available() else "cpu"
device = 'cpu'
data = pd.read_csv('../data/cap/processed_test_data.csv')


class CapDataset(Dataset):

    def __init__(self, src_file='processed_test_data.csv', m_rows=None):
      data = pd.read_csv(src_file)
      tmp_x = data[['x_t (mm)', 'plastic dissipation (mJ)', 'v_t (mm/s)']].to_numpy().astype(np.float32)
      tmp_y = data[['force (N)', 'plastic dissipation rate (mJ/s)']].to_numpy().astype(np.float32)
      self.x_data = torch.tensor(tmp_x, dtype=torch.float32).to(device)
      self.y_data = torch.tensor(tmp_y, dtype=torch.float32).to(device)

    def __len__(self):
        return len(self.x_data)

    def __getitem__(self, idx):
        features = self.x_data[idx, :]  # or just [idx]
        values = self.y_data[idx, :]
        return features, values  # tuple of matrices


class CleverNet(torch.nn.Module):
    def __init__(self, n_in=3, n_mid=3, n_hidden_layers=0, n_out=2):
        super(CleverNet, self).__init__()
        self.position_activation_linear = torch.nn.Linear(3, 1)  # 8-(10-10)-1
        torch.nn.init.xavier_uniform_(self.position_activation_linear.weight)
        torch.nn.init.zeros_(self.position_activation_linear.bias)

        self.velocity_activation_linear = torch.nn.Linear(3, 2)  # 8-(10-10)-1
        torch.nn.init.xavier_uniform_(self.velocity_activation_linear.weight)
        torch.nn.init.zeros_(self.velocity_activation_linear.bias)

        # self.position_activation_bilinear = torch.nn.Bilinear(3, 3, 3)  # 8-(10-10)-1
        # torch.nn.init.xavier_uniform_(self.position_activation_bilinear.weight)
        # torch.nn.init.zeros_(self.position_activation_bilinear.bias)

        # self.velocity_activation_bilinear = torch.nn.Bilinear(3, 3, 3)  # 8-(10-10)-1
        # torch.nn.init.xavier_uniform_(self.velocity_activation_bilinear.weight)
        # torch.nn.init.zeros_(self.velocity_activation_bilinear.bias)

        self.combination = torch.nn.Bilinear(1, 2, 2)
        torch.nn.init.xavier_uniform_(self.combination.weight)
        torch.nn.init.zeros_(self.combination.bias)

    def forward(self, x):
        z1 = torch.relu(self.position_activation_linear(x))
        z2 = torch.relu(self.velocity_activation_linear(x))
        z = self.combination(z1, z2)
        z = torch.relu(z)
        return z


class Net(torch.nn.Module):
    def __init__(self, n_in=3, n_mid=3, n_hidden_layers=0, n_out=2):
        super(Net, self).__init__()
        self.n_hidden = n_hidden_layers
        self.layer_1 = torch.nn.Linear(n_in, n_mid)  # 8-(10-10)-1
        self.hidden = [torch.nn.Linear(n_mid, n_mid) for i in range(n_hidden_layers)]
        self.oupt = torch.nn.Linear(n_mid, n_out)

        torch.nn.init.xavier_uniform_(self.layer_1.weight)
        torch.nn.init.zeros_(self.layer_1.bias)
        for i in range(n_hidden_layers):
            torch.nn.init.xavier_uniform_(self.hidden[i].weight)
            torch.nn.init.zeros_(self.hidden[i].bias)
        torch.nn.init.xavier_uniform_(self.oupt.weight)
        torch.nn.init.zeros_(self.oupt.bias)

    def forward(self, x):
        z = torch.relu(self.layer_1(x))
        for i in range(self.n_hidden):
            z = torch.relu(self.hidden[i](z))

        z = torch.relu(self.oupt(z))
        return z


def accuracy(model, ds, pct):
  # assumes model.eval()
  # percent correct within pct of true house price
  n_correct = 0; n_wrong = 0

  for i in range(len(ds)):
    (X, Y) = ds[i]            # (predictors, target)
    with torch.no_grad():
      oupt = model(X)         # computed price

    abs_delta = np.linalg.norm(oupt.cpu() - Y.cpu())
    max_allow = np.linalg.norm(pct * Y.cpu())
    if abs_delta < max_allow:
      n_correct +=1
    else:
      n_wrong += 1

  acc = (n_correct * 1.0) / (n_correct + n_wrong)
  return acc

def main():
    # 0. get started
    print("\nBegin predict cap force \n")
    # torch.manual_seed(4)  # representative results
    # np.random.seed(4)

    # 1. create DataLoader objects
    print("Creating Cap Dataset objects ")

    test_ds = CapDataset()  # all 40 rows
    train_ds = CapDataset()  # all 40 rows

    bat_size = 100
    train_ldr = torch.utils.data.DataLoader(train_ds, batch_size=bat_size, shuffle=True)
    n_mid = 10000
    n_hidden = 10000

    # 2. create network
    # net = Net().to(device)

    # fn = f".cap_model_clevernet_re_smaller.pth"
    fn = f".cap_model_drop_n_mid_{n_mid}_n_hidden{n_hidden}.pth"
    net = Net()
    # if os.path.exists(fn):
    #     print('loading trained model')
    #     net.load_state_dict(torch.load(fn))

    # 3. train model
    max_epochs = 500000
    ep_log_interval = 100
    lrn_rate = 0.05

    loss_func = torch.nn.MSELoss()
    # optimizer = torch.optim.SGD(net.parameters(), lr=lrn_rate)
    optimizer = torch.optim.Adam(net.parameters(), lr=lrn_rate)
    # optimizer = torch.optim.Adam(net.parameters())

    print("\nbat_size = %3d " % bat_size)
    print("loss = " + str(loss_func))
    print("optimizer = Adam")
    print("max_epochs = %3d " % max_epochs)
    print("lrn_rate = %0.3f " % lrn_rate)

    print("\nStarting training with saved checkpoints")
    net.train()  # set mode
    for epoch in range(0, max_epochs):
        # torch.manual_seed(1 + epoch)  # recovery reproducibility
        epoch_loss = 0  # for one full epoch

        for (batch_idx, batch) in enumerate(train_ldr):
            (X, Y) = batch  # (predictors, targets)
            X, Y = X.to(device), Y.to(device)
            optimizer.zero_grad()  # prepare gradients
            oupt = net(X)  # predicted prices
            loss_val = loss_func(oupt, Y)  # avg per item in batch
            epoch_loss += loss_val.item()  # accumulate avgs
            loss_val.backward()  # compute gradients
            optimizer.step()  # update wts

        if epoch % ep_log_interval == 0:
            print("epoch = %4d   loss = %0.4f" % \
                  (epoch, epoch_loss))

            # save checkpoint
            dt = time.strftime("%Y_%m_%d-%H_%M_%S")
            log = ".\\Log\\" + str(dt) + str("-") + \
                 str(epoch) + "_checkpoint.pt"

            info_dict = {
                'epoch': epoch,
                'net_state': net.state_dict(),
                'optimizer_state': optimizer.state_dict()
            }
            torch.save(info_dict, log)

    print("Done ")

    # 4. evaluate model accuracy
    print("\nComputing model accuracy")
    net.eval()
    acc_train = accuracy(net, train_ds, 0.10)
    print("Accuracy (within 0.10) on train material_data = %0.4f" % \
          acc_train)

    acc_test = accuracy(net, test_ds, 0.10)
    print("Accuracy (within 0.10) on test material_data  = %0.4f" % \
          acc_test)

    # 6. save final model (state_dict approach)

    # use saved_model to make prediction(s)
    net.eval()
    pred = net(train_ds.x_data).detach().numpy()
    y_dat = train_ds.y_data.detach().numpy()
    plt.plot(data['time (s)'], pred[:, 0], label='Model')
    plt.plot(data['time (s)'], y_dat[:, 0], label='Data')
    plt.ylabel('Force (N)')
    plt.xlabel('Time (s)')
    plt.grid()
    plt.legend()
    plt.tight_layout()

    plt.figure()
    plt.plot(data['time (s)'], pred[:, 1], label='Model')
    plt.plot(data['time (s)'], y_dat[:, 1], label='Data')
    plt.ylabel('PD rate (N)')
    plt.xlabel('Time (s)')
    plt.grid()
    plt.legend()
    plt.tight_layout()

    plt.show()
    print(f"\nSaving trained model state: {fn}")
    torch.save(net.state_dict(), fn)

    # saved_model = Net(n_mid=n_mid, n_hidden_layers=n_hidden)
    # saved_model.load_state_dict(torch.load(fn))
    print("\nEnd cap")


if __name__ == "__main__":
    main()


