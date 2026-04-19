import os

def list_directory(path='.'):
    try:
        entries = os.listdir(path)
        print(f"Contents of directory: {path}")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Example: list current directory
    list_directory()
    # Or provide a specific path
    # list_directory('/path/to/your/directory')
