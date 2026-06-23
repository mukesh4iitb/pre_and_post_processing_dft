import re
import os
import ast
from pymatgen.io.vasp.outputs import Poscar, Oszicar, Outcar

def E0_oszicar_old(oszicar_dir):
    OS=open(os.path.join(oszicar_dir, "OSZICAR"), 'r')
    lines_os = OS.readlines()
    pattern = re.compile("F=")
    for line in lines_os:
        for match in re.finditer(pattern, line):
            last_matched_line = line
    return float(last_matched_line.split()[4])
#print(E0_oszicar_old("."))

def E0_oszicar(oszicar_dir):
    oszicar = Oszicar(os.path.join(oszicar_dir, "OSZICAR"))
    return oszicar.ionic_steps[-1]["E0"]
#print(E0_oszicar("."))


def magmom_outcar(outcar_dir):
    outcar = Outcar(os.path.join(outcar_dir, "OUTCAR"))
    structure = Poscar.from_file(os.path.join(outcar_dir, "POSCAR")).structure
    
    mag_data = outcar.magnetization

    for i, site in enumerate(structure):
        if site.specie.symbol in ["Fe", "Co", "Ni", "Mn"]:
            return site.specie.symbol, mag_data[i]["tot"]


def parse_kv_line(line):
    """Parse only key: value pairs from a line."""
    pattern = r'(\w+):\s*(.*?)(?=\s+\w+:|$)'
    out = {}

    for k, v in re.findall(pattern, line):
        v = v.strip()
        try:
            v = ast.literal_eval(v)
        except:
            pass
        out[k] = v

    return out

def parse_data_file(filename):
    rows = []
    current = None

    with open(filename) as f:
        for line in f:
            line = line.strip()

            if not line:
                continue
                
            # ---- start new sys: ----
            if line.startswith("sys:"):
                if current:
                    rows.append(current)

                current = {
                    "sys": line.split(":", 1)[1].strip(),
                    "values": {}
                }
                continue

            # ---- key:value lines ----
            if ":" in line and current is not None:
                parsed = parse_kv_line(line)
                current["values"].update(parsed)

    # append last system
    if current:
        rows.append(current)

    return rows


