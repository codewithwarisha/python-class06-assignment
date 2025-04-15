# File Handling Example

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file!\n")
    file.write("We are learning Python file handling.")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)
