def a_formatter(expressions):
    # verify that the number of problems is less than or equal to 5. Print error otherwise 
    if len(expressions) > 5:
        return 'Error: Too many expressions'