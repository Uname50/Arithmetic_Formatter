def arithmetic_arranger(problems, display_answers=False):
    
    # check the number of problems
    if len(problems) > 5:
        return 'Error: Too many problems!'

    # initialize lists to hold each part of the formatted problems
    first_operands = []
    second_operands = []
    dashes = []
    results = []

    # iterate through each provided problem
    for problem in problems:
        
        # split the problem into components (operands and operator)
        parts = problem.split()  
        
        # assign operands and operator
        left_number, operator, right_number = parts[0], parts[1], parts[2]  

        # validation checks

        # check if the operands only contain digits
        if not(left_number.isdigit() and right_number.isdigit()):
            return 'Error: Numbers must only contain digits'
        
        # check if the operands contain no more than 4 digits
        if len(left_number) > 4 or len(right_number) > 4:
            return 'Error: Numbers cannot be more than four digits'
        
        # check if the operator is correct (only addition and subtraction allowed)
        if operator not in ['+', '-']:
            return 'Error: Operator must be "+" or "-"'

        # calculate the width for the formatting based on the longest operand and add 2 more spaces for the operator
        width = max(len(left_number), len(right_number)) + 2 

        # format the operands and operator, right-aligned
        top = left_number.rjust(width)
        bottom = operator + right_number.rjust(width - 1)
        
        # insert a line of dashes
        dash = '-' * width  
        
        # calculate the result if the operator is '+' or '-'
        if operator == '+':
            result = str(int(left_number) + int(right_number)).rjust(width)
        else:
            result = str(int(left_number) - int(right_number)).rjust(width)

        # append formatted components to their respective lists
        first_operands.append(top)
        second_operands.append(bottom)
        dashes.append(dash)
        results.append(result)

    # assemble the formatted problems line by line
    arranged_problems = '    '.join(first_operands) + '\n' + \
                        '    '.join(second_operands) + '\n' + \
                        '    '.join(dashes)
    
    # include results if display_answers is True
    if display_answers:
        arranged_problems += '\n' + '    '.join(results)

    # return the final formatted string
    return arranged_problems

