# gnuplot < fig-error.plt

# CSV
set datafile separator ","

# Save
set terminal png
set output "graph-error.png"

# Font
set tics font "Times New Roman, 14"
set xlabel font "Times New Roman, 18"
set ylabel font "Times New Roman, 18"
set key font "Times New Roman, 14"

# Axis
set logscale xy
set xlabel "Size"
set ylabel "Error"
set nokey

plot "result.csv" using 2:xtic(1) with linespoints

# pause -1