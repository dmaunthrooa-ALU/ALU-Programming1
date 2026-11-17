def have_common_member(list1, list2):
    # Loop through every item in the first list one by one
    for item in list1:
        # Check whether the current item also exists in the second list
        if item in list2:
            # As soon as we find one common item, we can stop and return True
            return True
    # If the loop finishes without finding any common item, return False
    return False

print(have_common_member([1, 2, 3, 4], [4, 5, 6]))