#!/bin/bash
if [ "$1" -eq 5 ]; then
    echo "Same!"
elif [ "$1" -gt 5 ]; then
    echo "Higher!"
else
    echo "Lower!"
fi
