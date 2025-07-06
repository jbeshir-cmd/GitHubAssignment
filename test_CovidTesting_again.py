from CovidTesting2_JemalBeshir import is_valid_sample, is_valid_calibration
def test_sample():
    assert is_valid_sample(0.97) == True
    assert is_valid_calibration(4) == True
    assert is_valid_sample(0.89) == False
    assert is_valid_calibration(8) == False    
#Question 3:
#Then it comes to testing, I noted during this exercise 
#that you must ensure the inputs are handled correctly 
#and that positive test cases execute as intended. 
#You need to verify what the user types in and determine 
#if the result is valid. If the input is “stop,” the loop 
#should break. If it’s “yes,” the test result should be 
#accurate, and anything else should be false. That’s what 
#helps decide if the test is positive or not. Because of 
#that, I would say that this approach is more effective, 
#but it can also be more effective, including the input 
#being tested.
#The current code structure, with everything happening 
#directly inside the loop, could become messy and more 
#complicated to manage as the program becomes more complex. It would make more sense to move that part of testing the input into its own function. Something like def is_test_t_or_f() could help keep the code cleaner and easier to work with down the line.