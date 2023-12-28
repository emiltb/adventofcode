from collections import deque
from typing import Any


data = [l.strip() for l in open("data/20.in")]

verbose = True


class Module:
    def __init__(self, name: str, targets: list[str]) -> None:
        self.name = name
        self.targets = targets

    def __repr__(self) -> str:
        return f"{type(self).__name__} -> {self.targets}"


class Broadcaster(Module):
    def __call__(self, src, signal: str) -> Any:
        for t in self.targets:
            if verbose:
                print(f"{self.name} -{signal}-> {t}")
            signal_queue.append((self.name, t, signal))
            # modules[t](self.name, signal)
            signals[signal] += 1


class Button(Module):
    def __call__(self, src=None, signal="low") -> Any:
        if verbose:
            print(f"Button -low-> Broadcaster")

        signal_queue.append((self.name, "broadcaster", "low"))
        # modules["broadcaster"]("low")
        signals["low"] += 1


# %
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
                for t in self.targets:
                    if verbose:
                        print(f"{self.name} -high-> {t}")
                    # modules[t](self.name, "high")
                    signal_queue.append((self.name, t, "high"))
                    signals["high"] += 1
            elif self.state == "on":
                self.state = "off"
                for t in self.targets:
                    if verbose:
                        print(f"{self.name} -low-> {t}")
                    # modules[t](self.name, "low")
                    signal_queue.append((self.name, t, "low"))
                    signals["low"] += 1


# &
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

        if all(v == "high" for v in self.last_input.values()):
            for t in self.targets:
                if verbose:
                    print(f"{self.name} -low-> {t}")
                # modules[t](self.name, "low")
                signal_queue.append((self.name, t, "low"))
                signals["low"] += 1
        else:
            for t in self.targets:
                if verbose:
                    print(f"{self.name} -high-> {t}")
                # modules[t](self.name, "high")
                signal_queue.append((self.name, t, "high"))
                signals["high"] += 1


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


signals = {"low": 0, "high": 0}
for _ in range(1000):
    signal_queue = deque([(None, "button", "low")])

    while signal_queue:
        src, target, signal = signal_queue.popleft()
        # print(src, target, signal)
        modules[target](src, signal)


print(signals["low"] * signals["high"])
