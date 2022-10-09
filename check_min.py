
def get_statement_index(equation, operator_index):
    start_index = operator_index - 1
    end_index = operator_index + 1

    char = equation[start_index]
    while True:
        if not (char.isnumeric() or char == '.' or char == '~'):
            start_index += 2
            break
        elif (start_index == 0):
            break
        else:
            char = equation[start_index]
        start_index -= 1

    char = equation[end_index]
    while True:
        if not (char.isnumeric() or char == '.' or char == '~'):
            end_index -= 1
            print("break")
            break
        elif (end_index > len(equation) - 1):
            end_index += 1
            break
        else:
            char = equation[end_index]
        end_index += 1

    sub_statement = equation[start_index:end_index]
    first_num = round(float(equation[start_index:operator_index]), 2)
    second_num = round(
        float(equation[operator_index + 1: end_index]), 2)
    return sub_statement, first_num, second_num


subequation, first_num, second_num = get_statement_index('~1+2', 1)
print(subequation, first_num, second_num)

subequation, first_num, second_num = get_statement_index('22+24', 2)

print(subequation, first_num, second_num)
subequation, first_num, second_num = get_statement_index('33+24+2', 2)

print(subequation, first_num, second_num)
subequation, first_num, second_num = get_statement_index('3+24+35', 4)

print(subequation, first_num, second_num)
subequation, first_num, second_num = get_statement_index('22+2', 2)
print(subequation, first_num, second_num)
