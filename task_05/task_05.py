import string
import sys
from typing import List

def do_reaction(polymer: str) -> str:
    reaction: List[str] = []
    for unit in polymer:
        if reaction and unit.swapcase() == reaction[-1]:
            reaction.pop()
        else:
            reaction.append(unit)
    return ''.join(reaction)

def part_one(polymer: str) -> int:
    return len(do_reaction(polymer))

def part_two(polymer: str) -> int:
    phase_one = do_reaction(polymer)
    length = len(phase_one)
    for unit in string.ascii_lowercase:
        test_phase = phase_one.replace(unit, '').replace(unit.upper(), '')
        length = min(length, len(do_reaction(test_phase)))
    return length

def main() -> None:
    polymer: str = ''
    for line in sys.stdin:
        polymer += line[:-1]
    print('Part 1 =', part_one(polymer))
    print('Part 2 =', part_two(polymer))

if __name__ == "__main__":
    main()
