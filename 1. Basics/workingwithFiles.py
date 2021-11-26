# Reading
with open("test.txt") as myFile:
    print(myFile.read())

# Writing
with open("test.txt","w") as myFile:
    myFile.write("Updated Data")

# Appending
with open("text.txt","a") as myFile:
    print()