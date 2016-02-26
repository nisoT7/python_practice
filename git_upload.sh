#!/bin/sh
git add -A
if [ $# != 0 ]; then
    git commit -m "$1"
else
   git commit -m "date '+%Y_%m_%d_%H_%M_%S'"
fi

git push -u origin master
