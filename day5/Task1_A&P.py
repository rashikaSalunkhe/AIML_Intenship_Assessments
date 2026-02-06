def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


# Taking user input
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Calling the function
area, perimeter = calc_rectangle(length, width)

# Printing the result
print(f"Area: {area}, Perimeter: {perimeter}")