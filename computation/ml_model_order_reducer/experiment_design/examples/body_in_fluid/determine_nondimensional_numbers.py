from computation.ml_model_order_reducer.experiment_design.dimensional_analysis import *

# Experimental variables
K = ExperimentalVariable('K', Units.FORCE, Variable.PREDICTED, 'Drag force on object')
L = ExperimentalVariable('L', Units.LENGTH, Variable.PREDICTOR, 'Typical length of object')
V = ExperimentalVariable('V', Units.VELOCITY, Variable.PREDICTED, 'Velocity of fluid')
rho = ExperimentalVariable(r'\rho', Units.DENSITY, Variable.PREDICTOR, 'Density of fluid')
g = ExperimentalVariable(r'g', Units.ACCELERATION, Variable.PREDICTOR, 'Gravitational acceleration')
nu = ExperimentalVariable(r'\nu', Units.VISCOSITY, Variable.PREDICTOR, 'Viscosity of fluid')
c = ExperimentalVariable(r'c', Units.VELOCITY, Variable.PREDICTOR, 'Acoustic velocity')
sigma = ExperimentalVariable(r'\sigma', Units.SURFACE_TENSION, Variable.PREDICTOR, 'Surface tension')

# experiment = ExperimentalSetup((K, L, V, rho, nu, g, sigma))
# experiment = ExperimentalSetup((K, nu, c, g, sigma, L, V, rho))
experiment = ExperimentalSetup((V, K, c, g, sigma, L, rho, nu))
experiment.write_experiment_variables_table()
experiment.write_dimensionless_products_table()

a = 0
