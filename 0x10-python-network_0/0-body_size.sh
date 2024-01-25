#!/usr/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

if [ $# -ne 1 ]
then
    echo "USAGE ./program url"
    exit 1
fi

# get url
url=$1

# Use curl to send url and get the response header
response_header=$(curl -sI "$url")

# Extract content length header from the response
res_body_size=$(echo "$response_header" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

# print length of the http esponse body
echo "$res_body_size"

