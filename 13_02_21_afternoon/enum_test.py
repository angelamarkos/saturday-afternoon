import enum
from enum import auto, unique

class Color(enum.IntEnum):
    RED = auto()
    WHITE = auto()
    BLUE = auto()

colors = Color

for name, member in colors.__members__.items():
    print(name, member.value, member.name)

color_1 = Color.RED
color_2 = Color.BLUE

print(color_2 != color_1)
print(color_2 > color_1)

permissions_dict = {'WRITE': 2, 'READ': 1}


@unique
class Permissions(enum.IntFlag):
    READ = 1
    WRITE = 2
    APPEND = 2

print(Permissions.__members__)
for name, member in Permissions.__members__.items():
    print(name, member.value)

permission = Permissions.READ | Permissions.WRITE
permission_2 = Permissions.READ ^ Permissions.WRITE
# permission_2 = permissions_dict['READ'] ^ permissions_dict['WRITE']

permission_3 = 2

print(permission_3 in permission)
print(permission_3 in permission_2)

class StatusCode(enum.IntEnum):
    BAD_REQUEST = 400
    NOT_FOUND = 404

import requests
response = requests.get('https://google.com')
if response.status_code == StatusCode.BAD_REQUEST:
    pass
elif response.status_code < StatusCode.BAD_REQUEST:
    pass