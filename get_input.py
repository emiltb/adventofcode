#!/usr/bin/env python
import os
import requests
import argparse

AOC_COOKIE = {"session": os.getenv("AOCCOOKIE")}

parser = argparse.ArgumentParser()
parser.add_argument("--year", type=int, default=2023)
parser.add_argument("--day", type=int, default=1)
parser.add_argument("--force", action=argparse.BooleanOptionalAction)
args = parser.parse_args()


input_path = f"{args.year}/data/{args.day}.in"
script_path = f"{args.year}/{args.day}.py"
if os.path.exists(input_path) and not args.force:
    print(f"Input for {args.year} day {args.day} already downloaded")
    exit(1)

headers = {"User-Agent": "github.com/emiltb/adventofcode by emilbp@gmail.com"}

data = requests.get(
    f"https://adventofcode.com/{args.year}/day/{args.day}/input",
    cookies=AOC_COOKIE,
    headers=headers,
)

print(data.request.headers)

with open(input_path, "w") as f:
    f.writelines(data.text)

if not os.path.exists(script_path):
    with open(script_path, "w") as f:
        f.writelines(f"data = [l.strip() for l in open('data/{args.day}.in')]\n\n")
