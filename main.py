# import functions from the external class
from a_formatter import arithmetic_arranger, generate_random_numbers

# create a list of random problems
random_problems = generate_random_numbers(5)

# print the problems with their solutions
print(arithmetic_arranger(random_problems, True))
