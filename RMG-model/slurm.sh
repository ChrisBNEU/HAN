#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=unlimited
#SBATCH --mem=120Gb
#SBATCH --job-name=HAN
#SBATCH --output=HAN.log
#SBATCH --partition=west
#SBATCH --exclude=c[5003]
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu=4Gb
#SBATCH --ntasks=1

source activate rmg_env
python $RMGpy/rmg.py -p input.py

