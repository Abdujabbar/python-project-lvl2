from gendiff.cli import get_command_args
from gendiff.generator_diff import generate_diff


def main():
    args = get_command_args()

    output = generate_diff(args.first_file, args.second_file, args.format)

    print(output)


if __name__ == '__main__':
    main()
