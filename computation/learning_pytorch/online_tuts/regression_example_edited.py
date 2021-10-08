import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch.utils.data as Data
import matplotlib.pyplot as plt

import pandas as pd

import numpy as np
import imageio

torch.manual_seed(1)  # reproducible

data = pd.read_csv('../data/cap/processed_test_data.csv')

N_FEATURES = 3
N_OUTPUTS = 2
N_HIDDEN = 10

net_params = {'n_feature': N_FEATURES,
              'n_hidden': N_HIDDEN,
              'n_output': N_OUTPUTS
              }

x_data = data[['x_t (mm)', 'plastic dissipation (mJ)', 'v_t (mm/s)']]
y_data = data[['force (N)', 'plastic dissipation rate (mJ/s)']]

x, y = Variable(torch.Tensor(x_data.to_numpy())), Variable(torch.Tensor(y_data.to_numpy()))


# x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x material_data (tensor), shape=(100, 1)
# y = x.pow(2) + 0.2 * torch.rand(x.size())  # noisy y material_data (tensor), shape=(100, 1)
#
# # torch can only train on Variable, so convert them to Variable
# x, y = Variable(x), Variable(y)

# view material_data
# plt.figure(figsize=(10, 4))
# plt.scatter(x.material_data.numpy(), y.material_data.numpy(), color="orange")
# plt.title('Regression Analysis')
# plt.xlabel('Independent varible')
# plt.ylabel('Dependent varible')
# plt.show()


# this is one way to define a network
class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)  # hidden layer
        self.predict = torch.nn.Linear(n_hidden, n_output)  # output layer

    def forward(self, x):
        x = F.relu(self.hidden(x))  # activation function for hidden layer
        x = self.predict(x)  # linear output
        return x


# net = Net(n_feature=1, n_hidden=10, n_output=1)  # define the network
net = Net(**net_params)  # define the network
# print(net)  # net architecture
optimizer = torch.optim.SGD(net.parameters(), lr=1)
loss_func = torch.nn.MSELoss()  # this is for regression mean squared loss

my_images = []
fig, ax = plt.subplots(figsize=(12, 7))

# train the network
for t in range(200):
    print(f"Epoch {t + 1}\n-------------------------------")
    prediction = net(x)  # input x and predict based on x

    loss = loss_func(prediction, y)  # must be (1. nn output, 2. target)

    optimizer.zero_grad()  # clear gradients for next train
    loss.backward()  # backpropagation, compute gradients
    optimizer.step()  # apply gradients

    # plot and show learning process
    # plt.cla()
    # ax.set_title('Regression Analysis', fontsize=35)
    # ax.set_xlabel('Independent variable', fontsize=24)
    # ax.set_ylabel('Dependent variable', fontsize=24)
    # ax.set_xlim(-1.05, 1.5)
    # ax.set_ylim(-0.25, 1.25)
    # ax.scatter(x.material_data.numpy(), y.material_data.numpy(), color="orange")
    # ax.plot(x.material_data.numpy(), prediction.material_data.numpy(), 'g-', lw=3)
    # ax.text(1.0, 0.1, 'Step = %d' % t, fontdict={'size': 24, 'color': 'red'})
    # ax.text(1.0, 0, 'Loss = %.4f' % loss.material_data.numpy(),
    #         fontdict={'size': 24, 'color': 'red'})
    #
    # # Used to return the plot as an image array
    # # (https://ndres.me/post/matplotlib-animated-gifs-easily/)
    # fig.canvas.draw()  # draw the canvas, cache the renderer
    # image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    # image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    #
    # my_images.append(image)
print("Done!")

torch.save(net.state_dict(), "cap_predictor.pth")

model = Net(**net_params)
model.load_state_dict(torch.load("cap_predictor.pth"))

model.eval()
with torch.no_grad():
    pred = model(x[0, :])
    a=0
# save images as a gif
# imageio.mimsave('./curve_1.gif', my_images, fps=10)
