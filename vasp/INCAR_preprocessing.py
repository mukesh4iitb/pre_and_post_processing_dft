import re

def normalize_value(val):
    val = val.strip()
    # --- 1. Boolean normalization ---
    bool_map = {
        "true": "True",
        ".true.": "True",
        "true.": "True",
        ".true": "True",
        ".false.": "False",
        "false.": "False",
        ".false": "False",
        "false": "False",
    }

    key = val.lower()
    if key in bool_map:
        return bool_map[key]

    # --- 2. Numeric normalization ---
    try:
        num = float(val)
        if num.is_integer():
            return str(int(num))
        else:
            return str(num)
    except:
        pass
    return val

def normalize_line(line):
    if "=" in line:
        key, val = line.split("=", 1)
        val = normalize_value(val)
        return f"{key.strip()} = {val.strip()}"
    return line



def INCAR_dict(INCAR_file="INCAR"):
    """
    This function will just avoid the comment lines.
    And return useful lines from INCAR file.
    """
    incar_dict = {}

    with open(INCAR_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "=" not in line:
                continue

            key=line.split("=")[0].strip()
            val=line.split("=")[1].strip()
            incar_dict[key] = val
    return incar_dict

def clean_INCAR(INCAR_file="INCAR", INCAR_clean=None):
    """
    This function will just avoid the comment lines.
    And return useful lines from INCAR file.
    """
    selected_lines = []
    cleaned_lines = []

    with open(INCAR_file, "r") as f:
        for line in f:

            line = line.strip()

            if "=" not in line:
                continue
            if not line:
                continue
            if "#" in line:
                first_part = line.split()[0].strip()
                if first_part.startswith("#"):
                    continue
            selected_lines.append(line)

    for line in selected_lines:
        cleaned_lines.append(normalize_line(line))

    if INCAR_clean is None:
        INCAR_clean = INCAR_file

    with open(INCAR_clean, "w") as f:
        f.write("\n".join(cleaned_lines) + "\n")


def combine_INCAR(file1, file2, output="INCAR_combined"):
    clean_INCAR(file1)
    clean_INCAR(file2)

    d1 = INCAR_dict(file1)
    d2 = INCAR_dict(file2)

    combined = {}
    conflicts = {}

    # Process all keys
    all_keys = set(d1.keys()).union(d2.keys())

    for key in all_keys:
        v1_raw = d1.get(key)
        v2_raw = d2.get(key)

        if v1_raw is None:
            combined[key] = v2_raw
            continue
        if v2_raw is None:
            combined[key] = v1_raw
            continue

        # normalize before comparison
        v1 = normalize_value(v1_raw)
        v2 = normalize_value(v2_raw)

        if v1 == v2:
            combined[key] = v1  # same physical value → keep one
        else:
            conflicts[key] = (v1, v2)

    # Write output
    with open(output, "w") as f:
        f.write("# ===== Combined INCAR =====\n")
        for k, v in sorted(combined.items()):
            f.write(f"{k} = {v}\n")

        if conflicts:
            f.write("\n# ===== Conflicting Parameters =====\n")
            for k, (v1, v2) in conflicts.items():
                f.write(f"# {k} = {v1}\n")
                f.write(f"{k} = {v2}\n")
    print(f"writing {output} file!")
    return combined, conflicts

combine_INCAR("INCAR_dos_bader", "INCAR.lobsterpy-3")
