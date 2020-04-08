#!/bin/bash
#SBATCH --array=0-35%36
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=1
#SBATCH --time=00:29:59
#SBATCH --mem=8Gb
#SBATCH --job-name=rocket-graph
#SBATCH --partition=short
#SBATCH --output=rocketman-graph-%a-slurm.log
##SBATCH --exclude=c[5003]


source activate rmg_env
export RMGpy=/scratch/nadeau.ma/RMG-Py

mkdir -p rocketman/$SLURM_ARRAY_TASK_ID
rm -rf rocketman/$SLURM_ARRAY_TASK_ID/*
cp -f rocketman-graph.ipynb rocketman/$SLURM_ARRAY_TASK_ID/
cp -f ../RMG-model/cantera/chem_annotated.cti rocketman/$SLURM_ARRAY_TASK_ID/
cd rocketman/$SLURM_ARRAY_TASK_ID
jupyter nbconvert --ExecutePreprocessor.timeout=None \
                  --ExecutePreprocessor.allow_errors=True \
                  --to notebook \
                  --execute \
                  --inplace \
                  rocketman-graph.ipynb
#jupyter nbconvert --to markdown rocketman.ipynb
