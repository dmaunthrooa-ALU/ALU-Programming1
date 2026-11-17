def second_smallest(numbers):
    # Step 1: Convert the list to a set to remove any duplicate values
    unique_numbers = list(set(numbers))

    # Step 2: Sort the unique numbers from smallest to largest
    unique_numbers.sort()

    # Step 3: Safety check – we need at least two different numbers
    if len(unique_numbers) < 2:
        return "List must have at least two unique numbers"

    # Step 4: The second-smallest number is now at index 1
    return unique_numbers[1]

# ===== Example usage =====
my_list = [12, 5, 8, 5, 19, 3, 7, 3]
print(second_smallest(my_list))   # Output: 5


