import sys
import process


def find_build(character, needed_stats):
    build = process.find_build(character, needed_stats)
    if build is not None:
        print(''.join(map(str, build)))
    else:
        print("This build is impossible")


if __name__ == '__main__':
    try:
        character, stats = sys.argv[1:]
        find_build(character, stats)
    except ValueError:
        print("Please input a correct format ex: 'mario 9/16/16/6/16'")
