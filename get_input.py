#!/usr/bin/python3
import os
import requests
import argparse

AOC_COOKIE = {"session": os.getenv("AOCCOOKIE")}

parser = argparse.ArgumentParser()
parser.add_argument("--year", type=int, default=2022)
parser.add_argument("--day", type=int, default=1)
args = parser.parse_args()


input_path = f"{args.year}/data/{args.day}.in"
if os.path.exists(input_path):
    print(f"Input for {args.year} day {args.day} already downloaded")
    exit(1)

data = requests.get(
    f"https://adventofcode.com/{args.year}/day/{args.day}/input", cookies=AOC_COOKIE
)
with open(input_path, "w") as f:
    f.writelines(data.text)
