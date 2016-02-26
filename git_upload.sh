#!/bin/sh
git add -A

if [ $# != 0 ]; then
    git commit -m "$1"
else
    git commit -m \"${date}\"
fi

git push -u origin master
