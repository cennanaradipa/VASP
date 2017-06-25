# Gnuplot script file for plotting band structure 
set terminal aqua size 600,900 font "Helvetica,14" enhanced dashed 
set grid
unset key
set xtic ("{/Symbol G}" 0.0000, "X" 0.5,"M" 1.0,"Z" 1.86602540, "{/Symbol G}" 2.36602540)
set ytic 2
set yrange [-7:4]
set xrange [0:2.36602540]
set title "Band Structure of i4mmm LCO using VASP"
set ylabel "Energy (E-E_{fermi})  (eV)"
set xlabel "Symmetry Points"
filename = ARG1
plot for [IDX=0:67] filename  i IDX u 1:2 t columnheader w lines lc 1, \
     for [IDX=0:67] filename  i IDX u 1:3 t columnheader w lines lc 2 dt 2
