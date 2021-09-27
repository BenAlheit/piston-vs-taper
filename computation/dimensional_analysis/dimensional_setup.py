"""
M denotes units for mass
L denotes units for length
T denotes units for time

Dimensional matrix is of the form:
      Q_1   Q_2 ....... Q_n
     _______________________   ---
M   |.......................| |k_1|    _
L   |.......................| |k_2|   |0|
T   |.......................| | . | = |0|
     -----------------------  | . |   |0|
                              | . |    -
                              |k_n|
                               ---
"""
import sympy as sp
from enum import Enum, auto
import jinja2
from typing import Tuple


class Units(Enum):
    """
    M denotes units for mass
    L denotes units for length
    T denotes units for time

    Dimensional matrix is of the form:
          Q_1   Q_2 ....... Q_n
         _______________________   ---
    M   |.......................| |k_1|    _
    L   |.......................| |k_2|   |0|
    T   |.......................| | . | = |0|
         -----------------------  | . |   |0|
                                  | . |    -
                                  |k_n|
                                   ---
    """
    FORCE = sp.Matrix([1, 1, -2])
    ENERGY_DENSITY = sp.Matrix([1, -1, -2])
    ENERGY_DENSITY_RATE = sp.Matrix([1, -1, -3])
    STRESS = sp.Matrix([1, -1, -2])
    VELOCITY = sp.Matrix([0, 1, -1])
    LENGTH = sp.Matrix([0, 1, 0])
    DENSITY = sp.Matrix([1, -3, 0])
    DIMENSIONLESS = sp.Matrix([0, 0, 0])


class Variable(Enum):
    MEASURED = auto()
    CONTROLLED = auto()


class ExperimentalVariable:
    def __init__(self, symbol: str, units: Units, variable_type: Variable, description=''):
        self.symbol = sp.Symbol(symbol)
        self.units = units
        self.description = description
        self.variable_type = variable_type


class ExperimentalSetup:
    # TODO: Determine exponents for dimensionless numbers. Do this somewhat intelligently (prioritise measured variables
    #  followed by controlled variables in order of decreasing 'controllability'. See Hutter pg. 355)
    def __init__(self, variables: Tuple[ExperimentalVariable, ...]):
        self.variables = variables
        self.n_variables = len(variables)
        self.dimensional_matrix = sp.Matrix.zeros(rows=3, cols=self.n_variables)
        self.construct_dimensional_matrix()

    def construct_dimensional_matrix(self):
        for i_variable in range(self.n_variables):
            self.dimensional_matrix[:, i_variable] = self.variables[i_variable].units.value
