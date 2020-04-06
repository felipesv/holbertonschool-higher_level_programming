#!/bin/bash
# get the content length in bytes
curl -s "$1" | wc -c
