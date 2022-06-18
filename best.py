import sys
import process

if __name__ == '__main__':
    try:
        character = sys.argv[1]
        stats = sys.argv[2:]
        process.find_best_builds(character, stats)
    except IndexError:
        print("Please input a correct format ex: 'mario technique shoot'")
