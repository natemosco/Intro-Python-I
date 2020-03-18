"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE


def print_file(location):
    with open(location, 'r') as current_file:
        print(current_file.read())
    current_file.close()
    print("is current file closed?:", current_file.closed)


print_file("./foo.txt")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE


def make_bar_file():
    with open("./bar.txt", "w") as bar:
        bar.write("Cuz you're dreaming with your eyes wide open. \n You cannot be afraid, Come Alive! Come Alive\n When the world becomes a fantasy...\n lyrics from dreaming with your eyes wide open from the feature film 'the greatest showman.'")
        bar.close()


make_bar_file()
print_file("./bar.txt")
