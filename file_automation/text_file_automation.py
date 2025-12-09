# Write to a text file
with open("sample.txt", "w") as f:
    f.write("Hello World\n")
    f.write("This is a test file\n")

# Read from the text file
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())