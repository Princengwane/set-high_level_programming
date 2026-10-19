#!/bin/bash
# Sends the contents of a file as a JSON POST request body.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
