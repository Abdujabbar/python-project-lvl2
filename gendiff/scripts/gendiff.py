import argparse


def main():

    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', metavar='first_file', type=str, nargs=1)
    parser.add_argument('second_file', metavar='second_file', type=str, nargs=1)

    args = parser.parse_args()

    print(args)


if __name__ == '__main__':
    main()
