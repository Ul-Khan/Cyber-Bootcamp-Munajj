#!/bin/bash

echo "what is your name?"
    read name
echo "hello $name!"

echo "which path do you wish to take?"
    read path

if [ $path = "left" ]; then
    echo "you have chosen the left path, you are destined for greatness"
    echo "Upon this path you will find riches, but beware of those who seek what you have "$name""
    echo "What is it that you seek on this path?"
    read seek
    echo "you seek $seek on the left path, very well, you shall have it"
elif [ $path = "right" ]; then
    echo "you have chosen the right path, you may be doomed"
    echo "What is it that you seek on this path?"
    read seek
    echo "you seek $seek on the right path, very well, I shall make sure you never attain it"
else
    echo " no path was chosen, you shall perish in the void"
fi