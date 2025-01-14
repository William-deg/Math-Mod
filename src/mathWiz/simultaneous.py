from matrices import Matrix


def __decodeEquation__(equation: str) -> list:
    equation1 = equation.replace(' ', '')
    attributes = []

    sum = float(equation1.split('=')[1].strip())
    attributes.append(sum)

    equation_sub = equation1.split('=')[0]

    breakdown = []
    current = []

    for char in equation_sub:
        if char == '+' or char == '-':
            if current:
                breakdown.append(current)
            breakdown.append(char)
            current = []
        else:
            current.append(char)

    breakdown.append(current)

    for i in range(len(breakdown)):
        if i == 0 and breakdown[0] != '-':
            attributes.append({f'{breakdown[0][-1]}': float(''.join(breakdown[0])[:-1])})
        elif breakdown[i] == '+' or breakdown[i] == '-':
            continue
        else:
            attributes.append({f'{breakdown[i][-1]}': (float(''.join(breakdown[i])[:-1])*1 if breakdown[i-1] == '+' else float(''.join(breakdown[i])[:-1])*-1)})
    
    return attributes


# deesired decoded output [2, {'x': 2}, {'y': 5}]

def solveSim(*equations):
    for equation in equations:
        attributes = __decodeEquation__(equation)

    #A = Matrix()
    #A_INVERSE = A.inverse()
    pass

__decodeEquation__('-2.054x-4y= 2')
#print(solveSim('2x+3y=2', '3x-5y=5'))