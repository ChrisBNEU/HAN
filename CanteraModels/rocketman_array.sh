#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=00:59:59
#SBATCH --mem=30Gb
#SBATCH --job-name=rocket
#SBATCH --output=rocketman/%a/slurm.log
#SBATCH --partition=general
#SBATCH --exclude=c[5003]
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=1
#SBATCH --array=35%24

source activate rmg3
export RMGpy=/scratch/r.west/RMG-Py

mkdir -p rocketman/$SLURM_ARRAY_TASK_ID

cp -f rocketman.ipynb rocketman/$SLURM_ARRAY_TASK_ID/
cp -f ../RMG-model/cantera/chem_annotated.cti rocketman/$SLURM_ARRAY_TASK_ID/
cd rocketman/$SLURM_ARRAY_TASK_ID
jupyter nbconvert --to notebook --execute rocketman.ipynb
