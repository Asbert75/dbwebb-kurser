#!/bin/bash

#Script for converting Salar.csv into JSON-format.

#.csv format:
#              ,,Koordinater,,,,,,
#Salsnr,Salsnamn,Lat,Long,Ort,Hus,Våning,Typ,Storlek **/

JSTRING=$(jq --slurp --raw-input --raw-output 'split("\n") | .[2:] | map(split(",")) | map({"Salsnr": .[0], "Salsnamn": .[1], "Lat": .[2], "Long": .[3], "Ort": .[4], "Hus": .[5], "Våning": .[6], "Typ": .[7], "Storlek": .[8]})' resources/salar.csv)

echo "${JSTRING//\"\"/null}" > salar.json
