#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=unlimited
#SBATCH --mem=120Gb
#SBATCH --job-name=HAN
#SBATCH --output=HAN.log
#SBATCH --partition=west
#SBATCH --exclude=c[5003]
#SBATCH --cpus-per-task=4
#SBATCH --ntasks=1

conda activate rmg3
export RMGpy=/scratch/r.west/RMG-Py
python $RMGpy/rmg.py -p -n4 input.py

