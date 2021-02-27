import argparse
import os
import pwd
import grp
import stat
from datetime import datetime

parser = argparse.ArgumentParser('myls', description='Custom implementation for ls', conflict_handler='resolve')

parser.add_argument('paths', default=['.'], nargs='*', help='Path for dircetory')

parser.add_argument('-l', action='store_true', help='extra info')

parser.add_argument('-h', '--human-readable', action='store_true', help='info', dest='hr')

args = parser.parse_args()

len_paths = len(args.paths)

for path in args.paths:
    if len_paths > 1:
        print(path)
    _, file_names, folder_names = next(os.walk(path))

    files_names = file_names + folder_names

    if args.l:
        for file_name in files_names:
            row = []
            stat_info = os.stat(file_name)
            row.append(stat.filemode(stat_info.st_mode))
            row.append(stat_info.st_nlink)
            row.append(pwd.getpwuid(stat_info.st_uid).pw_name)
            row.append(grp.getgrgid(stat_info.st_gid).gr_name)
            if args.hr:
                row.append(f'{round(stat_info.st_size / 1024, 1)}K')
            else:
                row.append(stat_info.st_size)
            row.append(datetime.fromtimestamp(stat_info.st_mtime).strftime("%b %d %H:%M"))
            row.append(file_name)
            formatting = '{: <2} ' * len(row)
            print(formatting.format(*row))
    else:
        print(*files_names, sep='  ')

