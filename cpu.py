import time
from tkinter import *
# TODO: Make a function that will call an error for invalid instructions.

class CPU(object):
    def __init__(self):
        # The CPU Registers:
        # The Accumulator, X Register, Y Register,
        # Status Register [C,Z,I,D,B,_,V,S], Program Counter, and Stack Pointer.

        self.A = 0
        self.X = 0
        self.Y = 0
        self.STATUS = [0, 0, 0, 0, 0, 0, 0, 0]
        self.PC = 0
        self.SP = 0

        self.memory = []
        for i in range(65536):
            self.memory.append(0)

    def process_instruction(self, rom_hex: bytes):
    
        root = Tk()
        frame = Frame(root, height = 532, width = 532)
        frame.pack()
        screen = Canvas(frame, bg = "black")
        screen.pack()
        screen.place(x =10 , y =10 , height = 512, width = 512)

        # TODO: process the instruction
        # TODO: Use Program Counter instead of 'i'
        i = 0
        while i < len(rom_hex):
            
            self.memory[3] = 1

            # TODO: Figure out how to deal with the flags
            # TEST

            if (rom_hex[i] == 105):

                self.A += rom_hex[i + 1]

                result = '{0:08b}'.format(self.A)
                if (len(result) > 8):
                    self.A = int(result[1:], 2)

                i += 1

            elif (rom_hex[i] == 101):

                self.A += self.memory[rom_hex[i+1]]

                result = '{0:08b}'.format(self.A)
                if (len(result) > 8):
                    self.A = int(result[1:], 2)

                i += 1

            elif (rom_hex[i] == 117):

                self.A += self.memory[rom_hex[i+1] + self.X]

                result = '{0:08b}'.format(self.A)
                if (len(result) > 8):
                    self.A = int(result[1:], 2)

                i += 1

            elif (rom_hex[i] == 109):
                print('ADC ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 125):
                print('ADC ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            elif (rom_hex[i] == 121):
                print('ADC ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',Y')
                i += 2

            elif (rom_hex[i] == 97):
                print('ADC ' + '($' + print_bytes(rom_hex[i + 1]) + ',X)')
                i += 1

            elif (rom_hex[i] == 113):
                print('ADC ' + '($' + print_bytes(rom_hex[i + 1]) + '),Y')
                i += 1

            # AND (Bitwise AND with Accumulator)
            elif (rom_hex[i] == 41):
                print('AND ' + '#$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 37):
                print('AND ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 53):
                print('AND ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 45):
                print('AND ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 61):
                print('AND ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            elif (rom_hex[i] == 57):
                print('AND ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',Y')
                i += 2

            elif (rom_hex[i] == 33):
                print('AND ' + '($' + print_bytes(rom_hex[i + 1]) + ',X)')
                i += 1

            elif (rom_hex[i] == 49):
                print('AND ' + '($' + print_bytes(rom_hex[i + 1]) + '),Y')
                i += 1

            # ASL (Arithmetic Shift Left)
            elif (rom_hex[i] == 10):
                print('ASL A')

            elif (rom_hex[i] == 6):
                print('ASL ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 22):
                print('ASL ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 14):
                print('ASL ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 30):
                print('ASL ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            # BIT (Test BITs)
            elif (rom_hex[i] == 36):
                print('BIT ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 44):
                print('BIT ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            # Branch Instructions

            # BPL (Branch on PLus)
            elif (rom_hex[i] == 16):
                print('BPL ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            # BMI (Branch on MInus)
            elif (rom_hex[i] == 48):
                print('BMI ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            # BVC (Branch on oVerflow Clear)
            elif (rom_hex[i] == 80):
                print('BVC ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            # BVS (Branch on oVerflow Set)
            elif (rom_hex[i] == 112):
                print('BVS ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            # BCC (Branch on Carry Clear)
            elif (rom_hex[i] == 144):
                print('BCC ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            # BCS (Branch on Carry Set)
            elif (rom_hex[i] == 176):
                print('BCS ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            # BNE (Branch on Not Equal)
            elif (rom_hex[i] == 208):
                print('BNE ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            # BEQ (Branch on EQual)
            elif (rom_hex[i] == 240):
                print('BEQ ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            # BRK (Break)
            elif (rom_hex[i] == 0):
                print('BRK')

            # CMP (Compare Accumulator)
            elif (rom_hex[i] == 201):
                print('CMP ' + '#$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 197):
                print('CMP ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 213):
                print('CMP ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 205):
                print('CMP ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 221):
                print('CMP ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            elif (rom_hex[i] == 217):
                print('CMP ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',Y')
                i += 2

            elif (rom_hex[i] == 193):
                print('CMP ' + '($' + print_bytes(rom_hex[i + 1]) + ',X)')
                i += 1

            elif (rom_hex[i] == 209):
                print('CMP ' + '($' + print_bytes(rom_hex[i + 1]) + '),Y')
                i += 1

            # CPX (Compare X Register)
            elif (rom_hex[i] == 224):
                print('CPX ' + '#$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 228):
                print('CPX ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 236):
                print('CPX ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            # CPY (Compare Y Register)
            elif (rom_hex[i] == 192):
                print('CPY ' + '#$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 196):
                print('CPY ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 204):
                print('CPY ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            # DEC (Decrement Memory)
            elif (rom_hex[i] == 198):
                print('DEC ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 214):
                print('DEC ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 206):
                print('DEC ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 222):
                print('DEC ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            # EOR (Bitwise Exclusive OR)
            elif (rom_hex[i] == 73):
                print('EOR ' + '#$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 69):
                print('EOR ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 85):
                print('EOR ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 77):
                print('EOR ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 93):
                print('EOR ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            elif (rom_hex[i] == 89):
                print('EOR ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',Y')
                i += 2

            elif (rom_hex[i] == 65):
                print('EOR ' + '($' + print_bytes(rom_hex[i + 1]) + ',X)')
                i += 1

            elif (rom_hex[i] == 81):
                print('EOR ' + '($' + print_bytes(rom_hex[i + 1]) + '),Y')
                i += 1

            # CLC (Clear Carry)
            elif (rom_hex[i] == 24):
                print('CLC')

            # SEC (Set Carry)
            elif (rom_hex[i] == 56):
                print('SEC')

            # CLI (Clear Interrupt)
            elif (rom_hex[i] == 88):
                print('CLI')

            # SEI (Set Interrupt)
            elif (rom_hex[i] == 120):
                print('SEI')

            # CLV (Clear Overflow)
            elif (rom_hex[i] == 184):
                print('CLV')

            # CLD (Clear Decimal)
            elif (rom_hex[i] == 216):
                print('CLD')

            # SED (Set Decimal)
            elif (rom_hex[i] == 248):
                print('SED')

            # INC (Increment Memory)
            elif (rom_hex[i] == 230):
                print('INC ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 246):
                print('INC ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 238):
                print('INC ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 254):
                print('INC ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            # JMP (Jump)
            elif (rom_hex[i] == 76):
                print('JMP ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 108):
                print('JMP ' + '($' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ')')
                i += 2

            # JSR (Jump to Subroutine)
            elif (rom_hex[i] == 32):
                print('JSR ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            # LDA (Load Accumulator)
            elif (rom_hex[i] == 169):
                print('LDA ' + '#$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 165):
                print('LDA ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 181):
                print('LDA ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 173):
                print('LDA ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 189):
                print('LDA ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            elif (rom_hex[i] == 185):
                print('LDA ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',Y')
                i += 2

            elif (rom_hex[i] == 161):
                print('LDA ' + '($' + print_bytes(rom_hex[i + 1]) + ',X)')
                i += 1

            elif (rom_hex[i] == 177):
                print('LDA ' + '($' + print_bytes(rom_hex[i + 1]) + '),Y')
                i += 1

            # LDX (Load X Register)
            elif (rom_hex[i] == 162):
                print('LDX ' + '#$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 166):
                print('LDX ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 182):
                print('LDX ' + '$' + print_bytes(rom_hex[i + 1]) + ',Y')
                i += 1

            elif (rom_hex[i] == 174):
                print('LDX ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 190):
                print('LDX ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',Y')
                i += 2

            # LDY (Load Y Register)
            elif (rom_hex[i] == 160):
                print('LDY ' + '#$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 164):
                print('LDY ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 180):
                print('LDY ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 172):
                print('LDY ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 188):
                print('LDY ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            # LSR (Logical Shift Right)
            elif (rom_hex[i] == 74):
                print('LSR A')

            elif (rom_hex[i] == 70):
                print('LSR ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 86):
                print('LSR ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 78):
                print('LSR ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 94):
                print('LSR ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            # NOP (No Operation)
            elif (rom_hex[i] == 234):
                print('NOP')

            # ORA (Bitwise OR with Accumulator)
            elif (rom_hex[i] == 9):
                # print('ORA ' + '#$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 5):
                # print('ORA ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 21):
                # print('ORA ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 13):
                # print('ORA ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 29):
                # print('ORA ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            elif (rom_hex[i] == 25):
                # print('ORA ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',Y')
                i += 2

            elif (rom_hex[i] == 1):
                # print('ORA ' + '($' + print_bytes(rom_hex[i + 1]) + ',X)')
                i += 1

            elif (rom_hex[i] == 17):
                # print('ORA ' + '($' + print_bytes(rom_hex[i + 1]) + '),Y')
                i += 1

            # TAX (Transfer A to X)
            elif (rom_hex[i] == 170):
                print('TAX')

            # TXA (Transfer X to A)
            elif (rom_hex[i] == 138):
                print('TXA')

            # DEX (Decrement X)
            elif (rom_hex[i] == 202):
                print('DEX')

            # INX (Increment X)
            elif (rom_hex[i] == 232):
                print('INX')

            # TAY (Transfer A to Y)
            elif (rom_hex[i] == 168):
                print('TAY')

            # TYA (Transfer Y to A)
            elif (rom_hex[i] == 152):
                print('TYA')

            # DEY (Decrement Y)
            elif (rom_hex[i] == 136):
                print('DEY')

            # INY (Increment Y)
            elif (rom_hex[i] == 200):
                print('INY')

            # ROL (Rotate Left)
            elif (rom_hex[i] == 42):
                print('ROL A')

            elif (rom_hex[i] == 38):
                # print('ROL ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 54):
                # print('ROL ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 46):
                # print('ROL ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 62):
                # print('ROL ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2


            # ROR (Rotate Right)
            elif (rom_hex[i] == 106):
                print('ROR A')

            elif (rom_hex[i] == 102):
                # print('ROR ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 118):
                # print('ROR ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 110):
                # print('ROR ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 126):
                # print('ROR ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            # RTI (Return from Interrupt)
            elif (rom_hex[i] == 64):
                print('RTI')

            # RTS (Return from Subroutine)
            elif (rom_hex[i] == 96):
                print('RTS')

            # SBC (Subtract with Carry)
            elif (rom_hex[i] == 233):
                # print('SBC ' + '#$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 229):
                # print('SBC ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 245):
                # print('SBC ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 237):
                # print('SBC ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 253):
                # print('SBC ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            elif (rom_hex[i] == 249):
                # print('SBC ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',Y')
                i += 2

            elif (rom_hex[i] == 225):
                # print('SBC ' + '($' + print_bytes(rom_hex[i + 1]) + ',X)')
                i += 1

            elif (rom_hex[i] == 241):
                # print('SBC ' + '($' + print_bytes(rom_hex[i + 1]) + '),Y')
                i += 1

            # STA (Store Accumulator)
            elif (rom_hex[i] == 133):
                self.memory[rom_hex[i+1]] = self.A
                i += 1

            elif (rom_hex[i] == 149):
                # print('STA ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 141):
                # print('STA ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            elif (rom_hex[i] == 157):
                # print('STA ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',X')
                i += 2

            elif (rom_hex[i] == 153):
                # print('STA ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]) + ',Y')
                i += 2

            elif (rom_hex[i] == 129):
                # print('STA ' + '($' + print_bytes(rom_hex[i + 1]) + ',X)')
                i += 1

            elif (rom_hex[i] == 145):
                # print('STA ' + '($' + print_bytes(rom_hex[i + 1]) + '),Y')
                i += 1

            # TXS (Transfer X to Stack Ptr)
            elif (rom_hex[i] == 154):
                print('TXS')

            # TSX (Transfer Stack Ptr to X)
            elif (rom_hex[i] == 186):
                print('TSX')

            # PHA (Push Accumulator)
            elif (rom_hex[i] == 72):
                print('PHA')

            # PLA (Pull Accumulator)
            elif (rom_hex[i] == 104):
                print('PLA')

            # PHP (Push Processor Status)
            elif (rom_hex[i] == 8):
                print('PHP')

            # PLP (Pull Processor Status)
            elif (rom_hex[i] == 40):
                print('PLP')

            # STX (Store X Register)
            elif (rom_hex[i] == 134):
                # print('STX ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 150):
                # print('STX ' + '$' + print_bytes(rom_hex[i + 1]) + ',Y')
                i += 1

            elif (rom_hex[i] == 142):
                # print('STX ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            # STY (Store Y Register)
            elif (rom_hex[i] == 132):
                # print('STY ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 148):
                # print('STY ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
                i += 1

            elif (rom_hex[i] == 140):
                # print('STY ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2
                
            print("Updating screen...")
            # NOTE: Use memory locations 0 - 1023 for now for testing
            for y in range(32):
                for x in range(32):
                    if self.memory[x] != 0:
                        screen.create_rectangle(0+(x*16), 0, 16+(x*16), 16, fill='red')
                        root.update()
                            
            time.sleep(0.5)

            i += 1

        # Tests for my sanity
        print("ACC = " + str(self.A))
        print("X = " + str(self.X))
        print("Y = " + str(self.Y))
        root.mainloop()
