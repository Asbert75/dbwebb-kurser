#!/bin/bash

SCRIPT=$( basename "$0" )

PORT="1337"
SERVER="localhost"

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
"  hello"
"  html"
"  status"
"  sum [value1] [value2] [valueN]"
"  filter [value1] [value2] [valueN]"
"  404"
"  all"
""
"Options:"
"  --help, -h     Print help."
    )

    printf "%s\n" "${usageTxt[@]}"
}

function app-hello
{
    curl -s "$ADDRESS/"
}

function app-html
{
    curl -s "$ADDRESS/index.html"
}

function app-status
{
    curl -s "$ADDRESS/status"
}

function app-sum
{
    QUERY=""
    for x in "$@"
    do
    QUERY+="$x&"
    done

    curl -s "$ADDRESS/sum?$QUERY"
}

function app-filter
{
    QUERY=""
    for x in "$@"
    do
    QUERY+="$x+&"
    done

    curl -s "$ADDRESS/filter?$QUERY"
}

function app-404
{
    curl -s "$ADDRESS/invalidRoute"
    echo ""
    curl -Is "$ADDRESS/invalidRoute"
}

function app-all
{
    echo " "
    echo "Running command: ./client.bash hello"
    app-hello "$@"

    echo " "
    echo "Running command: ./client.bash html"
    app-html "$@"

    echo " "
    echo "Running command: ./client.bash status"
    app-status "$@"

    echo " "
    echo "Running command: ./client.bash sum"
    app-sum "$@"

    echo " "
    echo "Running command: ./client.bash filter"
    app-filter "$@"

    echo " "
    echo "Running command: ./client.bash 404"
    app-404 "$@"
}




# Process options
while (( $# ))
do
    case "$1" in

        --help | -h)
            usage
            exit 0
        ;;

        hello         \
        | html       \
        | status       \
        | sum       \
        | filter       \
        | 404       \
        | all)
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
