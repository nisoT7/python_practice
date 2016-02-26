#!/bin/sh
git add -A
if [ $# != 0 ]; then
    git commit -m "$1"
else
    datetime= date + '+%Y_%m_%d_%H:%M:%S'
    git commit -m "$echo{datetime}"
fi

git push -u origin master
