#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./fast_commit.bash 'commit message'"
    exit 1
fi

echo "Executing 'git add .'"
git add .

echo "Executing 'git commit -m \"$1\"'"
git commit -m "$1"

echo "Executing 'git push'"
git push
