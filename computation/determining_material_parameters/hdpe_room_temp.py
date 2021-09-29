from jinja2 import Template
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt
from typing import Iterable
from computation.abaqus_utils import run_abaqus_standard_job as rj, extraction as ex

HDPE_nu = 0.46
RUN_ABAQUS = False
N_ABAQUS = 20
# True stress [MPa], true strain [mm/mm]
data = np.genfromtxt('../../data/hdpe-true-stress-strain-room-temp-6e-2-rate.csv', delimiter=',')
strain_data = data[:, 0]
stress_data = data[:, 1]


def get_ramberg_osgood_1d(eps: float, E: float, alpha: float, n: float, sig_0: float):
    """
    Stress strain relation for the Ramberg-Osgood model.
    For details see: http://130.149.89.49:2080/v2016/books/usb/default.htm?startat=pt05ch23s02abm29.html
    :param eps: The current strain
    :param E: Young's modulus
    :param alpha: yield offset material parameter
    :param n: hardening exponent (>1)
    :param sig_0: yield stress
    :return: The stress for the current strain.
    """
    strain_relation = lambda sig: (sig + alpha * (np.fabs(sig) / sig_0) ** (n - 1)) / E
    stress = op.root(lambda sig: strain_relation(sig) - eps, 10).x[0]
    return stress


def get_ramberg_osgood_1d_stress_array(strain: Iterable[float], E: float, alpha: float, n: float, sig_0: float):
    """
    Gets array of stresses for array of strains for RO model.
    :param strain: The current strain
    :param E: Young's modulus
    :param alpha: yield offset material parameter
    :param n: hardening exponent (>1)
    :param sig_0: yield stress
    :return: Array of stresses.
    """
    return np.array([get_ramberg_osgood_1d(eps, E, alpha, n, sig_0) for eps in strain])


def obj(params):
    """
    Objective function to minimize
    :param params: Parameters to optimize
    :return: Error value
    """
    stress_model = get_ramberg_osgood_1d_stress_array(strain_data, *params)
    relative_error = (stress_data - stress_model) / stress_data
    return np.linalg.norm(relative_error) ** 2


op_result = op.differential_evolution(obj,
                                      bounds=((100, 10000),
                                              (0, 0.5),
                                              (1, 10),
                                              (0.1, 15)),
                                      popsize=40,
                                      tol=0.000000001,
                                      atol=0.00000001,
                                      workers=1,
                                      # workers=n_cpus. -1 indicates all available cpus. Parallelization only workds on linux. For windows set workers=1 to avoid error.
                                      polish=True,
                                      updating='deferred',
                                      disp=True)

## Good fit obtained: [1.62856286e+03 3.45909933e-01 5.26480184e+00 7.83313655e+00]
## Good fit obtained: [1.62944658e+03 3.61176080e-01 5.26202581e+00 7.90527041e+00]
## Good fit obtained: [1.63012092e+03 4.23279057e-01 5.26001632e+00 8.19947508e+00]


op_params = op_result.x
print(op_params)
strain_model = np.linspace(0, strain_data[-1], 100)
stress_model = get_ramberg_osgood_1d_stress_array(strain_model, *op_params)
plt.plot(strain_model, stress_model, linewidth=2, label='Fitted Ramberg-Osgood model')

if RUN_ABAQUS:
    inp_template = Template(open('./hpde-behaviour.inp-tmp', 'r').read())
    E, alpha, n, sig_0 = op_params
    inp_file_str = inp_template.render(youngs_modulus=E,
                                       sig_0=sig_0,
                                       n=n,
                                       alpha=alpha,
                                       step_size=1./N_ABAQUS)
    # Path(directory).mkdir(parents=True, exist_ok=True)
    open(f'./hpde-behaviour.inp', 'w+').write(inp_file_str)
    rj.run_abaqus_standard_sim('./', 'hpde-behaviour')
    data = ex.extract_uniaxial('./', 'hpde-behaviour')
    plt.plot(data['strain (mm/mm)'], data['stress (MPa)'], linewidth=1, label='Abaqus simulation')

plt.plot(strain_data, stress_data, linewidth=0, marker='x', label='Room temperature,\nStrain rate = 6e-2/s ')
plt.xlabel('True strain [mm/mm]')
plt.ylabel('True stress [MPa]')
plt.grid()
plt.legend()
plt.show()
