import process


def find_build(character, needed_stats):
    build = process.find_build(character, needed_stats)
    if build is not None:
        print(''.join(map(str, build)))
    else:
        print("This build is impossible")


def build_to_stats(character, build):
    stats = process.build_to_stats(character, build)
    if stats is not None:
        print('/'.join(map(str, stats)))


def main():
    payload = input(">")
    try:
        character, params = payload.split()
        if '/' in params:
            find_build(character, params)
        else:
            build_to_stats(character, params)
    except ValueError:
        print("Please input a correct format ex: 'mario 9/16/16/6/16' or 'mario 5431'")


if __name__ == '__main__':
    main()
