# Task 5: List comprehension to filter words with an odd number of characters
def odd_length_words():
    words = input("Enter a list of words (comma-separated): ").split(',')
    
    # List comprehension to filter words with odd length
    odd_words = [word for word in words if len(word.strip()) % 2 != 0]
    
    print(f"Words with an odd number of characters: {odd_words}")

# Call the function
odd_length_words()
