import sys
import os
def convert_to_string(permissions, is_directory=False):
    p_list = ['r', 'w', 'e']
    directory_pref = 'd' if is_directory else '-'
    converted_permissions = ''
    while permissions:
        print(permissions)
        permission = permissions % 10
        permissions = permissions // 10
        bin_permission = bin(permission)[2:]
        str_permission = ''
        for i, value in enumerate(bin_permission):
            if value == '0':
                str_permission = f'{str_permission}-'
            else:
                str_permission = f'{str_permission}{p_list[i]}'

        converted_permissions = f'{str_permission}{converted_permissions}'
    return f'{directory_pref}{converted_permissions}'

if __name__ == '__main__':
    print(convert_to_string(755))
    args = sys.argv[1:]
    paths = []
    tags = []
    for arg in args:
        if arg.startswith('-'):
            tags.append(arg)
        else:
            paths.append(arg)

    for path in paths:
        print(f'{path}:')
        _, file_list, dir_list = next(os.walk(path))

        permission_files = lambda file_name: convert_to_string(int(oct(os.stat(f'{path}/{file_name}').st_mode)[-3:]))
        permission_dir = lambda file_name: convert_to_string(int(oct(os.stat(f'{path}/{file_name}').st_mode)[-3:]), True)
        print(*list(zip(map(permission_files, file_list), file_list)), sep='\n')
        print(*list(zip(map(permission_files, dir_list), dir_list)), sep='\n')




