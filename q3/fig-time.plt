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

plot "result-time.csv" title "CG" with linespoints, \
     "../q2/result-time.csv" title "Gauss" with linespoints
# plot "../q2/result-time.csv" title "Gauss" with linespoints
replot
# pause -1