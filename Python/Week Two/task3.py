# Task 3: Store information in a dictionary and print it
def person_info():
    person = {}
    
    person['name'] = input("Enter your name: ")
    person['age'] = int(input("Enter your age: "))
    person['favorite_color'] = input("Enter your favorite color: ")
    
    print(f"\nPerson's Information:\n{person}")

# Call the function
person_info()
