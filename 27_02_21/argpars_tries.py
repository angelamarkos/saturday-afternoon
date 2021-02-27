import argparse

parser = argparse.ArgumentParser(prog='MyParser',
                                 description='Description for my command',
                                 epilog='End of argpars help.',
                                 usage='%(prog)s [options]',
                                 prefix_chars='+/-')
# parser.add_argument('first_num', type=int, help='first number to add')
# parser.add_argument('second_num', type=int, help='second number to add')
# parser.add_argument('second_str', type=str, help='second number to add')
parser.add_argument('+num', type=float, help='float to add')
parser.add_argument('-n', '--name', type=float, help='float to ')
parser.add_argument('-v', '--verbose', nargs='?', help='float to ')
parser.add_argument('-t', action='store_false', help='float to ')
parser.add_argument('-q', action='store_const', const=1, default=0, help='float to ')
parser.add_argument('-q_1', nargs='?', const=1, default=0, help='float to ')
parser.add_argument('-z', action='append', help='float to ', dest='zk')
parser.add_argument('-k', action='append', help='float to ', dest='zk')
parser.add_argument('-p', action='append_const', const=1, help='float to ', dest='pe')
parser.add_argument('-e', action='append_const', const=2, help='float to ', dest='pe')


group = parser.add_mutually_exclusive_group()
group.add_argument('-o', nargs='*', default=[1], help='float to ')
group.add_argument('-w', nargs='+', default=[1], help='float to ')
args = parser.parse_args()

# print(f'{args.first_num} {args.second_str}')
print(args.__dict__)
print(args.num)

# =======================================================


parent_parser = argparse.ArgumentParser(description='Parent parser', add_help=False)
parent_parser.add_argument('path', help='path to file')

parser_1 = argparse.ArgumentParser(description='Parser 1', parents=[parent_parser])
parser_1.add_argument('-l', '--list', help='Text for -l')

parser_2 = argparse.ArgumentParser(description='Parser 2', parents=[parent_parser])
parser_2.add_argument('-a', '--add', help='Text for -a')

args_1 = parser_1.parse_args(['/path/to/file', '-l', '1'])
args_2 = parser_2.parse_args(['/path/to/file_2', '-l', '1'])

print(args_1.__dict__)
print(args_2.__dict__)



