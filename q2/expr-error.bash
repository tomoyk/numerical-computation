#!/bin/bash

for i in $(seq 100 100 1000)
do
    Q2_N=100 Q2_D=$i python main.py
done | grep "error:: " | sed "s/error:: //g" > result-error.csv

gnuplot < fig-error.plt