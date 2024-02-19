# import the functions
from a_formatter import arithmetic_arranger, generate_random_numbers

# function to test the arranger function by itself
def test_arithmetic_arranger():
    
    # test with a mix of normal problems
    input_problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    expected_output = "   32      3801      45      123\n+ 698    -    2    + 43    +  49\n-----    ------    ----    -----"
    assert arithmetic_arranger(input_problems) == expected_output, "Normal case failed"

    # test case: too many problems
    input_problems_too_many = ["32 + 32"] * 6 
    expected_error = "Error: Too many problems!"
    assert arithmetic_arranger(input_problems_too_many) == expected_error, "Too many problems case failed"

    # test for the number of digits 

    # test operator 

# function to test the randomizer
def test_generate_random_numbers():
    # check for the number of generated problems
    num_problems = 5
    generated_problems = generate_random_numbers(num_problems)
    assert len(generated_problems) == num_problems, "Generated problems count mismatch"

# Run the test functions
test_arithmetic_arranger()
test_generate_random_numbers()
print("All tests passed!")
