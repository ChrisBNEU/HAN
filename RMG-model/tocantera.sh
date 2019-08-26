#!/bin/bash
mkdir -p cantera
$(dirname $(which python))/ck2cti --input=chemkin/chem_annotated-gas.inp --surface=chemkin/chem_annotated-surface.inp --transport=chemkin/tran.dat --output=cantera/chem_annotated.cti
