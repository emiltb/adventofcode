from collections import deque
from functools import reduce

data = [l.strip() for l in open("data/20.in")]


class Module:
    def __init__(self, name: str, targets: list[str]) -> None:
        self.name = name
        self.targets = targets

    def __repr__(self) -> str:
        return f"{type(self).__name__} -> {self.targets}"

    def __call__(self, src, signal: str) -> None:
        for t in self.targets:
            signal_queue.append((self.name, t, signal))
            signals[signal] += 1


class Broadcaster(Module):
    pass


class Button(Module):
    pass


class FlipFlop(Module):
    def __init__(self, name: str, targets: list[str]) -> None:
        super().__init__(name, targets)
        self.state = "off"

    def __call__(self, src, signal) -> None:
        if signal == "high":
            pass
        elif signal == "low":
            if self.state == "off":
                self.state = "on"
                new_signal = "high"
            elif self.state == "on":
                self.state = "off"
                new_signal = "low"

            super().__call__(self.name, new_signal)


class Conjunction(Module):
    def __init__(self, name: str, targets: list[str]) -> None:
        super().__init__(name, targets)
        self.last_input = dict()

    def register_input(self, name: str):
        self.last_input[name] = "low"

    def __repr__(self) -> str:
        return f"{self.last_input} -> {type(self).__name__} -> {self.targets}"

    def __call__(self, src, signal) -> None:
        self.last_input[src] = signal
        new_signal = "low" if all(v == "high" for v in self.last_input.values()) else "high"  # fmt: skip
        super().__call__(self.name, new_signal)


class Output(Module):
    def __call__(self, src, signal):
        pass


modules = dict()
for d in data:
    name, targets = [s.strip() for s in d.split("->")]
    targets = [t.strip() for t in targets.split(",")]
    if name == "broadcaster":
        modules[name] = Broadcaster(name, targets)
    elif name[0] == "%":
        modules[name[1:]] = FlipFlop(name[1:], targets)
    elif name[0] == "&":
        modules[name[1:]] = Conjunction(name[1:], targets)

for k, m in dict(modules).items():
    for t in m.targets:
        if t not in modules.keys():
            modules[t] = Output(t, [])
        if isinstance(modules[t], Conjunction):
            modules[t].register_input(k)

modules["button"] = Button("button", ["broadcaster"])

verbose = False
signals = {"low": 0, "high": 0}
i = 1
state = {s: 0 for s in [m.last_input for k, m in modules.items() if "rx" in m.targets][0].keys()}  # fmt: skip
while any(v == 0 for v in state.values()):
    signal_queue = deque([(None, "button", "low")])

    while signal_queue:
        src, target, signal = signal_queue.popleft()
        modules[target](src, signal)
        if target == "rs" and signal == "high":
            state[src] = i
    if i == 1000:
        print(signals["low"] * signals["high"])
    i += 1

print(reduce(lambda x, y: x * y, [s for s in state.values()]))


# For showing the modules and connections in graphviz
# for k, m in modules.items():
#     for t in m.targets:
#         print(f"{k} -> {t}")

#     if isinstance(m, Output):
#         print(f"{k} [shape=star]")

#     if isinstance(m, Conjunction):
#         print(f"{k} [shape=invtriangle]")

#     if isinstance(m, Button) or isinstance(m, Broadcaster):
#         print(f"{k} [shape=diamond]")

#     if isinstance(m, FlipFlop):
#         print(f"{k} [shape=parallelogram]")
