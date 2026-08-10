# vasp

Scripts for pre- and post-processing [VASP](https://www.vasp.at/) DFT
calculations. See [`pymatgen_related/`](pymatgen_related) for newer,
`pymatgen`-based versions of the band/DOS plotting workflows.

## Contents

| File | Purpose |
|---|---|
| `arxiving_vasp_outputs.py` | Mirror every subdirectory into a matching `<dir>.arxiv` tree, copy input files (`POSCAR`, `KPOINTS`, `INCAR`, `POTCAR`), job scripts (`job*.sh`) and output files (`CONTCAR`, `OSZICAR`, `OUTCAR`, `XDATCAR`, `vasprun.xml`) into it, then gzip the outputs in place. |
| `band_plot.py` | Plot a band structure from a band-data file (e.g. extracted from `EIGENVAL` via `polar_band-KPOINTS`), with vertical lines at high-symmetry k-points; writes `klable.txt`. |
| `catPOSCAR.py` | Concatenate two `POSCAR` files with matching lattice vectors into one `cat_POSCAR.vasp`, renaming the second structure's species `X0, X1, ...` to keep them distinct. |
| `convert.py` | Swap two lattice axes (`ab`, `bc`, or `ca`) of a POSCAR-format file (hard-coded to read `TiO2.vasp`, write `TiO2_out.vasp`). |
| `disatom.py` | Compute the distance between two atoms (by 1-based index) in a POSCAR file, handling both Direct and Cartesian coordinates. `python3 disatom.py POSCAR i j` |
| `dos.py` | Parse a `DOSCAR` file and dump per-`DOS<n>` text files for the total DOS, a single atom's DOS, or all atoms + total, based on interactive input. |
| `energy.py` | `pymatgen`-based helpers: extract the final `E0` energy from an `OSZICAR` (plus a legacy regex-only version), read a magnetic atom's (Fe/Co/Ni/Mn) total magnetic moment from `OUTCAR`+`POSCAR`, and parse a custom `sys: <name>` / `key: value` text log (binding energies, magnetic moments per system) into a `pandas.DataFrame`. |
| `INCAR_preprocessing.py` | Clean and normalize `INCAR` files (strip comments, normalize booleans/numbers) and combine two `INCAR` files into one, reporting keys unique to each side and flagging conflicting values. |
| `md_plots.py` | Interactively plot AIMD quantities (T, E, F, E0, EK, SP, SK) vs. MD step from an `OSZICAR` file. Adapted from [K4ys4r/VASP_Scripts](https://github.com/K4ys4r/VASP_Scripts). |
| `merged_md_oszicar.py` | Prefix each `T=` line of a concatenated multi-run `OSZICAR` file with a running step counter, writing `<file>_new`. |
| `Plotbands.py` | Plot a band structure from `vasprun.xml` using `pymatgen`'s `BSPlotter` (note: file has an import-syntax issue — `from matplotlib.pyplot as plt` should be `import matplotlib.pyplot as plt`). |
| `Plotdos.py` | CLI DOS plotter built on `pymatgen`'s `DosPlotter`/`Vasprun`. Subcommands: `total`, `atomic`, `orbital`, `orbital_d`. Run `python3 Plotdos.py -h`. Originally by Dr. Uthpala Herath ([MatSciScripts](https://github.com/uthpalaherath/MatSciScripts)), modified for newer `pymatgen`. |
| `utility code-1.py` | Coordinate-geometry helpers (interactive `input()`-driven): spherical↔Cartesian and polar↔Cartesian conversions, rotation/translation of vectors, angle between vectors/points, midpoint, point-at-distance-along-line. |
| `utility code-2.py` | File-based variants of some of the same geometry helpers (`gradient`, `pt_from_one_pt`, `middle_pt`, `rotation`, `translation`, `mirror_images`) that read two coordinate lines out of a file by line number instead of prompting for raw vectors. |
| `pymatgen_related/` | `pymatgen`-based notebooks/scripts for band structure, DOS, and LOBSTER post-processing, plus example VASP data (`Si-band/`, `Si-dos/`, `lobster/`, `Si.cif`). |


