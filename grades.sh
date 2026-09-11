#!/bin/bash

score="93"

if [ $score -ge 90 ] && [ $score -le 100 ]; then
    echo "Excellent!"
elif [ $score -ge 80 ] && [ $score -lt 89 ]; then
    echo "Good Job!"
elif [ $score -ge 70 ] && [ $score -lt 79 ]; then
    echo "Keep Practicing!"
else
    echo "More Practice Needed!"
fi