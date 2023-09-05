# Need to define the function split_and_sort
def split_and_sort(nums):
    # Check whether input list length is less than or equal to 20
    if len(nums) > 20:
        return "Error: Input list should not contain more than 20 integers."
    # Check if there is 0 in the input list
    if 0 in nums:
        return "Error: The number 0 is not a valid input."
    # Filter the odd and even numbers into two separate lists
    odd_nums = [num for num in nums if num % 2 == 1]
    even_nums = [num for num in nums if num % 2 == 0]
    # Remove the duplicates and sort them out.
    odd_nums = sorted(odd_nums)
    even_nums = sorted(even_nums)
    return odd_nums, even_nums

# Testing with the Test Case 1.
nums = [3, 10, 9, 20, 16, 10, 9, 15, 7, 5, 28, 20, 5, 8, 20]
odd_nums, even_nums = split_and_sort(nums)
print("Test Case 1 - Odd numbers:", odd_nums)
print("Test Case 1 - Even numbers:", even_nums)

# Testing with the Test Case 2.
nums = [13, 7, 9, 15]
odd_nums, even_nums = split_and_sort(nums)
print("Test Case 2 - Odd numbers:", odd_nums)
print("Test Case 2 - Even numbers:", even_nums)

# Testing with the Test Case 3.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
odd_nums, even_nums = split_and_sort(nums)
print("Test Case 3 - Odd numbers:", odd_nums)
print("Test Case 3 - Even numbers:", even_nums)

# Testing with the Test Case 4.
nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odd_nums, even_nums = split_and_sort(nums)
print("Test Case 4 - Odd numbers:", odd_nums)
print("Test Case 4 - Even numbers:", even_nums)

# Testing with the Test Case 5.
nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
odd_nums, even_nums = split_and_sort(nums)
print("Test Case 5 - Odd numbers:", odd_nums)
print("Test Case 5 - Even numbers:", even_nums)

# Testing with the Test Case 6.
nums = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9]
result = split_and_sort(nums)
print("Test Case 6 - Result:", result)  # This will print out the error message saying “Error: The number 0 is not a valid input.”
