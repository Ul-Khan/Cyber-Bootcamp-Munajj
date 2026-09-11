#!/bin/bash

echo "What is your name?"
    read name
echo "hello $name!"
echo "I'm going to guess your age!"
    read age
if [ $age -ge 18 ]; then