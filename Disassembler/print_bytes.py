def print_bytes(number: int):
    if (number < 16):
        return ('0' + hex(number)[2:])
    else:
        return (hex(number)[2:])
