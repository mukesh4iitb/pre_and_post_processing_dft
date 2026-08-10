# pre_and_post_processing_dft

A collection of scripts for pre- and post-processing DFT
calculations — mainly [VASP](https://www.vasp.at/) and
[Gaussian](https://gaussian.com/) utilities using bash and python.

## Folders

| Folder | Contents |
|---|---|
| [`vasp/`](vasp/README.md) | Pre/post-processing for VASP: archiving job outputs, POSCAR manipulation, INCAR cleaning/merging, band structure/DOS/AIMD plotting (both hand-rolled and `pymatgen`-based), and general coordinate-geometry helpers. |
| [`gaussian/`](gaussian/README.md) | Bash functions for Gaussian 16 (g16): generating input files (`.gjf`/`.com`) from `.xyz` coordinates for various functionals/basis sets (with optional implicit solvent), extracting optimized geometries from output files, and checking job status. |

Each folder has its own `README.md` with a per-file breakdown and usage examples.


