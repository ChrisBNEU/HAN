#!/bin/bash
#SBATCH --array=1-20
#SBATCH -n 1
#SBATCH --time=0:30:00
#SBATCH -o "tocantera-%a.out"

mkdir -p cantera

# If not part of a slurm array job, or if the first of a slurm array job
# Then convert the annotated chemkin file
if [ -z "$SLURM_ARRAY_TASK_ID" ] || ["$SLURM_ARRAY_TASK_ID" -eq 1 ]
then
    echo annotated
    $(dirname $(which python))/ck2cti --input=chemkin/chem_annotated-gas.inp --surface=chemkin/chem_annotated-surface.inp --transport=chemkin/tran.dat --output=cantera/chem_annotated.cti
fi

# If not part of a slurm array job
# then ext now
if [ -z "$SLURM_ARRAY_TASK_ID" ]
then
    exit
fi

# If part of a slurm array job.
# task 1 does 0001, 0021, 0041, etc. up to 0501
# task 20 does 0020, 0040, 0060, etc. up to 0520
trap "exit" INT
for ((i=0;i<=25;i++)); 
do 
    let "j = 20 * $i + $SLURM_ARRAY_TASK_ID"
    oi=$(printf "%04d" $j)
    echo $oi
    ls chemkin/chem$oi-gas.inp &&  $(dirname $(which python))/ck2cti --input=chemkin/chem$oi-gas.inp --surface=chemkin/chem$oi-surface.inp --transport=chemkin/tran.dat --output=cantera/chem$oi.cti
done
