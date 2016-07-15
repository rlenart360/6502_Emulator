class Disassembler(object):
    def __init__(self):
        pass

    def process_hex(self, rom_hex: int):
        print(rom_hex)

        for i in range(len(rom_hex)):
            print(i)
            current_byte = rom_hex[i]

            # LSR (Logical Shift Right), Length 3 bytes
            if (rom_hex[i] == 78):
                print('LSR '+'$'+hex(rom_hex[i+2])[2:]+hex(rom_hex[i+1])[2:])
                i+=2
                print(i)


