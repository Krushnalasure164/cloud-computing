# 1. Ask for input
user_input = input("Enter numbers separated by spaces: ")

# 2. Convert input strings to integers
numbers = [int(n) for n in user_input.split()]

# 3. Sort the list
numbers.sort()

# 4. Print results
print("Sorted Numbers:", numbers)
