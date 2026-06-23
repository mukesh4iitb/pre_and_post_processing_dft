import re
from pymatgen.io.vasp.outputs import Oszicar

def E0_oszicar_old(OSZICAR_file):
    OS=open(OSZICAR_file, 'r')
    lines_os = OS.readlines()
    pattern = re.compile("F=")
    for line in lines_os:
        for match in re.finditer(pattern, line):
            last_matched_line = line
    return float(last_matched_line.split()[4])
#print(E0_oszicar_old("OSZICAR"))

def E0_oszicar(OSZICAR_file):
  """
  documentation: https://github.com/materialsproject/pymatgen-core/blob/7ae50681825df11d5719644b5078f436192a6b35/src/pymatgen/io/vasp/outputs.py
  It can provide more details like electronic_steps as well.
  """
    oszicar = Oszicar(OSZICAR_file)
    return oszicar.ionic_steps[-1]["E0"]
#print(E0_oszicar("OSZICAR"))
