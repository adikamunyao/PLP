# Task 1: Create a list of integers and compute the sum
def sum_of_integers():
    num_list = []
    while True:
        try:
            num = int(input("Enter an integer (or type 'done' to finish): "))
            num_list.append(num)
        except ValueError:
            break  # Exit when 'done' or non-numeric input is given

    print(f"The sum of all integers is: {sum(num_list)}")

# Call the function
sum_of_integers()
