from itertools import combinations

def solution(numbers):
    return sorted(set(sum(c) for c in combinations(numbers, 2)))