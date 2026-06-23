import re
import os
import ast
import pandas as pd
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

#data=parse_data_file("data.txt")


## It can process the follwoing kinds of data.txt
# sys: Fe2(1)
# with 5x5x1:
# Eb: -2.57054070000008 mag: ('Fe', -2.662)
# sys: Fe2(2)
# with 5x5x1:
# Eb: -1.5757607000000884 mag: ('Fe', 2.815)
# with 2x3x1
# Eb: -1.5686907000000896 mag: ('Fe', 2.812)
# sys: Fe3(1)
# with 5x5x1 not optimized fully
# Eb: -7.338240700000071 mag: ('Fe', 3.307)
# with 2x3x1
# Eb: -7.6287306999999345 mag: ('Fe', 3.306)
# sys: Fe3(2)
# with 5x5x1 not optimized fully
# Eb: -5.4272306999999245 mag: ('Fe', 3.216)



def dicts_to_dataframe(data):
    rows = []

    for item in data:
        row = {"sys": item["sys"]}

        values = item.get("values", {})

        for k, v in values.items():

            # handle Eb1, Eb2 ...
            if k.startswith("Eb"):
                row[k] = v

            # handle tuples or list
            elif k.startswith("mag") and isinstance(v, (tuple, list)):
                # row[f"{k}_atom"] = v[0]
                row[f"{k}_value"] = v[1]

            else:
                continue

        rows.append(row)

    return pd.DataFrame(rows)

# df = dicts_to_dataframe(data)
# print(df)

