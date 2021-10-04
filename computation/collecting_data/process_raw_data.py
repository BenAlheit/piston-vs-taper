import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

def delta(array):
    return array[1:] - array[:-1]


def mids(array):
    return (array[1:] + array[:-1])/2


raw_data = pd.read_csv('../learning_pytorch/raw_test_data.csv')
ts = raw_data['time (s)'].to_numpy()
delta_ts = delta(raw_data['time (s)'].to_numpy())
ts_at_delta_ts = mids(ts)
v_ts = delta(raw_data['x_t (mm)'].to_numpy())/delta_ts
pds_dots = delta(raw_data['plastic dissipation (mJ)'].to_numpy())/delta_ts
v_ts_at_ts = np.interp(ts, ts_at_delta_ts, v_ts)
pds_dots_at_ts = np.interp(ts, ts_at_delta_ts, pds_dots)
processed_data = raw_data.copy()
processed_data['v_t (mm/s)'] = v_ts_at_ts
processed_data['plastic dissipation rate (mJ/s)'] = pds_dots_at_ts
processed_data['contact'] = (np.abs(processed_data['force (N)']) > 1e-10).astype(int)

processed_data.set_index('time (s)', inplace=True)

processed_data.to_csv('../learning_pytorch/processed_test_data.csv')
seaborn.pairplot(processed_data, hue='contact')
plt.tight_layout()
plt.show()




for column in processed_data.columns:
    plt.figure()
    processed_data[column].plot()
    plt.grid()
    plt.ylabel(column)
    plt.xlabel('Time (s)')
    plt.tight_layout()
plt.show()
a=0
