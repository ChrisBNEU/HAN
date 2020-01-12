#!/bin/bash
#SBATCH --array=0-35%24
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=1
#SBATCH --time=00:29:59
#SBATCH --mem=8Gb
#SBATCH --job-name=rocket
#SBATCH --partition=west
#SBATCH --output=rocketman-%a-slurm.log
##SBATCH --exclude=c[5003]


source activate rmg3
export RMGpy=/scratch/r.west/RMG-Py

mkdir -p rocketman/$SLURM_ARRAY_TASK_ID

cp -f rocketman.ipynb rocketman/$SLURM_ARRAY_TASK_ID/
cd rocketman/$SLURM_ARRAY_TASK_ID
jupyter nbconvert --to notebook --execute rocketman.ipynb
