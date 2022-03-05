import argparse

from .gendiff import generate_diff

from gendiff.renderers.json.json import render as render_json


def main():
    renderers_map = {
        'json': render_json
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
