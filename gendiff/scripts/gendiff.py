import argparse

from gendiff.generate_diff_impl import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')

    parser.add_argument('-f', '--format',
                        help='set format of output', default='stylish')

    args = parser.parse_args()

    output = generate_diff(
        args.first_file, args.second_file, args.format)

    print(output)


if __name__ == '__main__':
    main()
