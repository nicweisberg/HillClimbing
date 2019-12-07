
def machine_exec(sequence, entry):
    """
    Simulates a simple calculating machine.
    """
    register = 0
    index = 1
    
    for operator in sequence:
        operand = entry[index]
        # perform the instruction
        if operator == "ADD":
            register += operand
        elif operator == "SUB":
            register -= operand
        elif operator == "MUL":
            register *= operand
        elif operator == "DIV":
            register = register / operand
        elif operator == "NOP":
            pass
        else:
            print('unknown operator', operator)
            register = None 
        index = index + 1
        
    return register




