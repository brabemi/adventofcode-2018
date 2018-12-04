import collections
import sys

def part_one(ids):
    twos, threes = 0, 0

    for element in ids:
        cntr = collections.Counter(element)
        vals = set(cntr.values())
        if 2 in vals:
            twos += 1
        if 3 in vals:
            threes += 1

    return twos * threes

def part_two(ids):
    for i in range(len(ids)):
        first = ids[i]
        length = len(first)
        for second in ids[i+1:]:
            match = [first[i] != second[i] for i in range(length)]
            if sum(match) == 1:
                return ''.join([
                    first[i] if not match[i] else '' for i in range(length)
                ])

def main():
    ids = []
    for line in sys.stdin:
        ids.append(line[:-1])

    print('Part 1 =', part_one(ids))
    print('Part 2 =', part_two(ids))

if __name__ == "__main__":
    main()
