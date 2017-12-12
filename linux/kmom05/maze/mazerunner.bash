#!/bin/bash

SCRIPT=$( basename "$0" )

PORT="1337"
SERVER="localhost"

IFS=","

if [[ ${LINUX_PORT+x} ]]; then
    PORT=$LINUX_PORT
fi

if [[ ${LINUX_SERVER+x} ]]; then
    SERVER=$LINUX_SERVER
fi

ADDRESS="$SERVER:$PORT"

function usage
{
    local usageTxt=(
"Usage: $SCRIPT [options] <command> [arguments]"
""
"Commands:"
"  init             Initiate the game and save the gameId to file"
"  maps             Prints available maps"
"  info             Prints room information"
"  select [map]     Selects a map"
"  enter            Go into the first room"
"  go north         Go into a new room, if the direction is available"
"  go south         Go into a new room, if the direction is available"
"  go east          Go into a new room, if the direction is available"
"  go west          Go into a new room, if the direction is available"
""
"Options:"
"  --help, -h     Print help."
    )

    printf "%s\n" "${usageTxt[@]}"
}

function app-init
{
    curl -s "$ADDRESS/?type=csv" | tail -c 6 > gameId.txt &&
    echo "Game Initialized. ID saved to file 'gameId.txt'."
}

function app-maps
{
    curl -sq "$ADDRESS/map?type=csv" > maps.csv

    MAP0=""
    MAP1=""

    while read m0 m1;
    do
        MAP0=$m0
        MAP1=$m1
    done < maps.csv

    echo "Available maps:"
    echo "0: $MAP0"
    echo "1: $MAP1"
}

function app-select
{
    GAMEID=$(<gameId.txt)

    if [[ "$1" -eq "0" ]]; then
        echo "You selected: maze-of-doom.json"
        curl -s "$ADDRESS/$GAMEID/map/maze-of-doom.json" > /dev/null
    elif [[ "$1" -eq "1" ]]; then
        echo "You selected: small-maze.json"
        curl -s "$ADDRESS/$GAMEID/map/small-maze.json" > /dev/null
    else
        echo "Invalid map choice."
    fi
}

roomId=""
desc=""
west=""
east=""
south=""
north=""

function app-enter
{
    GAMEID=$(<gameId.txt)
    curl -s "$ADDRESS/$GAMEID/maze?type=csv" > room.csv

    echo "You entered the first room."
}

function enterRoom
{
    room=$1
    direction=$2

    GAMEID=$(<gameId.txt)
    curl -s "$ADDRESS/$GAMEID/maze/$room/$direction?type=csv" > room.csv

    while read r d w e s n
    do
        roomId=$r
        desc=$d
        west=$w
        east=$e
        south=$s
        north=$n
    done < room.csv

    if [[ "$desc" = "You found the exit" ]]; then
        echo "You have found the exit! Exiting Game..."
        exit 1
    fi

    echo "You entered room: $roomId"
    echo "Room Description: $desc"

    DIRECTIONS=""
    if [[ "$north" != "-" ]]; then
        DIRECTIONS="north"
    fi

    if [[ "$south" != "-" ]]; then
        DIRECTIONS="$DIRECTIONS south"
    fi

    if [[ "$east" != "-" ]]; then
        DIRECTIONS="$DIRECTIONS east"
    fi

    if [[ "$west" != "-" ]]; then
        DIRECTIONS="$DIRECTIONS west"
    fi

    echo "You can go: $DIRECTIONS"
}

function app-go
{
    while read r d w e s n
    do
        roomId=$r
        desc=$d
        west=$w
        east=$e
        south=$s
        north=$n
    done < room.csv

    if [[ "$1" = "north" ]]; then
        if [[ "$north" = "-" ]]; then
            echo "You can't go that way."
        else
            echo "Walking north, you entered a new room."
            enterRoom "$roomId" "north"
        fi
    elif [[ "$1" = "south" ]]; then
        if [[ "$south" = "-" ]]; then
            echo "You can't go that way."
        else
            echo "Walking south, you entered a new room."
            enterRoom "$roomId" "south"
        fi
    elif [[ "$1" = "east" ]]; then
        if [[ "$east" = "-" ]]; then
            echo "You can't go that way."
        else
            echo "Walking east, you entered a new room."
            enterRoom "$roomId" "east"
        fi
    elif [[ "$1" = "west" ]]; then
        if [[ "$west" = "-" ]]; then
            echo "You can't go that way."
        else
            echo "Walking west, you entered a new room."
            enterRoom "$roomId" "west"
        fi
    else
        echo "Please choose a direction."
    fi
}

function app-info
{
    OLDIFS="$IFS"
    IFS=","
    while read r d w e s n
    do
        roomId=$r
        desc=$d
        west=$w
        east=$e
        south=$s
        north=$n
    done < room.csv
    IFS=$OLDIFS

    echo "Room Description: $desc "

    DIRECTIONS=""
    if [[ "$north" != "-" ]]; then
        DIRECTIONS="north"
    fi

    if [[ "$south" != "-" ]]; then
        DIRECTIONS="$DIRECTIONS south"
    fi

    if [[ "$east" != "-" ]]; then
        DIRECTIONS="$DIRECTIONS east"
    fi

    if [[ "$west" != "-" ]]; then
        DIRECTIONS="$DIRECTIONS west"
    fi

    echo "You can go: $DIRECTIONS"
}

function app-loop
{
    app-init
    echo ""
    app-maps
    echo ""

    STATUS='true'
    while $STATUS; do
        echo "Select map number and press enter: "
        read mapNum
        if [[ "$mapNum" -eq "0" ]]; then
            app-select "$mapNum"
            STATUS=false
        elif [[ "$mapNum" -eq "1" ]]; then
            app-select "$mapNum"
            STATUS='false'
        elif [[ "$mapNum" = "quit" ]]; then
            exit 1
        elif [[ "$mapNum" = "help" ]]; then
            usage
        fi
    done

    echo ""
    app-enter

    STATUS='true'
    while $STATUS; do
        echo ""
        echo "Select a direction and hit enter: (North, West, South, East)"
        read chooseDir
        if [[ "$chooseDir" = "north" ]] || [[ "$chooseDir" = "south" ]] || [[ "$chooseDir" = "west" ]] || [[ "$chooseDir" = "east" ]]; then
            echo ""
            app-go "$chooseDir"
        elif [[ "$chooseDir" = "quit" ]]; then
            exit 1
        elif [[ "$chooseDir" = "help" ]]; then
            usage
        fi
    done
}

# Process options
while (( $# ))
do
    case "$1" in

        --help | -h)
            usage
            exit 0
        ;;

        loop \
        | info    \
        | init     \
        | maps      \
        | select     \
        | enter       \
        | go)
            command=$1
            shift
            app-"$command" "$@"
            exit 0
        ;;

        *)
            exit 1
        ;;

    esac
done

exit 1
