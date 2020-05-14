"""########################################################Part_1###################################################"""
from two_column_text_read import two_column_text_read
from univariate_statistics import univariate_statistics
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from equations_of_state import fit_eos
from numpy import linspace
import matplotlib.pyplot as mp

display_graph = True


def parse_file_name(filename):
    to_parse = filename.split(".")
    chemical_symbol = to_parse[0]
    crystal_symmetry_symbol = to_parse[1]
    approximation_acronym = to_parse[2]
    return chemical_symbol, crystal_symmetry_symbol, approximation_acronym


filename = "Pt.Fm-3m.GGA-PBEsol.volumes_energies.dat"
chemical_symbol, crystal_symmetry_symbol, approximation_acronym = parse_file_name(filename)  # 1
data = two_column_text_read(filename)  # 2
statistics = univariate_statistics(data)  # 4
quadratic_coefficients = quadratic_fit(data)  # 5

un_data = zip(*data)
data_2 = list(un_data)

eos_fit_curve, bulk_modulus = fit_eos(data_2[0], data_2[1], quadratic_coefficients, eos='murnaghan',
                                      number_of_points=50)  # 6


def convert_units(value_to_be_converted, units_of_the_value_to_be_converted_from, units_to_be_converted_to=0):  # 7
    """
    :param value_to_be_converted: Somevalue
    :param units_of_the_value_to_be_converted_from: Accepted units: cb/a, rb/a, rb/cb
    :param units_to_be_converted_to: Accepted units: ca/a, ev/a, ggp
    :return: value_in_the_requested_units
    """
    if units_of_the_value_to_be_converted_from == "cb/a":
        value_in_the_requested_units = value_to_be_converted * 0.148185
    elif units_of_the_value_to_be_converted_from == "rb/a":
        value_in_the_requested_units = value_to_be_converted * 13.6057
    elif units_of_the_value_to_be_converted_from == "rb/cb":
        value_in_the_requested_units = value_to_be_converted / 29421.02648438959
    else:
        value_in_the_requested_units = value_to_be_converted
    return value_in_the_requested_units


def annotate_graph(chemical_symbol, crystal_symmetry_symbol):  # 9
    import matplotlib.pyplot as mp

    ax.annotate(chemical_symbol, xy=(min(data_2[0]) - (min(data_2[0]) * 0.07),
                                     max(data_2[1]) + max(data_2[0]) * 0.00007))

    ax.annotate(r'$ {}\overline{{{}}} {}$'.format(crystal_symmetry_symbol[0:2],
                                                  crystal_symmetry_symbol[3],
                                                  crystal_symmetry_symbol[1]),
                xy=(equilibrium_volume, (max(data_2[1]) + min(data_2[1])) / 2))

    ax.annotate('K_0={:.6f}GPa'.format(bulk_modulus_gigapascals),
                xy=(equilibrium_volume, (max(data_2[1]) + min(data_2[1])) / 2.00001))

    ax.annotate('V_0={:.3f}Å^3/atom'.format(equilibrium_volume),
                xy=(equilibrium_volume, (max(data_2[1]) + min(data_2[1])) / 1.99997))
    mp.axvline(equilibrium_volume - data_2[0][data_2[1].index(min(data_2[1]))] * 0.01, color="black", linestyle='--')

    mp.text(83.5226, -1032.86, "Created by Paul Rizzo 2020-05-12")
    mp.title("{} Equation of State for {} in DFT {}".format('murnaghan', chemical_symbol, approximation_acronym))
    return ax, mp  # 9


fig = mp.figure()
ax = fig.add_subplot(111)

volumes = linspace(min(data_2[0]), max(data_2[0]), len(eos_fit_curve))
line1, = ax.plot(data_2[0], data_2[1], 'o')  # 8
line2, = ax.plot(volumes, eos_fit_curve, color="black")

x_min = (min(data_2[0]) - (min(data_2[0]) * 0.10))
x_max = (max(data_2[0]) + (max(data_2[0]) * 0.10))
y_min = (min(data_2[1]) - (min(data_2[0]) * 0.00010))
y_max = (max(data_2[1]) + (max(data_2[0]) * 0.00010))

mp.xlim(x_min, x_max)
mp.ylim(y_min, y_max)
mp.xlabel(r'$ \mathit{Å^3/atom}\ $')
mp.ylabel(r'$ \mathcal{eV/atom}\ $')
bulk_modulus_gigapascals = convert_units(bulk_modulus, "rb/cb")
equilibrium_volume = data_2[0][data_2[1].index(min(data_2[1]))]
annotate_graph(chemical_symbol, crystal_symmetry_symbol)
if display_graph:  # 10
    mp.show(display_graph)
elif not display_graph:
    mp.savefig("Rizzo.Pt.Fm-3m.GGA-PBEsol.murnaghanEquationOfState.png")

"""########################################################Part_2###################################################"""

from generate_matrix import generate_matrix
from lowest_eigenvectors import lowest_eigenvectors
from numpy import linspace
import matplotlib.pyplot as mp

display_graph = True
potential_name = 'harmonic'
N_dim = 110
potential_parameter = 100

matrix = generate_matrix(-10, 10, N_dim, potential_name, potential_parameter)  # 1
eigenvalues, eigenvectors = lowest_eigenvectors(matrix, 2, 5)  # 2

x = linspace(-10, 10, N_dim)  # 3
line1, = mp.plot(x, eigenvectors[0][0:N_dim])  # 4
line2, = mp.plot(x, eigenvectors[1][0:N_dim])  # 4
line3, = mp.plot(x, eigenvectors[2][0:N_dim])  # 4

mp.xlabel("x [a.u.]")
mp.ylabel("ψ n ( x ) [a.u.]")
mp.legend((line1, line2, line3), ('ψ1, Ε1 = 0.62414396 a.u.', 'ψ2, Ε2 = 0.87335307 a.u.', 'ψ3, Ε3 = 1.12229893 a.u.'))
mp.axis([-10, 10, max(eigenvectors[0]) - 2, max(eigenvectors[0]) + 2])
mp.axhline(color="black")  # 5
mp.text(-9.5, -1.75, "Created by Paul Rizzo 2020-05-12")  # 6
mp.title("Select Wavefunctions for a Harmonic Potential on a Spatial Grid of 1, 2, 3 Points")  # 7

if display_graph:
    mp.show(display_graph)
elif not display_graph:
    mp.savefig("Rizzo.harmonic.Eigenvector1, 2, 3.png")
