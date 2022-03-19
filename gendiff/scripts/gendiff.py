
from gendiff.formatters import renderers_map
from gendiff.cli import get_command_args
from gendiff.generator_diff import generate_diff


def main():
    args = get_command_args()

    dicts_diff = generate_diff(args.first_file, args.second_file)

    if args.format not in renderers_map.keys():
        raise Exception(f"Not implemented method for format: {args.format}")

    renderer = renderers_map[args.format]

    print(renderer(dicts_diff))


if __name__ == '__main__':
    main()
