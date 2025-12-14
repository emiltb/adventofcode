*shapes, configs = open('data/12.in').read().split('\n\n')

def parse_shape(s):
    _, *s = s.strip().split()
    return [(r,c) for r, row in enumerate(s) for c, col in enumerate(row) if col == '#']
shapes = [parse_shape(s) for s in shapes]

def rotate_shape(s, n):
    s = list(s)
    def rotate(s):
        new_shape = []
        if (0,0) in s:
            new_shape.append((0,2))
        if (0,1) in s:
            new_shape.append((1,2))
        if (0,2) in s:
            new_shape.append((2,2))
        if (1,0) in s:
            new_shape.append((0,1))
        if (1,1) in s:
            new_shape.append((1,1))
        if (1,2) in s:
            new_shape.append((2,1))
        if (2,0) in s:
            new_shape.append((0,0))
        if (2,1) in s:
            new_shape.append((1,0))
        if (2,2) in s:
            new_shape.append((2,0))
        return sorted(new_shape)
    
    for _ in range(n):
        s = rotate(s)
    return s

def flip_vertical(s):
    new_shape = []
    if (0,0) in s:
        new_shape.append((2,0))
    if (0,1) in s:
        new_shape.append((2,1))
    if (0,2) in s:
        new_shape.append((2,2))
    if (1,0) in s:
        new_shape.append((1,0))
    if (1,1) in s:
        new_shape.append((1,1))
    if (1,2) in s:
        new_shape.append((1,2))
    if (2,0) in s:
        new_shape.append((0,0))
    if (2,1) in s:
        new_shape.append((0,1))
    if (2,2) in s:
        new_shape.append((0,2))
    return sorted(new_shape)    

def flip_horizontal(s):
    new_shape = []
    if (0,0) in s:
        new_shape.append((0,2))
    if (0,1) in s:
        new_shape.append((0,1))
    if (0,2) in s:
        new_shape.append((0,0))
    if (1,0) in s:
        new_shape.append((1,2))
    if (1,1) in s:
        new_shape.append((1,1))
    if (1,2) in s:
        new_shape.append((1,0))
    if (2,0) in s:
        new_shape.append((2,2))
    if (2,1) in s:
        new_shape.append((2,1))
    if (2,2) in s:
        new_shape.append((2,0))
    return sorted(new_shape)

def mutate(s, n):
    if n == 4:
        return flip_vertical(s)
    if n == 5:
        return flip_horizontal(s)
    else:
        return rotate_shape(s, n)

def print_area(area, fill, shape):
    for r in range(area[0]):
        for c in range(area[1]):
            if fill[(r,c)] == 1 and (r,c) in shape:
                print('X', end = '')
            elif fill[(r,c)] == 1:
                print('#', end = '')
            elif (r,c) in shape:
                print('*', end = '')
            else:
                print('.', end = '')
        print()
    print()

# current_shape = shapes[4]
# for offset in range(16):
#     offset_r = offset // 4
#     offset_c = offset % 4
#     print(offset_r, offset_c)
#     for n in range(4):
#         current_shape = [(s[0] + offset_r, s[1] + offset_c) for s in rotate_shape(shapes[4], n)]
#         print_area((4,4), current_shape)
#     print()

P1 = 0
for c in configs.strip().split('\n'):
    area, *presents = c.split()
    area = [int(n) for n in area.replace(':','').split('x')]
    presents = {idx: int(n) for idx, n in enumerate(presents) if n != '0'}

    print(area, presents)
    if area[0]*area[1] < sum(v*len(shapes[k]) for k, v in presents.items()):
        print('No chance of fitting')
        continue

    P1 += 1
    continue
    filled_area = {(r, c): 0 for r in range(area[0]) for c in range(area[1])}
    # print(filled_area)

    can_be_completed = True

    offset = 0
    mutations = 0

    for k, v in presents.items():
        for _ in range(v):
            # print({s for s in shapes[k]})
            while True:
                offset_r = offset // area[0]
                offset_c = offset % area[1]
                # print(offset_r, offset_c)
                current_shape = [(s[0] + offset_r, s[1] + offset_c) for s in mutate(shapes[k], mutations)]
                # print_area(area, filled_area, current_shape)

                # print('Current_shape:', current_shape)
                if (offset_r, offset_c) not in filled_area.keys():
                    print("No room in area")
                    can_be_completed = False
                    break
                elif not any(s in {k: v for k, v in filled_area.items() if v == 1} for s in current_shape) and all(s in filled_area.keys() for s in current_shape):
                    for s in current_shape:
                        filled_area[s] = 1
                    break

                if mutations in (0,1,2,3,4):
                    mutations += 1
                else:
                    mutations = 0
                    offset += 1

                if not can_be_completed:
                    break

        if not can_be_completed:
            P1 -= 1
            print()
            break


print(P1)




