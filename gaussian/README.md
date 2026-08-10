# gaussian

Bash functions for pre- and post-processing Gaussian 16 (g16) calculations:
generating `.gjf`/`.com` input files from `.xyz` coordinates for a range of
functionals/basis sets (with or without an implicit solvent), extracting
optimized coordinates from a finished job's `.out` file, and checking job
status. Source to use it.

```bash
source gaussian_dft_pre_and_post.sh
```

## Functions

All the `xyz2*` functions read an `.xyz` file
and write a Gaussian input (`.gjf`/`.com`) file with `%nprocshared`,
`%mem`, and `%chk` .

| Function | Description |
|---|---|
| `xyz2gjf <in.xyz> <out.gjf>` | Convert an `.xyz` file to a `.gjf` input, fixed at `B3LYP/6-31+G(d) OPT FREQ`. |
| `xyz2_inp <in.xyz> <out.com> <func> <basis> [name]` | Generic version: takes functional and basis set as arguments. |
| `xyz2_gen_inp <in.xyz> <out.com> <func> <basis_path> [name]` | Same, but for a user-supplied (`gen`) basis set file, referenced with `@<basis_path>`. |
| `xyz2_b3lyp_inp <in.xyz> <out.com> [name]` | B3LYP functional, `6-311+G**` basis set. |
| `xyz2_hse_inp <in.xyz> <out.com> [name]` | HSE (`HSEh1PBE`) functional, `6-311+G**` basis set. |
| `xyz2_pbe_inp <in.xyz> <out.com> [name]` | PBE (`PBEPBE`) functional, `6-311+G**` basis set. |
| `xyz2_lda_inp <in.xyz> <out.com> [name]` | LDA (`LSDA`) functional, `6-311G**` basis set. |
| `xyz2_sol_inp <in.xyz> <out.com> <func> <basis> <sol_val> [name]` | Generic solvated version (adds `SCRF(SMD, Read)` + `Eps=<sol_val>`); requires a dielectric constant. |
| `xyz2_gen_sol_inp <in.xyz> <out.com> <func> <basis_path> <sol_val> [name]` | Solvated version with a user-supplied (`gen`) basis set. |
| `xyz2_b3lyp_sol_inp <in.xyz> <out.com> <sol_val> [name]` | Solvated B3LYP, `6-311+G**`. |
| `xyz2_hse_sol_inp <in.xyz> <out.com> <sol_val> [name]` | Solvated HSE, `6-311+G**`. |
| `xyz2_pbe_sol_inp <in.xyz> <out.com> <sol_val> [name]` | Solvated PBE, `6-311+G**`. |
| `xyz2_lda_sol_inp <in.xyz> <out.com> <sol_val> [name]` | Solvated LDA, `6-311+G**`. |
| `get_opt_coords <in.out> <opt_coords.txt>` | Extract the last "Standard orientation" block from a finished g16 `.out` file and write it as `<element> <x> <y> <z>` rows. |
| `opt_coords2xyz <opt_coords.txt> <out.xyz>` | Convert the atomic-number-indexed coordinates from `get_opt_coords` into a proper `.xyz` file (element symbols looked up from a built-in periodic table, H–Og). |
| `get_status <in.out>` | Check whether a g16 job finished normally; if so, print the final SCF energy (`E0`) and vibrational frequencies. |

## Example workflow

Generate a new input file from an optimized structure (`structure.out`),
using the PBE functional:

**6-311G\*\* basis set:**

```bash
get_opt_coords structure.out opt_coords.txt
opt_coords2xyz opt_coords.txt structure_sol.xyz
xyz2_pbe_inp structure_sol.xyz structure_sol.com
```

**Custom (`gen`) basis set, e.g. def2-QZVPD, with an implicit solvent (ε = 3.1):**

```bash
get_opt_coords structure.out opt_coords.txt
opt_coords2xyz opt_coords.txt structure_sol.xyz
xyz2_gen_sol_inp structure_sol.xyz structure_sol.com PBEPBE /path/to/def2-QZVPD.bas 3.1
```








<!-- # Useful for pre and post for g16:

It generat the input files from xyz file to any kinds of file. It specially useful if you can to run multiple calculations. Other application of it as follows:



i)  xyz2gjf()  : this function, convert xyz file to gjf (input of gaussian and same as .com file).

ii) xyz2_b3lyp_inp() : this function, takes xyz input and gjf/com file with b3lyp functional and basis set 6-331G**
iii) xyz2_hse_inp(): this function, takes xyz input and gjf/com file with hse functional and basis set 6-331G**
iv) xyz2_pbe_inp(): this function, takes xyz input and gjf/com file with pbe functional and basis set 6-331G**

v) xyz2_lda_inp(): this function, takes xyz input and gjf/com file with lda functional and basis set 6-331G**
vi) xyz2_hse_sol_inp(): this function, takes xyz input and gjf/com file with hse functional and basis set 6-331G** and add solvention effect. So, it required dielectric constants as well.
vii) xyz2_pbe_sol_inp(): this function, takes xyz input and gjf/com file with pbe functional and basis set 6-331G** and add solvention effect. So, it required dielectric constants as well. 
viii) get_opt_coords(): This function, get the optimized co-ordinates from .out file. and write them as opt_coords.txt. Usually, this will be used with opt_coords2xyz() function.
ix) opt_coords2xyz(): this convert opt_coords.txt to xyz file. Usually, this will be used with get_opt_coords() function. 
x) get_status(): this check the status (whether completed or not completed) of gaussian jobs.


Example: Suppose, you have optimized a structure whose, output is structure.out and you want to generate input(com/gjf) file from the optimized co-ordinate and pbe functional with 6-331G** basis set or gen based basis set (def2-QZVPD).

For 6-331G** basis set:
get_opt_coords structure.out opt_coords.txt
opt_coords2xyz opt_coords.txt structure_sol.xyz
xyz2_b3lyp_inp structure_sol.xyz structure_sol.com

For gen based basis set: (only last line will change from the former one).
get_opt_coords structure.out opt_coords.txt
opt_coords2xyz opt_coords.txt structure_sol.xyz
xyz2_gen_sol_inp structure_sol.xyz structure_sol.com 3.1 -->
