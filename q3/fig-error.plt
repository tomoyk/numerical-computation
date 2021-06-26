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
set xlabel "d"
set ylabel "error"

plot "result-error.csv" with linespoints

# pause -1