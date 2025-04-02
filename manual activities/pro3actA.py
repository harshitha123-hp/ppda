def display_list(lst):
    """Displays the current state of the list."""
    print("Current List:", lst)

def insert_element(lst):
    """Inserts an element into the list."""
    element = input("Enter element to insert: ")
    lst.append(element)
    print(f"'{element}' added to the list.")

def delete_element(lst):
    """Deletes an element from the list if it exists."""
    element = input("Enter element to delete: ")
    if element in lst:
        lst.remove(element)
        print(f"'{element}' removed from the list.")
    else:
        print(f"'{element}' not found in the list.")

def find_element(lst):
    """Finds if an element exists in the list."""
    element = input("Enter element to find: ")
    if element in lst:
        print(f"'{element}' found in the list at index {lst.index(element)}.")
    else:
        print(f"'{element}' not found in the list.")

def sort_list(lst):
    """Sorts the list in ascending order."""
    lst.sort()
    print("List sorted in ascending order.")

def reverse_list(lst):
    """Reverses the list."""
    lst.reverse()
    print("List reversed.")

def main():
    lst = []  # Initialize an empty list
    
    while True:
        print("\nChoose an operation:")
        print("1. Insert an element")
        print("2. Delete an element")
        print("3. Find an element")
        print("4. Sort the list")
        print("5. Reverse the list")
        print("6. Display the list")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            insert_element(lst)
        elif choice == '2':
            delete_element(lst)
        elif choice == '3':
            find_element(lst)
        elif choice == '4':
            sort_list(lst)
        elif choice == '5':
            reverse_list(lst)
        elif choice == '6':
            display_list(lst)
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

# Run the program
main()
