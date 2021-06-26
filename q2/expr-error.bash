#!/bin/bash

for i in $(seq 100 100 500)
do
    Q2_N=$i Q2_D=100 python main.py
done | tee -a result-error.txt
