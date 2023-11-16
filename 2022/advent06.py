def slider(obj, w):
    window = obj[:w]
    yield window

    for s in obj[w:]:
        window = window[1:] + s
        yield window

def find_code(data, width):
    objslider = slider(data, width)

    for i, code in enumerate(objslider):
        if len(set(code)) == len(code):
            break
    return i + width, code

with open("inputs/input06.txt", "r") as f:
    data = f.read()

# Part 1
first_marker, code = find_code(data, 4)
print("First marker at", first_marker, code)

# Part 2
first_message, code = find_code(data, 14)
print("First message at", first_message, code)
