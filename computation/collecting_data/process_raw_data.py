import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import computation.plotting_config
from textwrap import wrap

SAVE_FIGS = True
PAIR_PLOTS = True
TIME_PLOT = True


def plot_sns_pairplot(data, columns=None, hue=None, size=None, save_path=None, title=''):
    if columns is None:
        columns = data.columns

    g = sns.PairGrid(data, hue=hue, vars=columns, palette="viridis")
    g.map_diag(sns.histplot, color=".3")
    if size is not None:
        g.map_offdiag(sns.scatterplot, size=data[size])
    else:
        g.map_offdiag(sns.scatterplot)

    g.add_legend(title=title, adjust_subtitles=True)
    g.tight_layout()
    if save_path is not None and SAVE_FIGS:
        plt.savefig(save_path)


def delta(array):
    return array[1:] - array[:-1]


def mids(array):
    return (array[1:] + array[:-1]) / 2


raw_data = pd.read_csv('../learning_pytorch/data/cap/raw_test_data.csv')
ts = raw_data['time (s)'].to_numpy()
delta_ts = delta(raw_data['time (s)'].to_numpy())
ts_at_delta_ts = mids(ts)
v_ts = delta(raw_data['x_t (mm)'].to_numpy()) / delta_ts
pds_dots = delta(raw_data['plastic dissipation (mJ)'].to_numpy()) / delta_ts
v_ts_at_ts = np.interp(ts, ts_at_delta_ts, v_ts)
pds_dots_at_ts = np.interp(ts, ts_at_delta_ts, pds_dots)
processed_data = raw_data.copy()
processed_data['v_t (mm/s)'] = v_ts_at_ts
processed_data['plastic dissipation rate (mJ/s)'] = pds_dots_at_ts
processed_data['contact'] = (np.abs(processed_data['force (N)']) > 1e-10).astype(int)
processed_data['elastoplastic'] = (np.abs(processed_data['plastic dissipation rate (mJ/s)']) > np.abs(
    processed_data['plastic dissipation rate (mJ/s)']).max() * 0.03).astype(int)

processed_data.set_index('time (s)', inplace=True)
processed_data.to_csv('../learning_pytorch/processed_test_data.csv')

if PAIR_PLOTS:
    plot_sns_pairplot(processed_data[['x_t (mm)',
                                      'plastic dissipation (mJ)',
                                      'force (N)',
                                      'contact']],
                      hue='contact',
                      save_path='../../report/results-figures/contact.pdf',
                      title='Contact dependence')

    plot_sns_pairplot(processed_data[['x_t (mm)',
                                      'plastic dissipation (mJ)',
                                      'plastic dissipation rate (mJ/s)',
                                      'elastoplastic']],
                      hue='elastoplastic',
                      save_path='../../report/results-figures/elastoplastic.pdf',
                      title='Elastoplastic dominance')

    data_contact_elastic_logic = (processed_data['contact'] == 1) & (processed_data['elastoplastic'] == 0)
    data_contact_elastic = processed_data.loc[data_contact_elastic_logic]
    data_contact_elasticplastic_logic = (processed_data['contact'] == 1) & (processed_data['elastoplastic'] == 1)
    data_contact_elastoplastic = processed_data.loc[data_contact_elasticplastic_logic]

    plot_sns_pairplot(data_contact_elastic[['x_t (mm)',
                                            'plastic dissipation (mJ)',
                                            'v_t (mm/s)',
                                            'force (N)',
                                            'plastic dissipation rate (mJ/s)',
                                            ]],
                      hue='plastic dissipation (mJ)',
                      size='v_t (mm/s)',
                      save_path='../../report/results-figures/contact-elastic.pdf',
                      title='Elastic contact force relation')

    plot_sns_pairplot(data_contact_elastoplastic[['x_t (mm)',
                                                  'plastic dissipation (mJ)',
                                                  'v_t (mm/s)',
                                                  'force (N)',
                                                  'plastic dissipation rate (mJ/s)',
                                                  ]],
                      hue='plastic dissipation (mJ)',
                      size='v_t (mm/s)',
                      save_path='../../report/results-figures/contact-elastoplastic.pdf',
                      title='Elastoplastic contact force relation')

if TIME_PLOT:
    plt.figure(figsize=(8, 10))
    cnt = 2
    ax1 = plt.subplot(int(f'711'))
    ax = ax1
    for column in ['x_t (mm)',
                   'v_t (mm/s)',
                   'plastic dissipation (mJ)',
                   'contact',
                   'elastoplastic',
                   'force (N)',
                   'plastic dissipation rate (mJ/s)',
                   ]:
        plt.plot(processed_data.index, processed_data[column])
        plt.ylabel('\n'.join(wrap(column, 20)))
        if cnt < 8:
            plt.setp(ax.get_xticklabels(), visible=False)
            place = int(f'71{cnt}')
            ax = plt.subplot(place, sharex=ax1)
        cnt += 1
        
    plt.xlabel('Time (s)')
    plt.grid()
    plt.tight_layout()
    plt.savefig('../../report/results-figures/loading-vs-time.pdf')
plt.show()
