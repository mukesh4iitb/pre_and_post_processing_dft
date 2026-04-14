# original taken from:
# https://matsci.org/t/how-to-plot-bandstructure-using-pymatgen-and-python/53711/2

from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter
from matplotlib.pyplot as plt

vasprun = Vasprun("./vasprun.xml")
bandstr = vasprun.get_band_structure(line_mode = True)
plt = BSPlotter(bandstr).get_plot(ylim=[-2, 2])
plt.figure.savefig("bandfmtest.pdf")

# chaging rc-parameters of plotlib object
plt.rcParams["legend.fontsize"] = 30
bsp = BSPlotter(bs).get_plot()

# ax = bsp.gca()
ax.lines[0].set_color("red")
