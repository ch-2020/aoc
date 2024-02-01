import argparse
import os, importlib
from global_ import globalvariables as gv

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", "-d", required=True, help="which day are you on?")
    parser.add_argument("--part", "-p", required= True, help="which part are you working on?")
    parser.add_argument("--mode", "-m", required= True, help="test (t) OR solution (s)")
    args = parser.parse_args()
    return args


def main(day, part, mode):
    script = f"day{day}p{part}"
    content = ""

    if mode == "t":
        content = open(f"inputs/testd{day}.txt").read()
    elif mode == "s":
        content = open(f"inputs/inputd{day}.txt").read()
    else: 
        print(f"Error when reading {content}")  

    gv.filecontent = content

    importlib.import_module(f'solutioncode.{script}')
    
if __name__ == "__main__":
    args = get_arguments()
    main(args.day, args.part, args.mode)