# Reading
with open("test.txt") as myFile:
    print("1. Reading -\n" + myFile.read())

# Writing
with open("test.txt","w") as myFile:
    myFile.write("Updated Data")

# Create a new file and then write. If file is already present, it throws error
# with open("test.txt","x") as myFile:
    # myFile.write("Updated Data")


# Appending
with open("test.txt","a") as myFile:
    myFile.write("\nAppended Data")

# Appending and reading simultaneously
with open("test.txt","a+") as myFile:
    myFile.write("\nNew Item Added")
    myFile.seek(0)
    print("2. Appending -\n",myFile.read())
