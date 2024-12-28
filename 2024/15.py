from collections import deque
from abc import ABC, abstractmethod
from dataclasses import dataclass
grid, instructions = open('data/15.in').read().split('\n\n')
grid = grid.split()
rows = len(grid)
cols = len(grid[0])

grid = {(r,c): s for r, l in enumerate(grid) for c, s in enumerate(l)}
instructions = deque("".join(instructions.split()))
dirs = {'^': (-1,0), 'v': (1,0), '>': (0,1), '<': (0,-1)}
pos = [(r,c) for (r,c), s in grid.items() if s == "@"][0]

def push(r, c, dr, dc):
    next_pos = (r + dr, c + dc)
    if grid[next_pos] == 'O':
        push(*next_pos, dr, dc)
    if grid[next_pos] == '.':
        grid[next_pos] = 'O'
        grid[(r,c)] = '.'

while instructions:
    dr, dc = dirs[instructions.popleft()]
    r, c = pos
    next_pos = (r + dr, c + dc)

    if grid[next_pos] == 'O':
        push(*next_pos, dr, dc)

    if grid[next_pos] == '.':
        grid[next_pos] = '@'
        grid[pos] = '.'
        pos = next_pos

print(sum(r * 100 + c for (r, c), s in grid.items() if s == 'O'))

grid, instructions = open('data/15.in').read().split('\n\n')
grid = grid.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.').split()
rows = len(grid)
cols = len(grid[0])
grid = {(r,c): s for r, l in enumerate(grid) for c, s in enumerate(l)}
instructions = deque("".join(instructions.split()))

def can_move(block, dr, dc, res):
    if all(grid[(r+dr, c+dc)] == '.' for r, c in block):
        res += block
    
    for r, c in block:
        if grid[(r+dr, c + dc)] == ']':
            block_position = [(r + dr, c - 1), (r + dr, c)]
        elif grid[(r+dr, c + dc)] == '[':
            block_position = [(r + dr, c), (r + dr, c + 1)]
        elif grid[(r+dr, c + dc)] == '#':
            res += [False]
            break
        else:
            continue
    
        if can_move(block_position, dr, dc, res):
            res += block
    
    if not all(res):
        return False
    
    return set(res)

def push_horizontal(r, c, dr, dc):
    next_pos = (r + dr, c + dc)
    if grid[next_pos] in '[]':
        push_horizontal(*next_pos, dr, dc)
    if grid[next_pos] == '.':
        grid[next_pos] = grid[(r,c)]
        grid[(r,c)] = '.'

def push_vertical(r, c, dr, dc):
    next_pos = (r + dr, c + dc)
    if grid[(r,c)] == '[':
        block_position = [(r,c), (r, c + 1)]
    elif grid[(r,c)] == ']':
        block_position = [(r,c - 1), (r, c)]

    if blocks := can_move(block_position, dr, dc, []):
        for br, bc in sorted(blocks, reverse = dr > 0):
            next_pos = (br + dr, bc + dc)
            grid[next_pos] = grid[(br, bc)]
            grid[(br, bc)] = '.'

pos = [(r,c) for (r,c), s in grid.items() if s == "@"][0]
while instructions:
    ins = instructions.popleft()
    dr, dc = dirs[ins]
    r, c = pos
    next_pos = (r + dr, c + dc)

    if grid[next_pos] in '[]':
        if dr == 0:
            push_horizontal(*next_pos, dr, dc) 
        else:
            push_vertical(*next_pos, dr, dc)

    if grid[next_pos] == '.':
        grid[next_pos] = '@'
        grid[pos] = '.'
        pos = next_pos

print(sum(r * 100 + c for (r, c), s in grid.items() if s == '['))
