#!/bin/bash
# request POST in json
curl "$1" -sX POST -H "Content-Type: application/json" -d "$(cat "$2")"
