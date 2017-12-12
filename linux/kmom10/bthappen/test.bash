#!/bin/bash

PORT="1337"
SERVER="localhost"
VERBOSE=false

if [[ ${LINUX_PORT+x} ]]; then
    PORT=$LINUX_PORT
fi

if [[ ${LINUX_SERVER+x} ]]; then
    SERVER=$LINUX_SERVER
fi

ADDRESS="http://$SERVER:$PORT"

function testPaths {
    testPath "$ADDRESS/"

    testPath "$ADDRESS/room/list?max=1"
    testPath "$ADDRESS/room/list?max=3"
    testPath "$ADDRESS/room/list?max=5"
    testPath "$ADDRESS/room/list?max=6"

    testPath "$ADDRESS/room/view/id/2-128"
    testPath "$ADDRESS/room/view/id/3-225"
    testPath "$ADDRESS/room/view/id/3-222"
    testPath "$ADDRESS/room/view/id/someId"

    testPath "$ADDRESS/room/view/house/karlshamn"
    testPath "$ADDRESS/room/view/house/A-huset"
    testPath "$ADDRESS/room/view/house/H-Huset"
    testPath "$ADDRESS/room/view/house/Modellverkstad?max=2"

    testPath "$ADDRESS/room/search/karlshamn?max=5"
    testPath "$ADDRESS/room/search/karlshamn"
    testPath "$ADDRESS/room/search/video"
    testPath "$ADDRESS/room/search/rummet"
}


function testPath {
    if [[ "$VERBOSE" = true ]]; then
        echo " "
        echo " "
        echo "Testing URL: $1"
        curl -s -o /dev/null -I -w '%{http_code}' "$1"
        echo " "
        curl -s "$1"
        echo " "
        read -n 1 -s -p "Press any key to continue"
    else
        echo " "
        echo "Testing URL: $1"
        curl -s -o /dev/null -I -w '%{http_code}' "$1"
        echo " "
        read -n 1 -s -p "Press any key to continue"
    fi
}


# Process options
while (( $# ))
do
    case "$1" in

        --verbose | -v)
            VERBOSE=true
            testPaths

            exit 0
        ;;

        *)

            exit 1
        ;;

    esac
done

# Run function if --verbose was not entered
if [[ "$VERBOSE" = false ]]; then
    testPaths
fi



exit 1
