import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt

# Stress [MPa], strain [mm/mm]
data = np.genfromtxt('../../data/hdpe-true-stress-strain-room-temp-6e-2-rate.csv', delimiter=',')
strain_data = data[:, 0]
stress_data = data[:, 1]


def get_ramberg_osgood_1d(eps, E, alpha, n, sig_0):
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


def get_ramberg_osgood_1d_stress_array(strain, E, alpha, n, sig_0):
    return np.array([get_ramberg_osgood_1d(eps, E, alpha, n, sig_0) for eps in strain])


def obj(params):
    import numpy as np
    import scipy.optimize as op

    # data = np.genfromtxt('../../data/hdpe-true-stress-strain-room-temp-6e-2-rate.csv', delimiter=',')
    data = np.genfromtxt(r'C:\Users\alhei\Dropbox\projects\piston-vs-taper\data\hdpe-true-stress-strain-room-temp-6e-2-rate.csv', delimiter=',')
    strain_data = data[:, 0]
    stress_data = data[:, 1]

    def get_ramberg_osgood_1d(eps, E, alpha, n, sig_0):
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

    def get_ramberg_osgood_1d_stress_array(strain, E, alpha, n, sig_0):
        return np.array([get_ramberg_osgood_1d(eps, E, alpha, n, sig_0) for eps in strain])

    stress_model = get_ramberg_osgood_1d_stress_array(strain_data, *params)
    normalized_error = (stress_data - stress_model) / stress_data
    return np.linalg.norm(normalized_error)

# params = [1000, 0.1, 5, 10]
#
# stress = get_ramberg_osgood_1d(0.1, *params)
# a=0
op_result = op.differential_evolution(obj,
                                      bounds=((100, 10000),
                                              (0, 0.5),
                                              (1, 10),
                                              (0.1, 15)),
                                      # args=(stress_data, strain_data),
                                      workers=-1,
                                      updating='deferred',
                                      disp=True)

op_params = op_result.x
print(op_params)
strain_model = np.linspace(0, strain_data[-1], 100)
stress_model = get_ramberg_osgood_1d_stress_array(strain_model, *op_params)
plt.plot(strain_model, stress_model, linewidth=1, label='Fitted Ramberg-Osgood model')
plt.plot(strain_data, stress_data, linewidth=0, marker='x', label='Room temperature,\nStrain rate = 6e-2/s ')
plt.grid()
plt.xlabel('True strain [mm/mm]')
plt.ylabel('True stress [MPa]')
plt.legend()
plt.show()
