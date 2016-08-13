import argparse
from tkinter import *
from tkinter import filedialog
from cpu import CPU


def main():
    rom_parser = argparse.ArgumentParser(description='NES Emulator')
    rom_parser.add_argument('rom_path', metavar='ROM', type=str, help='Path to NES ROM.')
    args = rom_parser.parse_args()

    # TODO: Validate ROM path is correct
    print(args.rom_path)

    # Load the ROM
    with open(args.rom_path, 'rb') as rom:
        instructions = rom.read()
        
    # TEST INSTRUCTIONS
    test = [117, 0]
    
    # Create the CPU
    cpu = CPU()
    cpu.process_instruction(test)
    print(cpu.A)
    
    root = Tk()
    frame = Frame(root, height = 532, width = 532)
    frame.pack()
    
    screen = Canvas(frame, bg = "black")
    screen.pack()
    screen.place(x =10 , y =10 , height = 512, width = 512)
    screen.create_rectangle(0, 0, 16, 16, fill='red')

    root.mainloop()


if __name__ == '__main__':
    main()
