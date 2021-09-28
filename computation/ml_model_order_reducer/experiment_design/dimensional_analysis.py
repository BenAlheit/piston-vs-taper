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
from pylatex import Document, Tabular, Math, Table, NoEscape
from typing import Tuple


class InputParameterType(Enum):
    VARIABLE = auto()
    FIXED = auto()


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
    ORDER = ['M', 'L', 'T']
    FORCE = sp.Matrix([1, 1, -2])
    ENERGY_DENSITY = sp.Matrix([1, -1, -2])
    ENERGY_DENSITY_RATE = sp.Matrix([1, -1, -3])
    STRESS = sp.Matrix([1, -1, -2])
    SURFACE_TENSION = sp.Matrix([1, 0, -2])
    VISCOSITY = sp.Matrix([1, -1, -1])
    VELOCITY = sp.Matrix([0, 1, -1])
    ACCELERATION = sp.Matrix([0, 1, -2])
    LENGTH = sp.Matrix([0, 1, 0])
    DENSITY = sp.Matrix([1, -3, 0])
    DIMENSIONLESS = sp.Matrix([0, 0, 0])


class Variable(Enum):
    PREDICTED = auto()
    PREDICTOR = auto()


class ExperimentalVariable:
    def __init__(self, symbol: str, units: Units, variable_type: Variable, description=''):
        self.symbol = sp.Symbol(symbol)
        self.units = units
        self.description = description
        self.variable_type = variable_type
        self.unit_str = ''
        for i_unit in range(3):
            exp = self.units.value[i_unit]
            if exp != 0:
                if exp == 1:
                    self.unit_str += Units.ORDER.value[i_unit]
                else:
                    self.unit_str += Units.ORDER.value[i_unit] + '^{' + str(exp) + '}'


class InputParameter(ExperimentalVariable):
    def __init__(self, parameter_type: InputParameterType, symbol: str, units: Units,
                 description='', influences: [ExperimentalVariable] = [], dimensional_analysis: bool = False,
                 value_range: Tuple[float, float] = None,
                 value: float = None):
        super().__init__(symbol, units, Variable.PREDICTOR, description)
        self.parameter_type = parameter_type
        self.influences = influences
        self.dimensional_analysis = dimensional_analysis


class ExperimentalSetup:
    r = 3
    # TABLE_GEOMETRY_OPTIONS = {"margin": "1in", "linespread": "1.25"}
    TABLE_GEOMETRY_OPTIONS = {}

    # TODO: Determine exponents for dimensionless numbers. Do this somewhat intelligently (prioritise measured variables
    #  followed by controlled variables in order of decreasing 'controllability'. See Hutter pg. 355)
    def __init__(self, variables: Tuple[ExperimentalVariable, ...], input_parameters=None):
        self.variables = variables
        self.dimensionless_variables = tuple(var for var in variables if var.units == Units.DIMENSIONLESS)
        self.dimensional_variables = tuple(var for var in variables if not var.units == Units.DIMENSIONLESS)
        self.n_dim_variables = len(self.dimensional_variables)
        self.n_non_dim_variables = len(self.dimensionless_variables)
        self.dimensional_matrix = sp.Matrix.zeros(rows=3, cols=self.n_dim_variables)
        self.construct_dimensional_matrix()

        self.alpha_table = sp.Matrix.zeros(rows=self.n_dim_variables - self.r, cols=self.r)
        self.calculate_alphas()

    def write_experiment_variables_table(self):
        experiment_variables_table = Document(geometry_options=self.TABLE_GEOMETRY_OPTIONS)

        with experiment_variables_table.create(Table(position='!htb')) as table:
            table.append(NoEscape('\centering'))
            table.append(NoEscape('\caption{Experimental variables}'))
            table.append(NoEscape('\label{tab:experimental-variables}'))
            with experiment_variables_table.create(Tabular('p{7cm} c c')) as tabular:
                tabular.add_hline()
                tabular.add_row(('Description', 'Symbol', 'Units'))
                tabular.add_hline()
                tabular.add_hline()
                for variable in self.variables:
                    symbol = Math(data=[NoEscape(str(variable.symbol))], inline=True)
                    units = Math(data=[NoEscape(f'[{variable.unit_str}]')], inline=True)
                    tabular.add_row((variable.description, symbol, units))

        experiment_variables_table.generate_pdf('experiment-variables-table', clean_tex=False)

    def write_dimensionless_products_table(self):
        dim_numbers_table = Document(geometry_options=self.TABLE_GEOMETRY_OPTIONS)
        dim_numbers_table.preamble.append(NoEscape('\\usepackage{color}\n'))

        with dim_numbers_table.create(Table(position='!htb')) as table:
            table.append(NoEscape('\centering'))
            table.append(NoEscape('\caption{Unique set of dimensionless products}'))
            table.append(NoEscape('\label{tab:dimensionless-products}'))
            n_var_cols = self.n_dim_variables + self.n_non_dim_variables
            with dim_numbers_table.create(Tabular('c || ' + ' c' * n_var_cols)) as tabular:
                tabular.add_hline()
                tabular.add_row(
                    (' ',) + tuple(Math(data=[NoEscape(f'{var.symbol}')], inline=True) for var in self.variables))
                tabular.add_hline()
                tabular.add_hline()
                n_dim_rows = self.n_dim_variables - self.r
                plc_hldr = ''
                for i_alpha in range(n_dim_rows):
                    tabular.add_row((Math(data=[NoEscape('\Pi_{' + str(i_alpha + 1) + '}')], inline=True),) +
                                    i_alpha * (plc_hldr,) + (1,) + (n_dim_rows - i_alpha - 1) * (plc_hldr,) +
                                    tuple(self.alpha_table[i_alpha, j_table] for j_table in range(self.r)) +
                                    (plc_hldr,) * self.n_non_dim_variables)
                    tabular.add_hline()

                for i_alpha in range(self.n_non_dim_variables):
                    tabular.add_row(
                        (Math(data=[NoEscape('\Pi_{' + str(n_dim_rows + i_alpha + 1) + '}')], inline=True),) +
                        (self.n_dim_variables + i_alpha) * (plc_hldr,) + (1,) + (
                                n_var_cols - (self.n_dim_variables + i_alpha + 1)) * (plc_hldr,))
                    tabular.add_hline()

        dim_numbers_table.generate_pdf('dimensionless-products-table', clean_tex=False)

    def construct_dimensional_matrix(self):
        for i_variable in range(self.n_dim_variables):
            self.dimensional_matrix[:, i_variable] = self.dimensional_variables[i_variable].units.value

    def calculate_alphas(self):
        for i_alpha in range(self.n_dim_variables - self.r):
            F = -self.dimensional_matrix[:, i_alpha]
            K = self.dimensional_matrix[:, self.n_dim_variables - self.r:]
            alpha = K.inv() * F
            self.alpha_table[i_alpha, :] = alpha.T
