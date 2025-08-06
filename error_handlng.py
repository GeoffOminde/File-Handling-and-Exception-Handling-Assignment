def read_file_with_error_handling():
    """
    Asks the user for a filename, tries to read it, and handles potential errors.
    """
    filename = input("Please enter the filename you would like to read (e.g., 'my_document.txt'): ")

    try:
        with open(filename, 'r') as f:
            content = f.read()
            print("\n--- File Content ---")
            print(content)
            print("--------------------")
            print("\nFile read successfully!")

    except FileNotFoundError:
        print(f"\nError: The file '{filename}' does not exist. Please check the name and try again.")
    except IsADirectoryError:
        print(f"\nError: '{filename}' is a directory, not a file. Please provide a valid file name.")
    except IOError as e:
        print(f"\nAn error occurred while trying to read the file '{filename}': {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# To test this, you can try entering:
# 1. A filename that doesn't exist (e.g., 'non_existent_file.txt')
# 2. The name of a directory if one exists
# 3. A valid filename (you can create a 'my_document.txt' file in the same directory)

# Create a dummy file for a successful test case
with open("my_document.txt", "w") as f:
    f.write("This is a test document for the Error Handling Lab.")

# Run the lab
read_file_with_error_handling()