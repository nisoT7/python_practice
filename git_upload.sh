#!/bin/sh
git add -A
if [ $# != 0 ]; then
    git commit -m "$1"
else
   datetime= date '+%Y_%m_%d-%H:%M:%S'
   git commit -m "datetime"
fi

git push -u origin master
