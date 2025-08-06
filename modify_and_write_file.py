def modify_and_write_file(input_filename="original.txt", output_filename="modified.txt"):
    """
    Reads the content of a file, modifies it, and writes it to a new file.

    Args:
        input_filename (str): The name of the file to read.
        output_filename (str): The name of the file to write the modified content to.
    """
    try:
        # Create a dummy original file for demonstration purposes
        with open(input_filename, 'w') as f:
            f.write("This is the original content of the file.\n")
            f.write("It has multiple lines.\n")
            f.write("Let's see how the program modifies it.")

        # Read the content from the original file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully read from '{input_filename}', modified the content, and wrote to '{output_filename}'.")
        print("\nOriginal Content:\n" + content)
        print("\nModified Content:\n" + modified_content)

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Run the challenge
modify_and_write_file()