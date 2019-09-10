import argparse
import os, sys


my_parser = argparse.ArgumentParser(prog='cli',                                     # Program name
                                    usage='%(prog)s [-h] [-v]',                     # Program usage
                                    description='List the content of a folder',     # Program description
                                    epilog='so what u gunna duh? :v',               # Program epilog, comes at the end
                                    prefix_chars='-',                               # Arguments prefix
                                    fromfile_prefix_chars='@',                      # Load arguments from file
                                    )


# Add the arguments

# my_parser.add_argument('Path', metavar='path', type=str, help='the path to list')

# my_parser.add_argument('a', help='a first argument')
# my_parser.add_argument('b', help='b second argument')
# my_parser.add_argument('c', help='c third argument')
# my_parser.add_argument('d', help='d fourth argument')
# my_parser.add_argument('e', help='e fifth argument')

my_parser.add_argument('-v', '--verbose', action='store_true', help='an optional argument',)
my_parser.add_argument('-i', '--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

# if not os.path.isdir(input_path):
#     print('The path specified does not exist')
#     sys.exit()

# print('\n'.join(os.listdir(input_path)))
