import argparse


def get_command_args():
    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')

    parser.add_argument('-f', '--format',
                        help='set format of output', default='stylish')

    return parser.parse_args()
