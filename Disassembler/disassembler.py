class Disassembler(object):
    def __init__(self):
        pass

    def process_hex(self, rom_hex):
        print(rom_hex)

        i = 0
        while i < (len(rom_hex)):

            current_byte = rom_hex[i]

            # LSR (Logical Shift Right), MODE: Absolute, LENGTH: 3 bytes
            if (rom_hex[i] == 78):
                print('LSR ' + '$' + hex(rom_hex[i + 2])[2:] + hex(rom_hex[i + 1])[2:])
                i += 2

            # ORA (Bitwise OR with Accumulator), MODE: Indirect, X, LENGTH: 2 bytes
            elif (rom_hex[i] == 1):
                print('ORA ' +'($' +hex(rom_hex[i+1])[2:] + ',X)')
                i+=1

            # SEI (Set Interrupt), Processor Status Intruction
            elif (rom_hex[i] == 120):
                print('SEI')

            # CLD (Clear Decimal), Processor Status Intruction
            elif (rom_hex[i] == 216):
                print('CLD')

            # ADC (Add with Carry)
            elif (rom_hex[i] == 105):
                print('ADC '+'#$'+hex(rom_hex[i+1])[2:])
                i+=1

            # ADC
            elif (rom_hex[i] == 101):
                print('ADC '+'$'+hex(rom_hex[i+1])[2:])
                i+=1

            elif (rom_hex[i] == 117):
                print('ADC '+'$'+hex(rom_hex[i+1])[2:]+',X')
                i+=1

            elif (rom_hex[i] == 109):
                print('ADC '+'$'+hex(rom_hex[i+2])[2:]+hex(rom_hex[i+1])[2:])
                i+=2

            elif (rom_hex[i] == 125):
                print('ADC '+'$'+hex(rom_hex[i+2])[2:]+hex(rom_hex[i+1])[2:]+',X')
                i+=2

            elif (rom_hex[i] == 121):
                print('ADC ' + '$' + hex(rom_hex[i + 2])[2:] + hex(rom_hex[i + 1])[2:] + ',Y')
                i+=2

            elif (rom_hex[i] == 97):
                print('ADC ' + '($' + hex(rom_hex[i + 1])[2:] + ',X)')
                i+=1

            elif (rom_hex[i] == 113):
                print('ADC ' + '($' + hex(rom_hex[i + 1])[2:] + '),Y')
                i+=1

            i += 1
