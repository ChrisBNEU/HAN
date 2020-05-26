#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=24:00:00
#SBATCH --mem=120Gb
#SBATCH --job-name=HAN8dbchange
#SBATCH --output=HAN.log
#SBATCH --partition=short
#SBATCH --cpus-per-task=4
#SBATCH --ntasks=1

source activate rmg_env
export RMGPY=/home/blais.ch/RMG_Base_env/RMG-Py
python $RMGPY/rmg.py input.py
