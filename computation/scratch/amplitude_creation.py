import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 1000)

half_periods = 5
off = 0.3
y = (1 + np.sin(np.pi * half_periods * x - np.pi/2))*(off + x*(1-off))/2

plt.plot(x, y)
amp = np.array([x, y]).T
np.savetxt('amp.csv', y, delimiter=',')
np.savetxt('time.csv', x, delimiter=',')
print()
plt.show()
