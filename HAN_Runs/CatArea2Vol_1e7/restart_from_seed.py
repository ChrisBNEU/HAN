restartFromSeed(path='seed')

# Data sources
database(
    thermoLibraries=['surfaceThermoPt', 
                     'primaryThermoLibrary',
                     'thermo_DFT_CCSDTF12_BAC',
                     'DFT_QCI_thermo',
                     'NOx2018',
                     'NitrogenCurran',
                     'primaryNS',
                     'autotst-han-library',
                    ],
    reactionLibraries = [('Surface/CPOX_Pt/Deutschmann2006', True),  # when Ni is used, change the library to Surface/Deutschmann_Ni
                         'BurkeH2O2inN2',
                         ('NOx2018', True),
                         'Nitrogen_Glarborg_Lucassen_et_al',
                         'Nitrogen_Glarborg_Zhang_et_al',
                         'Nitrogen_Glarborg_Gimenez_et_al',
                         ],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies =['default', 
	# specifying exactly which surface families we want to use
	# can also just use 'surface' for default surface families
    	'Surface_Abstraction',
	'Surface_Abstraction_vdW',
	'Surface_Addition_Single_vdW',
	#'Surface_Adsorption_Abstraction_vdW',
	#'Surface_Adsorption_Bidentate',
	'Surface_Adsorption_Dissociative',
	'Surface_Adsorption_Double',
	'Surface_Adsorption_Single',
	'Surface_Adsorption_vdW',
	#'Surface_Bidentate_Dissociation',
	'Surface_Dissociation',
	'Surface_Dissociation_Double_vdW',
	'Surface_Dissociation_vdW',
	'Surface_Dual_Adsorption_vdW',
	'Surface_EleyRideal_Addition_Multiple_Bond',
	'Surface_Migration',
	#'Surface_Recombination',
	'Surface_Dissociation_Beta',
	 ],
    kineticsEstimator = 'rate rules',
)


# Some reference values you can use below in the catalystProperties block
bindings = {}
densities = {}
bindings['Pt(111)'] = {  # default values for Pt(111)
                       'C':(-7.02515507E+00, 'eV/molecule'),
                       'O':(-3.81153179E+00, 'eV/molecule'),
                       'N':(-4.63224568E+00, 'eV/molecule'),
		               'H':(-2.75367887E+00, 'eV/molecule'),
                       }
densities['Pt(111)'] = (2.483E-09, 'mol/cm^2')  # default for Pt(111)
bindings['Ir(111)'] = {  # default values for Ir(111)
                       'C':(-7.25234155E+00, 'eV/molecule'),
                       'O':(-4.35235655E+00, 'eV/molecule'),
                       'N':(-5.06204488E+00, 'eV/molecule'),
		               'H':(-2.67673532E+00, 'eV/molecule'),
                       }
densities['Ir(111)'] = (2.587E-09, 'mol/cm^2')  # default for Ir(111)
bindings['Rh(111)'] = {  # default values for Rh(111)
                       'C':(-7.33483762E+00, 'eV/molecule'),
                       'O':(-4.71419163E+00, 'eV/molecule'),
                       'N':(-5.30055389E+00, 'eV/molecule'),
		               'H':(-2.83000775E+00, 'eV/molecule'),
                       }
densities['Rh(111)'] = (2.656E-09, 'mol/cm^2')  # default for Rh(111)

catalystProperties(  # specifying which catalyst to run the simulation on
    bindingEnergies = bindings['Pt(111)'],
    surfaceSiteDensity= densities['Pt(111)'],
)

# List of species
species(
    label='X',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)

species(
    label = 'NH3',
    reactive = True,
    structure=SMILES('N')
)

species(
    label='NH2OH',
    reactive=True,
    structure=SMILES("NO"),
)

species(
    label='HNO3',
    reactive=True,
    structure=SMILES("[O-][N+](=O)O"),
)

species(
    label='CH3OH',
    reactive=True,
    structure=SMILES("CO"),
)

species(
    label='H2O',
    reactive=True,
    structure=SMILES("O"),
)

## Other things for naming purposes
species(
    label='N2',
    reactive=True,
    structure=SMILES("N#N"),
)

species(
   label='O2',
   reactive=True,
   structure=adjacencyList(
       """
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
"""),
)

