#!/bin/bash
: <<'COMMENT'
Script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
COMMENT

response=$(curl -sX POST --data-binary "@$2" "$1")

echo "$response"
