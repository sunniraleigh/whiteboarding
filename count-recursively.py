# TEST CASES
# One
# [4] -> 1
# None
# [] -> 0
# Many
# [4,5,8,9] -> 4

def count_recursively(lst):
    """Return number of items in a list, using recursion."""
    # define a length counter
    # loop over list
    # add 1 to length everytime

    if lst == []:
        return 0
    else:
        length = 1

        # add 1 to length for every item in the list

        new_lst = lst[1:]

        new_len = count_recursively(new_lst)

        return length + new_len


# [4,5,8,9]
# length=1
# new_list = [5,8,9]
# len + new_len = 1 + 3
# return 4

# [5,8,9]
# length=1
# new_list = [8,9]
# len + new_len = 1 + 2
# return 3

# [8,9]
# length = 1
# new_list = [9]
# len + new_len = 1 + 1
# return 2

# [9]
# length=1
# []
# lenght + new_len = 1 + 0
# return 1

# []
# length=0
# return 0

def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    # START SOLUTION

    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])