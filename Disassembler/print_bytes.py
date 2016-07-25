def print_bytes(number: int):
    if (number < 16):
        print('0' + hex(number)[2:])
    else:
        print(hex(number)[2:])
