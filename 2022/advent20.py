data = [
    {"n": int(f), "sorted": False} for f in open("inputs/input20.txt").read().split()
]

while any([~el["sorted"] for el in data]):
    for i, el in enumerate(data):
        if el["sorted"] == False:
            print(i, el)
            item = data.pop(i)
            item["sorted"] = True
            data.insert(i + item["n"], item)
        break
