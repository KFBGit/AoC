#!/bin/bash

calcTotalCalsPerElf() {
	local totalCaloriesPerElf=() caloriesOfElf=0

	cat $1 | while read line
	do
	#	echo "working on: $line"
		[[ $line == "" ]] && totalCaloriesPerElf+=("$caloriesOfElf") && caloriesOfElf=0 && continue
		echo "${totalCaloriesPerElf[@]}"
	#	echo "adding line to tempvar: $line"
		((caloriesOfElf+=line))
	#	echo $caloriesOfElf
	#	if [[ $caloriesOfElf == 54911 ]]; then
	#		echo "found the culprit..."
	#	fi

	done
	totalCaloriesPerElf+=("$caloriesOfElf")
	echo "${totalCaloriesPerElf[@]}"
}

calcTotalCalsPerElf "$1"
