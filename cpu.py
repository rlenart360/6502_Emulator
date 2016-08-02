class CPU(object):
    def __init__(self):
        # The CPU Registers:
        # The Accumulator, X Register, Y Register,
        # Status Register [S,V,_,B,D,I,Z,C], Program Counter, and Stack Pointer.
        
        self.A = 0
        self.X = 0
        self.Y = 0
        self.STATUS = [0,0,0,0,0,0,0,0]
        self.PC = 0
        self.SP = 0
        
        # TODO: Initialize memory.

    def process_instruction(self, instruction: bytes):
    		
        # TODO: process the instruction
        print(instruction)
        print(self.A)
