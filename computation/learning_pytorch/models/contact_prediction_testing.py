import torch
from torch import nn

device = "cuda" if torch.cuda.is_available() else "cpu"


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

        self.hidden = nn.ModuleList([torch.nn.Linear(mid_dim, mid_dim) for i in range(n_hidden_layers)])
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

model = NeuralNetwork(3,
                      3,
                      3,
                      0,
                      0,
                      n_hidden_layers=2)

state_dict = torch.load("/home/cerecam/Benjamin_Alheit/projects/piston-vs-taper/computation/learning_pytorch/models/contact/contact_mid_dim_3_n_hidden_2.pth")

model.load_state_dict(state_dict)
model.state_dict()
print(state_dict)
print(model.accuracy)
