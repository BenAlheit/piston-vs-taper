from computation.ml_model_order_reducer.experiment_design.dimensional_analysis import *

# Cap variables
Fc = ExperimentalVariable('F_c', Units.FORCE, Variable.PREDICTED, 'Axial contact force')
pd_rate = ExperimentalVariable('\dot{\Phi}_{c}', Units.ENERGY_DENSITY_RATE, Variable.PREDICTED, 'Rate of volume average plastic dissipation')
pd = ExperimentalVariable('\Phi_{c}', Units.ENERGY_DENSITY, Variable.PREDICTOR, 'Rate of volume average plastic dissipation')
delta_p = ExperimentalVariable('\Delta P', Units.STRESS, Variable.PREDICTOR, 'Pressure difference')
v = ExperimentalVariable('v', Units.VELOCITY, Variable.PREDICTOR, 'Velocity')
x_t = ExperimentalVariable('x_t', Units.LENGTH, Variable.PREDICTOR, 'Distance of cap past taper')
l_c = ExperimentalVariable('l_c', Units.LENGTH, Variable.PREDICTOR, 'Length of cap past piston')
d_c = ExperimentalVariable('d_c', Units.LENGTH, Variable.PREDICTOR, 'Diameter of cap')
rho_c = ExperimentalVariable(r'\rho_c', Units.DENSITY, Variable.PREDICTOR, 'Density of cap')
E_c = ExperimentalVariable(r'E_c', Units.STRESS, Variable.PREDICTOR, 'Young\'s modulus of cap')
nu_c = ExperimentalVariable(r'\nu_c', Units.DIMENSIONLESS, Variable.PREDICTOR, 'Poisson\'s ratio of cap')
sig_yc = ExperimentalVariable(r'\sigma_{yc}', Units.STRESS, Variable.PREDICTOR, 'Yield stress of cap')

# Piston variables
l_p = ExperimentalVariable('l_p', Units.LENGTH, Variable.PREDICTOR, 'Length of piston')
d_p = ExperimentalVariable('d_p', Units.LENGTH, Variable.PREDICTOR, 'Diameter of piston')
rho_p = ExperimentalVariable(r'\rho_p', Units.DENSITY, Variable.PREDICTOR, 'Density of piston')
E_p = ExperimentalVariable(r'E_p', Units.STRESS, Variable.PREDICTOR, 'Young\'s modulus of piston')
nu_p = ExperimentalVariable(r'\nu_p', Units.DIMENSIONLESS, Variable.PREDICTOR, 'Poisson\'s ratio of piston')

# Transition piece variables
l_t = ExperimentalVariable('l_p', Units.LENGTH, Variable.PREDICTOR, 'Length of transition piece')
delta_d_t = ExperimentalVariable('d_p', Units.LENGTH, Variable.PREDICTOR, 'Diameter change of transition piece')
rho_t = ExperimentalVariable(r'\rho_p', Units.DENSITY, Variable.PREDICTOR, 'Density of transition piece')
E_t = ExperimentalVariable(r'E_p', Units.STRESS, Variable.PREDICTOR, 'Young\'s modulus of transition piece')
nu_t = ExperimentalVariable(r'\nu_p', Units.DIMENSIONLESS, Variable.PREDICTOR, 'Poisson\'s ratio of transition piece')

# Misc variables
mu_cs = ExperimentalVariable(r'\mu_{cs}', Units.DIMENSIONLESS, Variable.PREDICTOR, 'Cap-on-steel CoF')
mu_ss = ExperimentalVariable(r'\mu_{ss}', Units.DIMENSIONLESS, Variable.PREDICTOR, 'Steel-on-steel CoF')
mu_as = ExperimentalVariable(r'\mu_{as}', Units.DIMENSIONLESS, Variable.PREDICTOR, 'Aluminium-on-steel CoF')

# cap_vs_taper_experiment = ExperimentalSetup((Fc, pd_rate, pd, delta_p, v, x_t, l_c, d_c, rho_c, E_c, nu_c, sig_yc,
#                                              l_p, d_p, rho_p, E_p, nu_p,
#                                              l_t, delta_d_t, rho_t, E_t, nu_t,
#                                              mu_cs, mu_ss, mu_as))

# cap_vs_taper_experiment = ExperimentalSetup((Fc, pd_rate, pd, delta_p, v, x_t, l_c, d_c, rho_c, E_c, sig_yc,
#                                              l_p, d_p, rho_p, E_p,
#                                              l_t, delta_d_t, rho_t, E_t))

cap_vs_taper_experiment = ExperimentalSetup((Fc, pd_rate, l_c, d_c, rho_c, E_c, sig_yc,
                                             l_p, d_p, rho_p, E_p,
                                             l_t, delta_d_t, rho_t, E_t, delta_p, v, x_t, pd,
                                             mu_cs, mu_ss, mu_as))

cap_vs_taper_experiment.write_experiment_variables_table()
cap_vs_taper_experiment.write_dimensionless_products_table()


a = 0



