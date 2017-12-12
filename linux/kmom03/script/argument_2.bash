#!/bin/bash
EVENT="$1"

if [ "$EVENT" = "d" ]; then
    now=$(date)
    echo "$now"
elif [ "$EVENT" = "n" ]; then
    for x in {1..20}; do
        echo "$x"
    done
elif [ "$EVENT" = "a" ]; then
    if [ "$2" ]; then
        echo "$2"
    else
        echo "Missing argument"
    fi
fi
