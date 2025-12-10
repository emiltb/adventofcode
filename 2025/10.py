from heapq import heappop, heappush
data = [l.strip().split() for l in open('data/10.test.in')]

P1 = 0
for d in data:
    lights, *buttons, _ = d
    lights = int(lights[1:-1][::-1].replace('.','0').replace('#','1'), base=2)
    buttons = [{eval(l)} for l in buttons]

    q = [(0, 0b0, b) for b in buttons]
    
    while q:
        presses, state, button = heappop(q)
     

        for b in button:
            if isinstance(b, int):
                state ^= 1 << b
            else:
                for n in b:
                    state ^= 1 << n
        
        if state == lights:
            P1 += presses + 1
            break

        for b in buttons:
            next_node = (presses + 1, state, b)
            heappush(q, next_node)

print(P1)

# P2 = 0
# for d in data:
#     _, *buttons, joltage = d
#     buttons = [{eval(l)} for l in buttons]
#     joltage = eval(joltage.replace('{','[').replace('}',']'))

#     state = [0] * len(joltage)

#     q = [(0, state, b) for b in buttons]

#     print(state)

#     while True:
#         print(buttons)
#     # while q:
#     #     presses, state, button = heappop(q)
#     #     state = list(state)
#     #     print(presses, state, button)
     

#     #     for b in button:
#     #         if isinstance(b, int):
#     #             b = [b]
#     #         for n in b:
#     #             state[n] += 1
#     #             print(f'Pressed {n}. State {state}.')
        
#     #     if state == joltage:
#     #         P2 += presses + 1
#     #         print(P2)
#     #         break

#     #     # for s, j in zip(state, joltage):
#     #     #     if s > j:
#     #     #         break

#     #     # if presses > 11:
#     #     #     break

#     #     # for b in buttons:
#     #     #     next_node = (presses + 1, state, b)
#     #     #     # print("Next node: ", next_node)
#     #     #     heappush(q, next_node)

#     break