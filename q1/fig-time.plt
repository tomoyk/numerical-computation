# gnuplot < fig-error.plt

# CSV
set datafile separator ","

# Save
set terminal png
set output "graph-time.png"

# Font
set tics font "Times New Roman, 14"
set xlabel font "Times New Roman, 18"
set ylabel font "Times New Roman, 18"
set key font "Times New Roman, 14"

# Axis
# set logscale xy
set xlabel "Size"
set ylabel "Time"
set nokey

# Grids
set grid linetype 1 linecolor 0 mxtics mytics

plot "result-backup.csv" using 3:xtic(1) with linespoints

# pause -1