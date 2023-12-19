"""
Your task is to complete the sum_of_even_numbers 
function so that it calculates and returns the 
sum of all even numbers in the given list. 
Once you've written the code, you can test it with 
the example usage provided.
"""

def sum_of_even_numbers(numbers):
    # My code goes here
    even_number = []
    for num in numbers:
        even = num % 2
        if even == 0:
            even_number.append(num)
    return sum(even_number)
    # End of my code

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers_list)
print(f"Sum of even numbers: {result}")