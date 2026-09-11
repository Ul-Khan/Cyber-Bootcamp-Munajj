#!/bin/bash

score="90"

if [ $score -ge 90 ]; then
    echo "Grade A"
elif [ $score -ge 80 ]; then
    echo "Grade B"
elif [ $score -ge 70 ]; then 
    echo "Grade C"
elif [ $score -ge 60 ]; then
    echo "Grade D"
else
    echo "FAILED"
    fi