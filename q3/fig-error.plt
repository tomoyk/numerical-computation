# gnuplot < fig-error.plt

# CSV
set datafile separator ","

# Save
set terminal png
set output "graph-error.png"

# Font
set tics font "Times New Roman, 18"
set xlabel font "Times New Roman, 18"
set ylabel font "Times New Roman, 18"
set key font "Times New Roman, 18"

# Axis
set logscale xy
set xlabel "n"
set ylabel "error"

plot "result-error.csv" title "CG" with linespoints, \
     "../q2/result-error.csv" title "Gauss" with linespoints

# pause -1