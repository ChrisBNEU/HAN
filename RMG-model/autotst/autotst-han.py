#%%
import time
import os
import pickle
import subprocess
import multiprocessing
from multiprocessing import Process
import logging
FORMAT = "%(filename)s:%(lineno)d %(funcName)s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
from hotbit import Hotbit

from rmgpy.data.kinetics import KineticsLibrary
from autotst.calculator.gaussian import Gaussian
from autotst.species import Species
from autotst.job.job import Job
from multiprocessing import Manager, Process
from rmgpy.molecule import Molecule as RMGMolecule 
from rmgpy.species import Species as RMGSpecies

#%%
if os.getenv('SLURM_ARRAY_TASK_ID'):
    i = int(os.getenv('SLURM_ARRAY_TASK_ID'))
else:
    #raise Exception("Specif y a TS number!")
    logging.warning("Number not specified as script argument or via environment variable, so using default")
    i = 10

logging.info("Running with job number : {}".format(i))

#%%

logging.info("Loading species dictionary...")
path_to_dict = "../chemkin/species_dictionary.txt"
species_dict = KineticsLibrary().get_species(path_to_dict)
logging.info("There are {} species to process...".format(len(species_dict)))

#%%

species_name, rmg_species = list(species_dict.items())[i-1]
logging.info("Performing calculations for {} : {}".format(species_name, rmg_species))
autotst_species = Species(rmg_species=rmg_species)
logging.info("Successfully created an AutoTST species for {}...".format(species_name))

#%%

directory = "/scratch/westgroup/HANscratch" #Feel free to edit to a different directory

job = Job(
    calculator=Gaussian(
        settings={
            "method": "m062x",
            "basis": "cc-pVTZ",
            "mem": "5GB",
            "nprocshared": 20,
        },
        directory = directory 
    ),
    conformer_calculator=Hotbit(),
    partition="general"
)

logging.info("Sumbitting low energy conformers for calculation")
result = job.calculate_species(species=autotst_species)

if result:
    print("AutoTST successfully arrived at an optimized geometry for {}".format(autotst_species))
else:
    print("AutoTST could not arrive at an optimized geometry for {} :(".format(autotst_species))

print("All geometries completed")
print("Done!")
