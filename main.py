import argparse
from cpu import CPU


def main():
    rom_parser = argparse.ArgumentParser(description='NES Emulator')
    rom_parser.add_argument('rom_path', metavar='ROM', type=str, help='Path to NES ROM.')
    args = rom_parser.parse_args()

    # TODO: Validate ROM path is correct
    print(args.rom_path)

    # Load the ROM
    with open(args.rom_path, 'rb') as rom:
        lines = rom.readlines()

    # Create the CPU
    cpu = CPU()
    cpu.process_instruction(lines[0][0:2])


#this is a test

if __name__ == '__main__':
    main()
