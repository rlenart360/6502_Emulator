from print_bytes import print_bytes

class Disassembler(object):
    def __init__(self):
        pass

    def process_hex(self, rom_hex):
        print(rom_hex)
        
        # Loop that will process the ROM
        
        # TODO: Find out where the actual game starts in the ROM and set *i* accordingly
        
        i = 0
        while i < (len(rom_hex)):

            # ADC (Add with Carry)
            if (rom_hex[i] == 105):
                print('ADC ' + '#$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 101):
                print('ADC ' + '$' + print_bytes(rom_hex[i + 1]))
                i += 1

            elif (rom_hex[i] == 117):
                print('ADC ' + '$' + print_bytes(rom_hex[i + 1]) + ',X')
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
            
            # TAX (Transfer A to X)
            # TXA (Transfer X to A)
            # DEX (Decrement X)
            # INX (Increment X)
            # TAY (Transfer A to Y)
            # TYA (Transfer Y to A)
            # DEY (Decrement Y)
            # INY (Increment Y)
            
            # ROL (Rotate Left)
            
            # ROR (Rotate Right)
            
            # RTI (Return from Interrupt)
            
            # RTS (Return from Subroutine)
            
            # SBC (Subtract with Carry)
            
            # STA (Store Accumulator)
            
            # TXS (Transfer X to Stack Ptr)
            # TSX (Transfer Stack Ptr to X)
            # PHA (Push Accumulator)
            # PLA (Pull Accumulator)
            # PHP (Push Processor Status)
            # PLP (Pull Processor Status)
            
            # STX (Store X Register)
            
            # STY (Store Y Register)
            # TODO: Keep working on the Disassembler

            i += 1
