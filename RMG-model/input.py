# Data sources
database(
    thermoLibraries=['surfaceThermoPt', 
                     'primaryThermoLibrary',
                     'thermo_DFT_CCSDTF12_BAC',
                     'DFT_QCI_thermo',
                     'NOx2018',
                     'Nitrogen_G4',
                     'NitrogenCurran',
                     'primaryNS',
                     'autotst-han-library',
                    ],
    reactionLibraries = [('Surface/CPOX_Pt/Deutschmann2006', True),
                         'BurkeH2O2inN2',
                         'NOx2018',
                         'Nitrogen_Glarborg_Lucassen_et_al',
                         'Nitrogen_Glarborg_Zhang_et_al',
                         'Nitrogen_Glarborg_Gimenez_et_al',
                         ],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies =['default', 
        'Surface_Adsorption_Single',
        'Surface_Adsorption_vdW',
        'Surface_Adsorption_Dissociative',
        'Surface_Dissociation',
        'Surface_Abstraction',
        'Surface_EleyRideal_Addition_Multiple_Bond',
        'Surface_Migration',
        'Surface_Dissociation_Double_vdW',
        'Surface_Addition_Single_vdW',
        'Surface_Dissociation_vdW',
        'Surface_Abstraction_vdW',
        'Surface_Dual_Adsorption_vdW',
        #broken: 'Surface_Recombination_Single',
        'Surface_Adsorption_Abstraction_vdW',
        ],
    kineticsEstimator = 'rate rules',
)

# Some reference values you can use below in the catalystProperties block
bindings = {}
densities = {}
bindings['Pt(111)'] = { 
                       'C':(-7.02515507E+00, 'eV/molecule'),
                       'O':(-3.81153179E+00, 'eV/molecule'),
                       'N':(-4.63224568E+00, 'eV/molecule'),
		               'H':(-2.75367887E+00, 'eV/molecule'),
                       }
densities['Pt(111)'] = (2.483E-09, 'mol/cm^2')
bindings['Ir(111)'] = { 
                       'C':(-7.25234155E+00, 'eV/molecule'),
                       'O':(-4.35235655E+00, 'eV/molecule'),
                       'N':(-5.06204488E+00, 'eV/molecule'),
		               'H':(-2.67673532E+00, 'eV/molecule'),
                       }
densities['Ir(111)'] = (2.587E-09, 'mol/cm^2')
bindings['Rh(111)'] = { 
                       'C':(-7.33483762E+00, 'eV/molecule'),
                       'O':(-4.71419163E+00, 'eV/molecule'),
                       'N':(-5.30055389E+00, 'eV/molecule'),
		               'H':(-2.83000775E+00, 'eV/molecule'),
                       }
densities['Rh(111)'] = (2.656E-09, 'mol/cm^2')

catalystProperties(
    bindingEnergies = bindings['Ir(111)'],
    surfaceSiteDensity= densities['Ir(111)'],
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
    temperature=[(400,'K'),(2000,'K')],
    initialPressure=(1.0, 'bar'),
    nSims = 4,
    initialGasMoleFractions={
        'NH2OH': 0.450974,
        'HNO3': 0.481448,
        'NH3': 0.0304738,
        'CH3OH': 0.0325297,
        'H2O': 0.00457386,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(1.e7, 'm^-1'), # Quite high
    terminationConversion = { "CH3OH": 0.99,},
    terminationTime=(10., 's'),
)

surfaceReactor(
    temperature=[(400,'K'),(2000,'K')],
    initialPressure=(1.0, 'bar'),
    nSims = 4,
    initialGasMoleFractions={
        'NH2OH': 0.450974,
        'HNO3': 0.481448,
        'NH3': 0.0304738,
        'CH3OH': 0.0325297,
        'H2O': 0.00457386,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(1.e5, 'm^-1'), # Medium
    terminationConversion = { "CH3OH": 0.99,},
    terminationTime=(10., 's'),
)

surfaceReactor(
    temperature=[(400,'K'),(2000,'K')],
    initialPressure=(1.0, 'bar'),
    nSims = 4,
    initialGasMoleFractions={
        'NH2OH': 0.450974,
        'HNO3': 0.481448,
        'NH3': 0.0304738,
        'CH3OH': 0.0325297,
        'H2O': 0.00457386,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(348, 'm^-1'), # Lower limit
    terminationConversion = { "CH3OH": 0.99,},
    terminationTime=(10., 's'),
)


simulator(
    atol=1e-18,
    rtol=1e-16,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.25,
    toleranceInterruptSimulation=0.25, 
    minCoreSizeForPrune=100,
    toleranceThermoKeepSpeciesInEdge=0.5, # prune before simulation based on thermo
    minSpeciesExistIterationsForPrune=3,
    filterReactions=False, # NotImplemented for SurfaceReactor
    maxNumSpecies=100,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.1,
    toleranceInterruptSimulation=1e6, # inturrupt tolerance was 0.1 w/out pruning, 1e8 w pruning on
    maximumEdgeSpecies=50000,
    minCoreSizeForPrune=100,
    toleranceThermoKeepSpeciesInEdge=0.5, # prune before simulation based on thermo
    minSpeciesExistIterationsForPrune=3, # prune rxns from edge that dont move into core
    filterReactions=False, # NotImplemented for SurfaceReactor
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.01,
    toleranceInterruptSimulation=1e8, # inturrupt tolerance was 0.1 w/out pruning, 1e8 w pruning on
    maximumEdgeSpecies=50000,
    minCoreSizeForPrune=100,
    toleranceThermoKeepSpeciesInEdge=0.5, # prune before simulation based on thermo
    minSpeciesExistIterationsForPrune=3, # prune rxns from edge that dont move into core
    filterReactions=False, # NotImplemented for SurfaceReactor
)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=False,
    saveSimulationProfiles=True,
)

generatedSpeciesConstraints(
    allowed=['input species','reaction libraries'],
)
