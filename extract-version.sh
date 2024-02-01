#!/bin/bash

filename="$1"

# Define the regex pattern
regex='VERSION = "(.*)"'

# Read the contents of the file
contents="$(cat $filename)"

# Check if the contents match the regex
if [[ $contents =~ $regex ]]; then
    # Print the matched version
    echo "${BASH_REMATCH[1]}"
else
    # Print an error message and exit with an error code
    echo "Couldn't find a match for ($regex) in $filename."
    exit 1
fi