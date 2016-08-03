# TODO: Make a function that will call an error for invalid instructions.

class CPU(object):
    def __init__(self):
        # The CPU Registers:
        # The Accumulator, X Register, Y Register,
        # Status Register [C,Z,I,D,B,_,V,S], Program Counter, and Stack Pointer.
        
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
        	
        	if (rom_hex[i] == 105):
        	
        		self.A = self.A + rom_hex[i+1]
        		
        		
        		if (self.A < 0):
        			self.STATUS[7] = 1
        		else: self.STATUS[7] = 0
        		
        		#if ():
        		#	self.STATUS[6] = 1
        		#else: self.STATUS[6] = 0
        		
        		if (self.A == 0):
        			self.STATUS[1] = 1
        		else: self.STATUS[1] = 0
        		
        		if (self.A > 255):
        			self.STATUS[0] = 1
        		else: self.STATUS[0] = 0
        		
        		i+=1
        		
        	i+=1
        		
        
        
        
        #Tests for my sanity
        print(self.A)
        print(self.STATUS)
