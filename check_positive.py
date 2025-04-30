
def is_positive(number):
    # Check if the number is positive
    if number > 0:
        return True
    else:
        return False

# Testing
test_number = -5
output = is_positive(test_number)
print("Is the number positive?", output)