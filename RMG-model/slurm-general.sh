#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=23:59:59
#SBATCH --mem=120Gb
#SBATCH --job-name=HAN
#SBATCH --output=HAN.log
#SBATCH --partition=general
#SBATCH --exclude=c[5003]
#SBATCH --cpus-per-task=4
#SBATCH --ntasks=1

source activate rmg3
export RMGpy=/scratch/r.west/RMG-Py
python $RMGpy/rmg.py -p -n4 -t 00:23:59:00 input.py

