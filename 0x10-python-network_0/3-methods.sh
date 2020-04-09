#!/bin/bash
# display all the http methods
curl "$1" -sI | grep Allow: | cut -d":" -f2- | sed 's/^ *//'
