from two_column_text_read import two_column_text_read
from univariate_statistics import univariate_statistics
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from equations_of_state import fit_eos
from numpy import linspace
import matplotlib.pyplot as mp


def parse_file_name(filename="Pt.Fm-3m.GGA-PBEsol.volumes_energies.dat"):
    to_parse = filename.split(".")
    chemical_symbol = to_parse[0]
    crystal_symmetry_symbol = to_parse[1]
    approximation_acronym = to_parse[2]
    return chemical_symbol, crystal_symmetry_symbol, approximation_acronym


filename = "Pt.Fm-3m.GGA-PBEsol.volumes_energies.dat"
chemical_symbol, crystal_symmetry_symbol, approximation_acronym = parse_file_name(filename)  # 1
print(chemical_symbol)
print(crystal_symmetry_symbol)
print(approximation_acronym)
print()


data = two_column_text_read("Pt.Fm-3m.GGA-PBEsol.volumes_energies.dat")  # 2
print("DATA")
print(data / 1)  # 3
print()


statistics = univariate_statistics(data)  # 4
print("STATISTICS")
print(statistics)
print()


quadratic_coefficients = quadratic_fit(data)  # 5
print("QUADRATIC_COEFFICIENTS")
print(quadratic_coefficients)
print()

un_data = zip(*data)
data_2 = list(un_data)

eos_fit_curve = fit_eos(data_2[0], data_2[1], quadratic_coefficients, eos='murnaghan', number_of_points=50)  # 6
print("EOS_FIT_CURVE")
print(eos_fit_curve)
print()

un_data = zip(*data)
data_2 = list(un_data)

bulk_modulus = 230  # Found on internet as I was unsure how to calculate bulk modulus, already in gigapascals


def convert_units(value_to_be_converted, units_of_the_value_to_be_converted_from, units_to_be_converted_to):  # 7
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
    from matplotlib.font_manager import FontProperties
    fig = mp.figure()
    ax = fig.add_subplot(111)
    ax.annotate('hello', xy=(2, 1), xycoords=(0.5, -0.046),)
    ax.set_ylim(-0.054, -0.036)
    return ax


fig = mp.figure()
ax = fig.add_subplot(111)

volumes = linspace(min(data_2[0]), max(data_2[0]), len(eos_fit_curve))
print(volumes)
line1, = ax.plot(data_2[0], data_2[1], 'o')
line2, = ax.plot(volumes, eos_fit_curve, color="black")
x_min = (min(data_2[0]) - (min(data_2[0]) * 0.10))
x_max = (max(data_2[0]) + (max(data_2[0]) * 0.10))
mp.xlim(x_min, x_max)
mp.xlabel(r'$ \mathcal{eV/atom}\ $')
mp.ylabel(r'$ \mathit{Å^3/atom}\ $')

font = ##############
ax.annotate(chemical_symbol, xy=(83, -1032.838))
ax.annotate(crystal_symmetry_symbol, xy=(100.5, -1032.85), fontproperties='italic')

mp.show()  # 8


