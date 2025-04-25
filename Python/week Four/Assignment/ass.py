# File Reader & Writer with Error Handling 🧪🖋️

def modify_content(content):
    """Function to modify the file content."""
    return content.upper()  # You can change this to any transformation

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            data = file.read()
            word_count = len(data.split())
            modified_data = modify_content(data)

            print(f"\n✅ The file was read successfully.")
            print(f"📄 Word count: {word_count} words")

            output_filename = "output_modified.txt"
            with open(output_filename, 'w') as new_file:
                new_file.write(modified_data)

            print(f"✍️ Modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"❌ Error: Could not read the file '{filename}'.")

if __name__ == "__main__":
    main()
