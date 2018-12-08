import sys
from typing import Counter, Dict, List


class Sleep:
    def __init__(self) -> None:
        self.duration: int = 0
        self.minutes: Counter[int] = Counter({0:0})

    def add_sleep(self, start: int, end: int) -> None:
        self.duration += end - start
        self.minutes.update(range(start, end))

def make_sleep_stats(logs: List[str]) -> Dict[int, Sleep]:
    sorted_logs: List[str] = sorted(logs)
    guards: Dict[int, Sleep] = {}
    guard_id = 0
    sleep_start = 0
    for log in sorted_logs:
        if log.endswith(' begins shift\n'):
            guard_id = int(log.split('#', 1)[1].split(' ', 1)[0])
            if guard_id not in guards:
                guards[guard_id] = Sleep()
        elif log.endswith(' falls asleep\n'):
            sleep_start = int(log[15:17])
        elif log.endswith(' wakes up\n'):
            guards[guard_id].add_sleep(sleep_start, int(log[15:17]))
    return guards

def part_one(guards: Dict[int, Sleep]) -> int:
    guard = max(guards.items(), key=lambda x: x[1].duration)
    return guard[0] * guard[1].minutes.most_common(1)[0][0]

def part_two(guards: Dict[int, Sleep]) -> int:
    guard = max(guards.items(), key=lambda x: x[1].minutes.most_common(1)[0][1])
    return guard[0] * guard[1].minutes.most_common(1)[0][0]

def main() -> None:
    logs: List[str] = []
    for line in sys.stdin:
        logs.append(line)
    guards = make_sleep_stats(logs)
    print('Part 1 =', part_one(guards))
    print('Part 2 =', part_two(guards))

if __name__ == "__main__":
    main()
