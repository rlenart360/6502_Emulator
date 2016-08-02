# TODO: Make a function that will call an error for invalid instructions.

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
        
        self.memory = []
        for i in range(65536):
        	self.memory.append(0)

    def process_instruction(self, rom_hex: bytes):
    		
        # TODO: process the instruction
        i = 0
        while i < len(rom_hex):
        	
        	if (rom_hex[i] = 105):
        		self.A = self.A + rom_hex[i+1]
        		if (self.A < 0):
        			self.STATUS[7] = 1
        		i+=1
        		
        	i+=1
        		
        
        
        
        #Tests for my sanity
        print(self.A)
        print(self.memory[0])
        print(self.memory[65535])
