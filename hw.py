def update(original, index, new_char):
    if index < 0 or index >= len(original):
        return "Index out of range!"
    return original[:index] + new_char + original[index + 1:]

def delete(original, index):
    if index < 0 or index >= len(original):
        return "Index out of range!"
    return original[:index] + original[index + 1:]

string = input("Enter the string: ")


choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    idx = int(input("Enter the index of character to update: "))
    new_char = input("Enter the new character: ")
    updatedstring = update(string, idx, new_char)
    print("Updated string:", updatedstring)

elif choice == '2':
    idx = int(input("Enter the index of character to delete: "))
    updatedstring = delete(string, idx)
    print("String after deletion:", updatedstring)

else:
    print("Invalid choice!")

    
