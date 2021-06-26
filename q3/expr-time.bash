#!/bin/bash

for i in $(seq 100 100 1000)
do
    Q3_N=$i Q3_D=100 python main.py
done | grep "time:: " | sed "s/time:: //g" > result-time.csv

gnuplot < fig-time.plt