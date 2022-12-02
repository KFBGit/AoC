#!/bin/bash

i=1

for line in ../input/calories.input
do
	if $line==""
	then
		i=$((i+1))
	else
		echo ""
	fi
done
