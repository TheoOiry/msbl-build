import operator

from const.equipments import *
from const.base_stats import *

NUMBER_OF_POSSIBILITIES = 2400

EQUIPMENTS = [HEAD, ARMS, BODY, LEGS]

BAD_FORMAT_ERROR = "Bad format for needed stats please use the format '8/8/8/8/8'"


def number_to_build(n):
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


def base_stats_from(character):
    base_stats = BASE_STATS.get(character.lower())
    if base_stats is None:
        print(f"{character} is not a valid character")
        return None
    return base_stats


def parse_needed_stats(needed_stats):
    needed_stats = needed_stats.strip().split('/')
    if len(needed_stats) != 5:
        print(BAD_FORMAT_ERROR)
        return None
    try:
        return list(map(int, needed_stats))
    except ValueError:
        print(BAD_FORMAT_ERROR)


def builds():
    for i in range(NUMBER_OF_POSSIBILITIES + 1):
        yield number_to_build(i)


def build_to_str(build):
    return ''.join(map(str, build))


def stats_to_str(stats):
    return '/'.join(map(str, stats))


def find_build(character, needed_stats):
    base_stats = base_stats_from(character)
    needed_stats = parse_needed_stats(needed_stats)
    if base_stats is None or needed_stats is None:
        return None
    for build in builds():
        if compute_build(base_stats, build) == needed_stats:
            return build
    return None


def build_to_stats(character, build):
    base_stats = base_stats_from(character)
    try:
        return compute_build(base_stats, list(map(int, str(build))))
    except IndexError:
        print(f"{build} is not a valid build")
        return None


def find_builds_by_best_stats(base_stats, stats_index):
    valid_builds = []
    for build in builds():
        build_stats = compute_build(base_stats, build)
        important_stats = [build_stats[i] for i in stats_index]
        if sorted(important_stats) == important_stats:
            valid_builds.append((build, sum(important_stats)))

    if len(valid_builds) > 0:
        max_total = max([total for _, total in valid_builds])
        return [b for b, total in valid_builds if total == max_total]
    return []


def find_best_builds(character, stats):
    base_stats = base_stats_from(character)
    try:
        stats_index = [STATS_NAMES.index(s) for s in stats][::-1]
        best_builds = find_builds_by_best_stats(base_stats, stats_index)
        if len(best_builds) == 0:
            print("No build found")
        else:
            best_builds = [(build, compute_build(base_stats, build)) for build in best_builds]
            print('\n'.join([f'({build_to_str(build)}): {stats_to_str(stats)}' for build, stats in best_builds]))
    except ValueError:
        print(f"Bad stats names need to be in: {', '.join(STATS_NAMES)}")
