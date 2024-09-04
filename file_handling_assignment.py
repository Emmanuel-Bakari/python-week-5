def create_and_write_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write("Hello there.\n")
            file.write("Here's a number: 42\n")
            file.write("Welcome.\n")
        print(f"Successfully wrote to {filename}.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while writing to {filename}: {e}")
    finally:
        print("Write operation completed.")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading {filename}: {e}")
    finally:
        print("Read operation completed.")

def append_to_file(filename):
    try:
        with open(filename, 'a') as file:
            file.write("Feel free.\n")
            file.write("Dont be shy.\n")
            file.write("Have a good day.\n")
        print(f"Successfully appended to {filename}.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to {filename}: {e}")
    finally:
        print("Append operation completed.")

if __name__ == "__main__":
    filename = "my_file.txt"
    
    create_and_write_file(filename)
    read_file(filename)
    append_to_file(filename)
    read_file(filename) 