VASP scripts
============
This project is a fork from Ryan Valenza's repo, which you can check out just under the repo name. Currently I am doing a spin polarized calculation with DFT+U to obtain optical propertie using VASP. The goal is to match the experimental data, giving additional evidence for the arguments to be put into the paper. I had trouble directly using Valenza's script as I don't use matpotlib and the symmetry points are different.

### readEIGENVAL.py

The modificiations I made are mostly on this script. I'm still a bit new to Python, so there might be some redundancies in the code. Here's a list of all the changes I've added:

* Corrected kpoint coordinates so that it will add up per increment of the absolute difference between each kpoint
* I wanted to keep the regular expression method used by Valenza, but since I saw another script giving similar results using for loops, I went and change about 90% of the code to fit it. 
* I added the functionality to be able to input spin polarization calculations
* Values of bands will be shifted to the Fermi level, therefore you need to input the Fermi energy beforehand
* Plotting is optimized for gnuplot's indexing format, however this can be modified easily

### readDOSCAR.py

So far the most manageable way to plot the dos is to simply take the values that are relevant based on on the INCAR files, dump them to a .dat or .text file, and plot using gnuplot or any other plotting software. Detailed DOS can be deciphered if we look into the vasprun.xml file and the basic format shown in VASP manual, but a script is needed to sort this out for systems with large number of atoms. The old script by Valenza is for non-spin polarization calculations, so I did not use them. The format for spin polarized is simple, located at the first batch of data in the DOSCAR file.

### Other files on this repo

I have deleted some of the files that are specific to the old project by Valenza.  I will keep the files for VASP scripting purposes and will modify them as soon as needed. 

# Author: Muhammad Avicenna Naradipa 
