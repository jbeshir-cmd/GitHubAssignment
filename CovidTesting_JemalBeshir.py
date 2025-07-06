# Question 2: To collect information on the race, gender, and income of the test subject,
# the program would have to prompt the test subject, asking for the race, gender and income. 
# From there, I would store the input into variables, being race, gender and income.
# The main issue though would be with inputs spelling incorrectly, or giving inputs that are
# correct, but are creating errors. Such as not using commas for the income, or using lowercase.

def is_valid_sample(sample_quality):
    """Test if the sample quality is acceptable.

    Returns True if the sample quality is high enough for valid test results
    and, False if it is not.
    """
    if sample_quality >= .9:
        return True
    else:
        return False

def is_valid_calibration(calibration_time):
    """Test if the calibration is acceptable.

    Returns True if the calibration time is low enough for valid results, and
    False if it is not.
    """
    if calibration_time < 5:
        return True
    else:
        return False

def main():
    total_tests = 0
    positive_tests = 0

    while True:
        answer = input("Test positive? [y,n or stop]: ")
        if answer == "stop":
            break

        if answer == "y":
            test_result = True
        else:
            test_result = False

        q = float(input("Sample quality: "))
        t = int(input("Minutes since last calibration: "))
        race = input("Enter your Race:")
        gender = input("Enter your gender")
        income = input("Enter your income, using no commas or decimals:")

        total_tests += 1

        if is_valid_sample(q) and test_result and is_valid_calibration(t): # For the test to be valid, both the sample being valid AND the calibration being valid should met, not either or.
            positive_tests += 1

    print()
    print("Total tests: ", total_tests)
    print("Positive: ", positive_tests)
    print("Negative: ", total_tests - positive_tests)

main()