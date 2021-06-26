# gnuplot < fig-error.plt

# CSV
set datafile separator ","

# Save
set terminal png
set output "graph-adv.png"

# Font
set tics font "Times New Roman, 14"
set xlabel font "Times New Roman, 18"
set ylabel font "Times New Roman, 18"
set key font "Times New Roman, 14"

# Axis
set logscale xy
set xlabel "iterations"
set ylabel "|{r_k}| / |{b}|"
set nokey

plot "result-adv.csv" title "CG" with linespoints

# pause -1