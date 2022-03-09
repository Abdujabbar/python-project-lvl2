import argparse

from ..gendiff import generate_diff

from gendiff.formatters.stylish import render as stylish_renderer
from gendiff.formatters.plain import render as plain_renderer


def main():
    renderers_map = {
        'stylish': stylish_renderer,
        'json': '',
        'plain': plain_renderer
    }

    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')

    parser.add_argument('-f', '--format',
                        help='set format of output', default='json')

    args = parser.parse_args()

    output = generate_diff(
        args.first_file, args.second_file, renderers_map[args.format])

    print(output)


if __name__ == '__main__':
    main()
