from encode_decode import *


if __name__ == '__main__':
    str_to_encode = input('Expression: ')
    print(b_encode(str_to_encode))
    print(b_decode(b_encode(str_to_encode)))
    str_to_dec = input('Expression to decode: ')
    validate_decode(str_to_dec)
