#!/usr/bin/env python3

def get_input(prompt):
    """Function to get input from the user."""
    return input(prompt).strip()

def main():
    # Prompt the user for inputs
    old_pattern = get_input("Enter the old pattern: ")
    new_pattern = get_input("Enter the new pattern: ")
    file_name = get_input("Enter the filename: ")

    # Check if the file exists and read its contents
    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
    except FileNotFoundError:
        print(f"File \"{file_name}\" does not exist.")
        return

    # Perform the substitution
    updated_contents = file_contents.replace(old_pattern, new_pattern)

    # Write the updated contents back to the file
    with open(file_name, 'w') as file:
        file.write(updated_contents)

    print(f"File {file_name} has been updated.")

if __name__ == "__main__":
    main()

