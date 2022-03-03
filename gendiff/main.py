import argparse

from .gendiff import generate_diff


def main():

    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')

    parser.add_argument('-f', '--format',
                        help='set format of output', default='json')

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
