import os


def read_file():
    filename = input("Please enter the filename: ")
    
    try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of {filename}:\n")
            print(content)
    
        # Step 2: Check if file exists and is readable
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"File '{filename}' does not exist.")

        # Step 3: Ask the user for the type of modification
        print("Choose a modification type:")
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        print("3. Reverse text")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            modification = str.upper  # Convert to uppercase
        elif choice == '2':
            modification = str.lower  # Convert to lowercase
        elif choice == '3':
            modification = lambda s: s[::-1]  # Reverse text
        else:
            raise ValueError("Invalid choice. Please select 1, 2, or 3.")

        # Step 4: Prepare the new file name
        new_filename = f"modified_{os.path.basename(filename)}"

        # Step 5: Process the file line-by-line
        with open(filename, 'r') as file, open(new_filename, 'w') as new_file:
            for line in file:
                new_file.write(modification(line))

        print(f"File has been modified and saved as '{new_filename}'.")

        # Ask if user wants to try another file
        choice = input("\nWould you like to read another file? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the file reader. Goodbye!")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: Could not read the file {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
           

# Example usage
read_file()
