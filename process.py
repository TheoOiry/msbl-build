import operator

from const.equipments import *
from const.base_stats import *

NUMBER_OF_POSSIBILITIES = 2400

EQUIPMENTS = [HEAD, ARMS, BODY, LEGS]

BAD_FORMAT_ERROR = "Bad format for needed stats please use the format '8/8/8/8/8'"


def number_to_build(n):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % 7))
        n //= 7
    for _ in range(4 - len(digits)):
        digits.append(0)
    return digits[::-1]


def compute_build(base_stats, build):
    equipments_stats = [EQUIPMENTS[i][val] for (i, val) in enumerate(build)]
    stats = base_stats
    for equipment_stats in equipments_stats:
        stats = list(map(operator.add, stats, equipment_stats))
    return stats


def parse_inputs(character, needed_stats):
    base_stats = BASE_STATS.get(character.lower())
    if base_stats is None:
        print(f"{character} is not a valid character")
        return
    needed_stats = needed_stats.strip().split('/')
    if len(needed_stats) != 5:
        print(BAD_FORMAT_ERROR)
    try:
        needed_stats = list(map(int, needed_stats))
    except ValueError:
        print(BAD_FORMAT_ERROR)

    return base_stats, needed_stats


def find_build(character, needed_stats):
    base_stats, needed_stats = parse_inputs(character, needed_stats)
    for i in range(NUMBER_OF_POSSIBILITIES):
        build = number_to_build(i)
        if compute_build(base_stats, build) == needed_stats:
            return build
    return None
