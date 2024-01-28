#!/bin/bash
# Script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sXH POST "Content-Type: application/json" --data-binary "@'$2'" "$1"
