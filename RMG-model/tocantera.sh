#!/bin/bash
mkdir -p cantera
$(dirname $(which python))/ck2cti --input=chemkin/chem_annotated-gas.inp --surface=chemkin/chem_annotated-surface.inp --transport=chemkin/tran.dat --output=cantera/chem_annotated.cti

trap "exit" INT
for ((i=10;i<=99;i++)); 
do 
   echo $i
   ls chemkin/chem00$i-gas.inp &&  $(dirname $(which python))/ck2cti --input=chemkin/chem00$i-gas.inp --surface=chemkin/chem00$i-surface.inp --transport=chemkin/tran.dat --output=cantera/chem00$i.cti
done

trap "exit" INT
for ((i=100;i<=999;i++)); 
do 
   echo $i
   ls chemkin/chem0$i-gas.inp && $(dirname $(which python))/ck2cti --input=chemkin/chem0$i-gas.inp --surface=chemkin/chem0$i-surface.inp --transport=chemkin/tran.dat --output=cantera/chem0$i.cti
done
