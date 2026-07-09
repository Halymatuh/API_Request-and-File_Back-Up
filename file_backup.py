import os

source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")

try:

    if not os.path.exists(source):
        print("Error: Source file does not exist.")
    elif os.path.exists(destination):
        print("Error: Destination file already exists.")
    else:

        with open(source, "r") as file:
            content = file.read()

        with open(destination, "w") as file:
            file.write(content)

        print("File copied successfully!")

except PermissionError:
    print("Error: Permission denied.")

except IOError:
    print("Error: Could not open the file.")

except Exception as e:
    print("An unexpected error occurred:", e)