species(
    label='NO2',
    reactive=True,
    structure=adjacencyList("""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 O u1 p2 c0 {1,S}
"""),
)

species(
    label='NO',
    reactive=True,
    structure=adjacencyList("""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
"""),
)

species(
    label='N2O',
    reactive=True,
    structure=adjacencyList("""
1 N u0 p0 c+1 {2,D} {3,D}
2 N u0 p2 c-1 {1,D}
3 O u0 p2 c0 {1,D}
"""),
)

species(
    label='CO2',
    reactive=True,
    structure=SMILES("O=C=O"),
)

species(
    label='H2',
    reactive=True,
    structure=SMILES("[H][H]"),
)

species(
    label='CO',
    reactive=True,
    structure=SMILES("[C-]#[O+]"),
)

species(
    label='CH4',
    reactive=True,
    structure=SMILES("C"),
)

species(
    label='C2H6',
    reactive=True,
    structure=SMILES("CC"),
)

species(
    label='CH2O',
    reactive=True,
    structure=SMILES("C=O"),
)

species(
    label='CH3',
    reactive=True,
    structure=SMILES("[CH3]"),
)

species(
    label='C3H8',
    reactive=True,
    structure=SMILES("CCC"),
)

species(
    label='H',
    reactive=True,
    structure=SMILES("[H]"),
)

species(
    label='C2H5',
    reactive=True,
    structure=SMILES("C[CH2]"),
)

species(
    label='HCO',
    reactive=True,
    structure=SMILES("[CH]=O"),
)

species(
    label='CH3CHO',
    reactive=True,
    structure=SMILES("CC=O"),
)

species(
    label='OH',
    reactive=True,
    structure=SMILES("[OH]"),
)

species(
    label='C2H4',
    reactive=True,
    structure=SMILES("C=C"),
)

#----------
# Reaction systems


surfaceReactor(
    temperature=[(400,'K'),(2300,'K')],
    initialPressure=(1.0, 'bar'),
    nSims = 6,
    initialGasMoleFractions={
        'NH2OH': 0.31940968187635516,
        'HNO3': 0.35048479213953954,
        'NH3': 0.031075110263184432,
        'CH3OH': 0.20701222018021495,
        'H2O': 0.09201819554070598,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(1.e7, 'm^-1'), # upper limit
    terminationConversion = { "CH3OH": 0.995,},
    terminationTime=(10., 's'),
)


simulator(
    atol=1e-19,
    rtol=1e-12,
)

# First 100 species added with epsilon (move to core) e=0.25 (quite loose)
#notes on each setting are from the RMG cookbook
model(
    # determines the relative flux to put a species into the core.
    # A smaller value will result in a larger, more complex model
    # when running a new model, it is recommended to start with higher values and then decrease to converge on the model
    # attempt with suggested 1/10 to 1/00 toleranceMoveToCore    
    toleranceKeepInEdge=0.0025, 
    # comment out the next three terms to disable pruning
    # determines the relative flux needed to not remove species from the model.
    # Lower values will keep more species and utilize more memory
    # leave at 0.25, as low as 0.1 suggested for combustion 
    toleranceMoveToCore=0.25, 
    # determines when to stop a ODE run to add a species.
    # Lower values will improve speed.
    # if it is too low, may never get to the end simulation to prune species.
    # must be greater than toleranceMoveToCore
    toleranceInterruptSimulation=1,
    # number of edge species needed to accumulate before pruning occurs
    # larger values require more memory and will prune less often
    # leave at 100, higher values require more resources. 
    minCoreSizeForPrune=100,
    # prune before simulation based on thermo
    toleranceThermoKeepSpeciesInEdge=0.5,
    # make sure that the pruned edge species have existed for a set number of RMG iterations.
    # the user can specify to increase it from the default value of 2
    minSpeciesExistIterationsForPrune=3,
    # filter the reactions during the enlarge step to omit species from reacting if their
    # concentration are deemed to be too low
    # Not Implemented for SurfaceReactor
    filterReactions=False, 
)

# reduce epsilon to e=0.1


options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=False,
    generatePlots=False,
    saveEdgeSpecies=False,
    saveSimulationProfiles=True,
)

generatedSpeciesConstraints(  # don't forbid species that show up in the input file or in specified reaction libraries
    allowed=['input species','reaction libraries'],
)
