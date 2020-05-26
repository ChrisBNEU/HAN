#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=24:00:00
#SBATCH --mem=120Gb
#SBATCH --job-name=HAN8TEST
#SBATCH --output=HAN.log
#SBATCH --partition=short
#SBATCH --cpus-per-task=4
#SBATCH --ntasks=1

source activate rmg_env_han
export RMGPY_HAN=/home/blais.ch/RMG_HAN_env/RMG-Py
python $RMGPY_HAN/rmg.py input.py
