#------------Method 1-------------------------------
def list_to_number(numbers):
    # Step 1: Convert every integer into a string
    # Step 2: Join all those strings together into one long string
    # Step 3: Convert the resulting string back into an integer
    result = int(''.join(str(num) for num in numbers))
    return result

# ===== Example =====
sample = [10, 33, 50]
print(list_to_number(sample))  

#------------Method 2-------------------------------
numbers = [1, 3, 50]

# 1. Turn each number into a string
string_list = [str(num) for num in numbers]

# 2. Glue the strings together
joined = ''.join(string_list)

# 3. Convert the big string into an integer
final_number = int(joined)

print(final_number)
