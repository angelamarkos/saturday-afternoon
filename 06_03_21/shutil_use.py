import shutil
import os
import stat
# 1. copy
# with open('original.txt', 'w') as file:
#     file.write('Text to copy')

# f = open('original.txt', 'r')
# copy = open('text.py', 'w')

# os.mkdir('copies/copies2')
# shutil.copy2('original.txt', 'copies/copies2/original.txt')
# shutil.copyfileobj(f, copy)

# f.close()
# copy.close()

# print(os.stat('original.txt'))
# print(os.stat('./copies/original.txt'))
# print(os.stat('./copies/copies2/original.txt'))

# os.remove('text.py')
# shutil.move('copies/text.py', '.')

# shutil.rmtree('copies')

# shutil.make_archive('./archived', 'tar', 'to_be_archived')

# shutil.unpack_archive('archived.tar', 'new_dir')

print(os.stat('original.txt').st_mode)
os.chmod('text.py', stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)

# shutil.copymode('text.py', 'original.txt')
# shutil.copytree('new_dir', 'copy_new_dir')

