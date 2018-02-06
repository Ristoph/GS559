### Chris Braden PS4 question 5
##
## GIVEN: two files containing amino acid masses and nitrogens, and a query sequence
## RETURN: a message restating the query sequence, and denoting the monoisotopic mass and the heavy-N mass to
##         three decimal places

import sys


mass_file = open(sys.argv[1], 'r')
nit_file = open(sys.argv[2], 'r')
seq = list(sys.argv[3])

mass_lib = {} # initialize libraries for storing mass values
nitcount_lib = {}

nmass = float(0.997) # increased mass of heavy N
mono_mass = float() # initialize value for each mass
heavyn_mass = float()


for line in mass_file: # make a library of the masses
    line = line[0:-2]
    line = list(line.rsplit(','))
    mass_lib[line[0]] = line[1]

for line in nit_file: # make a library of the nitrogen counts
    line = line[0:-2]
    line = list(line.rsplit(','))
    nitcount_lib[line[0]] = line[1]

for amino_acid in seq: # add up masses of elements in seq
    mono_mass = mono_mass + float(mass_lib[amino_acid])
    heavyn_mass = heavyn_mass + float(mass_lib[amino_acid]) + (float(nitcount_lib[amino_acid]) * nmass)

mono_mass = mono_mass + 18.0 # add  mass for terminal H and OH
heavyn_mass = heavyn_mass + 18.0

print "The peptide", ''.join(seq), "has a monoisotopic mass of", "%.3f" % mono_mass, "and a heavy_N mass of", "%.3f" % heavyn_mass