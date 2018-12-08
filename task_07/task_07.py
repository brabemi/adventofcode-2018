import copy
import sys
from typing import List, Dict, Tuple, Set

from pprint import pprint

def parse_line(line: str) -> Tuple[str, str]:
    ancestor = line[5]
    successor = line[36]
    return ancestor, successor

def graph_reduce(ancs: Dict[str, Set[str]], sucs: Dict[str, Set[str]]) -> str:
    ancsk = set(ancs.keys())
    sucsk = set(sucs.keys())
    adepts = list(sucsk - ancsk)
    if not adepts:
        return ''.join(sorted(ancsk))
    adept = sorted(adepts)[0]
    for suc in sucs[adept]:
        ancs[suc].remove(adept)
        if len(ancs[suc]) == 0 and suc in sucsk:
            ancs.pop(suc, None)
    sucs.pop(adept, None)
    return adept + graph_reduce(ancs, sucs)

def part_one(ancestors: Dict[str, Set[str]], successors: Dict[str, Set[str]]) -> str:
    ancs = copy.deepcopy(ancestors)
    sucs = copy.deepcopy(successors)
    return graph_reduce(ancs, sucs)

def main() -> None:
    ancestors: Dict[str, Set[str]] = {}
    successors: Dict[str, Set[str]] = {}
    for line in sys.stdin:
        anc, suc = parse_line(line)

        if anc not in successors:
            successors[anc] = set()
        successors[anc].add(suc)
        if suc not in ancestors:
            ancestors[suc] = set()
        ancestors[suc].add(anc)

    print('Part 1 =', part_one(ancestors, successors))

if __name__ == "__main__":
    main()
