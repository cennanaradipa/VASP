#!/usr/bin/python
# Muhammad Avicenna Naradipa
# Mod 5/5/2017 cennanaradipa: added gnuplot plotting, kpoints
# Forked from Ryan Valenza
# Post-processing for EIGENVAL file to plot bandstructures

import sys
import re
import math
import numpy as np
try:
	eigenval = open("EIGENVAL","r")
except IOError:
	sys.exit("Could not open EIGENVAL")

eigenval.readline() # N/A
eigenval.readline() # N/A
eigenval.readline() # N/A
eigenval.readline() # Cartesian/Direct

# System name w/ stripped newline character
name = eigenval.readline().rstrip() 
print "# System:        " + name

# Important information
first = eigenval.readline()
(nelect,nkpts,nbands) = first.split()
print "# of electrons:  " + nelect
print "# of k-points:   " + nkpts
print "# of bands:      " + nbands

# Details for easy plotting
fermi = float(input("\n What is the Fermi Energy in eV? \n (Check from OUTCAR) \n"))
print "Fermi Energy is set to ",fermi

spin  = raw_input("\n Is it spin polarized (y/n)? \n (ISPIN = 2) \n")
if spin == 'y':
    print "\n Taking two bands from EIGENVAL"
else:
    print "\n Taking one band from EIGENVAL"
print "Creating bands_man.txt"
#-------------------------------------------------- 
# Begin collecting data
#-------------------------------------------------- 

# Initialization of bands, kpoints
k     = [[0]*3 for i in range(int(nkpts))]
bands = np.zeros((int(nkpts),int(nbands),2))
xcor  = []

# Open file for writing
out = open("bands_man.txt","w")

out.write("# These are the rewritten results of VASP calculation based on an EIGEIGENVAL file \n")
out.write("# Some details include:")
out.write("# Number of electrons %s\n"%nelect)
out.write("# Number of k-points  %s\n"%nkpts)
out.write("# Number of bands     %s\n"% nbands)
out.write("# This has been formattted to gnuplot's indexing format \n")
out.write("# Plot using this format:\n")
out.write("#    plot for [IDX] i IDX u 1:2 w lines title \"columnheader(1)\"\n")

for i in range(int(nkpts)):
    
    # empty line
    eigenval.readline()
    
    # Split values inside lines 
    kptline = eigenval.readline()
    # print kptline
    (kx,ky,kz,enval) = kptline.split()

    # Ignore the first index
    if i == 0:
        k_tot = float(0)

    # If not the first index, find mod
    else:
        k[i][0] = float(kx)
        k[i][1] = float(ky)
        k[i][2] = float(kz)
        k_tot += math.sqrt( \
                (k[i][0]-k[i-1][0])**2 + \
                (k[i][1]-k[i-1][1])**2 + \
                (k[i][2]-k[i-1][2])**2)
    
    xcor.append(k_tot)
    for j in range(int(nbands)):
        bandline = eigenval.readline()
        if spin == 'y':
            (bndnum,up,down,weightup,weightdown) = bandline.split() 
            bands[i][j][0] = float(up)
            bands[i][j][1] = float(down)
            #print bands[j]
        else:
            (bndnum,nospin,weight) = bandline.split()
            bands[i][j][0] = float(nospin)
        
for i in range(int(nbands)):
    out.write("\n\"Band #%d\" \n"%(i+1))
    for j in range(int(nkpts)):
        out.write("%.8f %.8f %.8f \n"%(xcor[j],
            bands[j][i][0] - fermi,
            bands[j][i][1] - fermi)) 

