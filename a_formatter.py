def arithmetic_arranger(problems):
  
  # verify that the number of problems is less than or equal to 5. Print error otherwise 
  if len(problems) > 5:
    return 'Error: Too many problems'

  # check if the operand is correct. Only accept "+" or "-"
  for problem in problems:
    # get rid of spaces
    stripped_problem = problem.replace(' ', '')

    flag = False
  
    # to find the operator, break down each "problem", or supplied expression into 3 parts: 1st number, the operator, and 2nd number 
    for character in stripped_problem:
      # go through the string and separate it
      if character in ["+", "-"]:
        # find the index of the operator in the stripped problem
        operator_index = stripped_problem.find(character)
        # based on that index, identify the left and right numbers
        left_number = stripped_problem[:operator_index]
        right_number = stripped_problem[operator_index+1:]

        flag = True
    if flag == False:
      return "Error: Operator must be '+' or '-'"
      
      # check that the 1st and 2nd numbers only contain digits and are no longer than 4 characters
      if len(left_number) <= 4 and len(right_number) <= 4:
        
