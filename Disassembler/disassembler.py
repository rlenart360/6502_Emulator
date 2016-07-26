from print_bytes import print_bytes

class Disassembler(object):
    def __init__(self):
        pass

    def process_hex(self, rom_hex):
        print(rom_hex)
        
        # Loop that will process the ROM
        i = 0
        while i < (len(rom_hex)):

            # LSR (Logical Shift Right), MODE: Absolute, LENGTH: 3 bytes
            if (rom_hex[i] == 78):
                print('LSR ' + '$' + print_bytes(rom_hex[i + 2]) + print_bytes(rom_hex[i + 1]))
                i += 2

            # ORA (Bitwise OR with Accumulator), MODE: Indirect, X, LENGTH: 2 bytes
            elif (rom_hex[i] == 1):
                print('ORA ' + '($' + print_bytes(rom_hex[i + 1]) + ',X)')
                i += 1

            # SEI (Set Interrupt), Processor Status Instruction
            elif (rom_hex[i] == 120):
                print('SEI')

            # CLD (Clear Decimal), Processor Status Instruction
            elif (rom_hex[i] == 216):
                print('CLD')

            # ADC (Add with Carry)
            elif (rom_hex[i] == 105):
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
            
            # EOR (Bitwise Exclusive OR)
            
            # CLC (Clear Carry)
            # SEC (Set Carry)
            # CLI (Clear Interrupt)
            # SEI (Set Interrupt)
            # CLV (Clear Overflow)
            # CLD (Clear Decimal)
            # SED (Set Decimal)
            
            # INC (Increment Memory)
            
            # JMP (Jump)
            
            # JSR (Jump to Subroutine)
            
            # LDA (Load Accumulator)
            
            # LDX (Load X Register)
            
            # LDY (Load Y Register)
            
            # LSR (Logical Shift Right)
            
            # NOP (No Operation)
            
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
