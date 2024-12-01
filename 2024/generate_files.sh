#!/bin/bash

if [ -z "$1" ]; then
    read -p "Enter the aoc day as filename (without extension): " pythonFileName
else
    pythonFileName="$1"
fi

# Generate python scripts
mkdir -p solutioncode
pythonFilePathP1="solutioncode/day${pythonFileName}p1.py"
pythonFilePathP2="solutioncode/day${pythonFileName}p2.py"

if [ ! -e "$pythonFilePathP1" ]; then
    touch "$pythonFilePathP1" 
    echo "from global_ import globalvariables as gv" >> "$pythonFilePathP1"
    echo "f = gv.filecontent" >> "$pythonFilePathP1"
    echo "Python files created: $pythonFilePathP1"
else
    echo "$pythonFilePathP1 file already exists. Skipping request."
fi

if [ ! -e "$pythonFilePathP2" ]; then
    touch "$pythonFilePathP2"
    echo "from global_ import globalvariables as gv" >> "$pythonFilePathP2" 
    echo "f = gv.filecontent" >> "$pythonFilePathP2"
    echo "Python files created: $pythonFilePathP2"
else
    echo "$pythonFilePathP2 file already exists. Skipping request."
fi

# Generate input file
mkdir -p inputs
inputFilePath="inputs/inputd${pythonFileName}.txt"
testFilePath="inputs/testd${pythonFileName}.txt"
touch "$inputFilePath"
touch "$testFilePath"
echo "Input and test files created: $inputFilePath and $testFilePath"

# automatically download input --> not done, failed with cookie
#set AOC_COOKIE="62842729%3A3YFSRo1dJv2OWtsi5kunGGjipL_UAl-ZtRWbXl4DniXd8kf4" 
#curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/2022/day/$1/input > "$textFilePath"