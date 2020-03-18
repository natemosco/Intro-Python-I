# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num):
    if num % 2 == 0:
        return "true"
    else:
        return "false"


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(is_even(num))
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def print_even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


num2 = input("enter a number: ")
num2 = int(num2)
print_even_odd(num2)
