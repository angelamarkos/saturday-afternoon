def validate_decode(str_to_decode):
    print(str_to_decode)
    print(len(str_to_decode))
    if len(str_to_decode) % 8:
        raise Exception('length of decoding string should devided by 8')
    if set(str_to_decode) > {'1', '0'}:
        raise Exception('String to decode should contains only 1 or 0')