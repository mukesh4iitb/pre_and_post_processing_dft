# Useful for pre and post for g16:

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
xyz2_gen_sol_inp structure_sol.xyz structure_sol.com 3.1
