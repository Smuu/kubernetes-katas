#!/bin/sh

cd $(dirname "$0")

group=$1

if [ -z $group ]; then
    echo Please give group parameter
    exit 1
fi

versions="v0.0.1 v0.0.2 v1.0.0 v1.0.1"

for v in $versions; do
    docker build --pull --build-arg VERSION=$v -t $group/troubleshooting-app:$v .
    docker push $group/troubleshooting-app:$v
done
