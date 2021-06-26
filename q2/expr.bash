#!/bin/bash

for i in $(seq 100 100 500)
do
    Q2_N=300 Q2_D=$i python main.py
done
