#!/bin/bash --login
#SBATCH --ntasks=32
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=25G
#SBATCH --time=3-00:00:00
#SBATCH --job-name VASP_gaas
#SBATCH -A cmich   # this line ensure that we are using buy-in node.
#SBATCH --output=%x.o%j



#module purge
#module load intel-compilers/2022.2.1
#module load imkl-FFTW/2022.2.1
#srun  -n 16 /path/to/VASP/vasp.6.3.2-sol/vasp_std > vasp.out

module purge
/path/to/lobster-5.1.1 > lobster.out
