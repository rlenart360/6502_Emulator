import argparse

from disassembler import Disassembler


def main():
    rom_parser = argparse.ArgumentParser(description='NES Disassembler')
    rom_parser.add_argument('rom_path', metavar='ROM', type=str, help='Path to NES ROM.')
    args = rom_parser.parse_args()

    print(args.rom_path)

    # Load the ROM
    with open(args.rom_path, 'rb') as rom:
        rom_hex = rom.read()

    # Create the Disassembler
    disassembler = Disassembler()
    disassembler.process_hex(rom_hex[32768:65536])

if __name__ == '__main__':
    main()
