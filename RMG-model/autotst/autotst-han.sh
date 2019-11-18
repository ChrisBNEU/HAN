#!/bin/sh
#set a job name
#SBATCH --job-name=HAN-species

#a file for job output, you can check job progress
#SBATCH --output=log-files/HAN-species.%a.log

# a file for errors from the job
#SBATCH --error=log-files/HAN-species.%a.log

#SBATCH -N 1
#SBATCH -n 2
##SBATCH --ntasks-per-node=12
#SBATCH --partition=west
#SBATCH --mem=5GB
#SBATCH --exclude=c3040,c5003
#SBATCH --array=1-104%40

source activate rmg3
python autotst-han.py
