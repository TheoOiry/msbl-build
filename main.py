import process

if __name__ == '__main__':
    payload = input(">")
    try:
        character, needed_stats = payload.split()
        build = process.find_build(character, needed_stats)
        if build is not None:
            print(''.join(map(str, build)))
        else:
            print("This build is impossible")
    except ValueError:
        print("Please input a correct format ex: mario 9/16/16/6/16")
