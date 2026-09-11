#!/bin/bash

echo "What is your name?"
    read name
echo "hello $name!"

echo "What is your age?"
    read age
if [ $age -ge 18 ]; then
    echo "you are 18 or older and access granted"
else
    echo "you are a twerp, entry denied"
fi