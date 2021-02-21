def b_encode(str_to_encode):
    return ''.join('{:08b}'.format(ord(it)) for it in str_to_encode)

def b_decode(str_to_decode):
    return ''.join(chr(int(str_to_decode[i:i+8], 2)) for i in range(0, len(str_to_decode), 8))


