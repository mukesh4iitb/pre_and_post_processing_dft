#!/bin/bash --login
#SBATCH --ntasks=32
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=15G
#SBATCH --time=0-04:00:00
#SBATCH --job-name VASP
#SBATCH -A cmich  # this line ensure that we are using buy-in node.
#SBATCH --output=%x.o%j

##export I_MPI_HYDRA_BOOTSTRAP=ssh
#cat /etc/os-release
## working for ntasks=1, 28, 32, 40
#module purge
#module load intel/2022b
#module load foss/2022b
#module load HDF5/1.14.0-gompi-2022b
#module load imkl/2022.2.1
#
##mpirun /mnt/research/barone/VASP/vasp.6.4.0/bin/vasp_std
#mpirun  /mnt/research/barone/VASP/vasp.6.3.2-sol/vasp_std > vasp.out

module purge
module load intel-compilers/2022.2.1
module load imkl-FFTW/2022.2.1

# Save this info to a log file  
echo "$SLURM_JOB_ID | $SLURM_JOB_NAME | $(date)  | $SLURM_SUBMIT_DIR " >> /mnt/home/k0122399/vasp_check/vasp_job_history.txt


export SUBMIT_DIR=$SLURM_SUBMIT_DIR
export JOB=$SLURM_JOB_NAME
export DATE=$(date +%Y-%m-%d)
export RUNID=${JOB}_${SLURM_JOB_ID}_${DATE}
export SCRATCH_DIR=$SCRATCH/vasp_runs/$RUNID

echo "Date: $DATE"
echo "SUBMIT DIR: $SUBMIT_DIR"
echo "SLURM JOB ID: $SLURM_JOB_ID" 
echo "SCRATCH DIR: $SCRATCH_DIR"
echo ""

mkdir -p $SCRATCH_DIR
for inpfile in *;
do
   if [[ -f $inpfile ]]; then
      cp $SUBMIT_DIR/$inpfile $SCRATCH_DIR
   fi
done

# Catch external termination like scancel or wall time
trap 'cp -r $SCRATCH_DIR $SUBMIT_DIR/TERMINATED_${RUNID}; echo -e "\n Job with RUNID $RUNID terminated early. Scratch saved."; exit 1' TERM INT

cd $SCRATCH_DIR

export I_MPI_PMI_VALUE_LENGTH_MAX=512
#################### EXECUTABEL ############################## 
srun -n 32 /mnt/research/barone/VASP/vasp.6.3.2-sol/vasp_std > vasp.out
status=$?
#################### EXECUTABEL ############################## 


# Copy back essential results regardless of success
cp $SCRATCH_DIR/vasp.out $SUBMIT_DIR/

for file in CONTCAR OUTCAR OSZICAR XDATCAR vasprun.xml vasp.out; do
    if [ -f "$file" ]; then
        cp "$SCRATCH_DIR/$file" "$SUBMIT_DIR/"
    fi
done

# Archive scratch directory if failed
if [ $status -ne 0 ]; then
    cp -r $SCRATCH_DIR $SUBMIT_DIR/FAILED_${RUNID}
    echo "Job with RUNID $RUNID failed. Copied scratch dir for debugging."
else
    rm -f $SCRATCH_DIR/WAVECAR
    rm -f $SCRATCH_DIR/CHG
    echo "JOB with RUNID $RUNID completed successfully."
    touch $SCRATCH_DIR/DONE
    cp $SCRATCH_DIR/DONE $SUBMIT_DIR/
fi

