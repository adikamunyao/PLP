# Task 4: Find common elements between two sets
def common_elements():
    set1 = set(map(int, input("Enter the elements of the first set (comma-separated): ").split(',')))
    set2 = set(map(int, input("Enter the elements of the second set (comma-separated): ").split(',')))

    common_set = set1.intersection(set2)
    print(f"The common elements are: {common_set}")

# Call the function
common_elements()
