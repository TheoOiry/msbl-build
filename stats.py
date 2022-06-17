import sys
import process


def build_to_stats(character, build):
    stats = process.build_to_stats(character, build)
    if stats is not None:
        print('/'.join(map(str, stats)))


if __name__ == '__main__':
    try:
        character, params = sys.argv[1:]
        build_to_stats(character, params)
    except ValueError:
        print("Please input a correct format ex: 'mario 5431'")
