from collections import Counter
from itertools import product
import sys
from typing import List, NamedTuple


class Claim(NamedTuple):
    claim_id: int
    x: int
    y: int
    width: int
    height: int

def parse_line(line: str) -> Claim:
    # #1 @ 1,3: 4x4
    claim_id_str, rest = line.split(' @ ', 1)
    claim_id = int(claim_id_str[1:])
    coordinates, rest = rest.split(': ', 1)
    x, y = tuple(map(int, coordinates.split(',', 1)))
    width, height = tuple(map(int, rest.split('x', 1)))
    return Claim(claim_id=claim_id, x=x, y=y, width=width, height=height)

def claim_x_range(claim: Claim) -> range:
    return range(claim.x, claim.x + claim.width)

def claim_y_range(claim: Claim) -> range:
    return range(claim.y, claim.y + claim.height)

def claims_overlap(claim_a: Claim, claim_b: Claim) -> int:
    ax = claim_x_range(claim_a)
    ay = claim_y_range(claim_a)
    bx = claim_x_range(claim_b)
    by = claim_y_range(claim_b)
    x_overlap = len(set(ax).intersection(bx))
    y_overlap = len(set(ay).intersection(by))
    return x_overlap * y_overlap

def part_one(claims: List[Claim]) -> int:
    overlap: Counter = Counter()
    for claim in claims:
        x_range = claim_x_range(claim)
        y_range = claim_y_range(claim)
        cntr = Counter(product(x_range, y_range))
        overlap += cntr
    overlap_sum: int = 0
    for k in overlap:
        if overlap[k] > 1:
            overlap_sum += 1
    return overlap_sum

def part_two(claims: List[Claim]) -> int:
    for claim_a in claims:
        claim_area = claim_a.width * claim_a.height
        overlap = 0
        for claim_b in claims:
            overlap += claims_overlap(claim_a, claim_b)
            if overlap and overlap != claim_area:
                break
        if overlap == claim_area:
            return claim_a.claim_id
    return 0

def main() -> None:
    claims: List[Claim] = []
    for line in sys.stdin:
        claims.append(parse_line(line))
    print('Part 1 =', part_one(claims))
    print('Part 2 =', part_two(claims))

if __name__ == "__main__":
    main()
