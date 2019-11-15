## Thermo calculator

1. Update the `autotst_han.sh` file so the array line
```
#SBATCH --array=1-168%40
```
corresponds to the number of species in the latest RMG model,
i.e. number of entries in `../chemkin/species_dictionary.txt`

2. Run `sbatch autotst_han.sh`

3. Wait for the jobs to run. They will end up in the 
`/scatch/westgroup/HANsratch/species/` directory.

4. Launch the `get-thermo` notebook. Run it to the end.
this will process all the results found in 
`/scatch/westgroup/HANsratch/species/`
and make a new thermo library called
`autotst-han-library.py` 
which can be used in RMG.