#!/bin/bash
#script takes URL as argument, sends a GET request to the URL, displays the body of the response
curl -sX GET -H "X-School-User-Id: 98" "$1"
