# Program that reads a text file, processes its content, and writes the results to a new file.

# Read the input file
with open("./input.txt", "r") as file:
    data = file.read()

# Process the data
num_words = len(data.split())  # Count words
upper_case = data.upper()      # Convert to uppercase

# Display result
print(f"The number of words in the file is {num_words} words.")

# Write to the output file
with open("./output.txt", "w") as new_file:
    new_file.write(upper_case)

print("Operation successful")

 
 