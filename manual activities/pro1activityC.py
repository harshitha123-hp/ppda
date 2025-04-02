def find_largest_number():
    print("Enter five numbers to find the largest among them:")

    # Initialize the first number as the largest
    largest = float(input("Enter number 1: "))

    # Loop to get the remaining 4 numbers
    for i in range(2, 6):
        num = float(input(f"Enter number {i}: "))
        if num > largest:
            largest = num  # Update the largest number if a bigger one is found

    print(f"The largest number is: {largest}")

# Run the program
find_largest_number()
