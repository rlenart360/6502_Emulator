class CPU(object):
    def __init__(self):
        # TODO implement proper registers
        self.registers = []

    def process_instruction(self, instruction: bytes):
        # TODO process the instruction
        print(instruction)
