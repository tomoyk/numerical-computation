# gnuplot < fig-time.plt

# CSV
set datafile separator ","

# Save
set terminal png
set output "graph-time.png"

# Font
set tics font "Times New Roman, 18"
set xlabel font "Times New Roman, 18"
set ylabel font "Times New Roman, 18"
set key font "Times New Roman, 18"

# Axis
set logscale xy
set xlabel "n"
set ylabel "cpu time"

# Grids
set grid linetype 1 linecolor 0 mxtics mytics

# Legends
set key left top

plot "result-time.csv" title "CG" with linespoints linewidth 2, \
     "../q2/result-time.csv" title "Gauss" with linespoints linewidth 2
replot
# pause -1