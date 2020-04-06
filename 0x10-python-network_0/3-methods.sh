#!/bin/bash
# display all the http methods
curl 0.0.0.0:5000/route_4 -sI | grep Allow: | cut -d":" -f2- | sed 's/^ *//'
