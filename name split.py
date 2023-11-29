#Gianni Russell
#October 31, 2023
def enter_names():
    print("Enter a list of names, separated by semicolons and a space ('; '), and last name, first name (i.e. separated by ', '):")
    return input()

def format_names(names_str):
    names = names_str.split('; ')
    first_names = [name.split(', ')[1] for name in names]
    last_names = [name.split(', ')[0] for name in names]
    return first_names, last_names

def print_names(first_names, last_names):
    for i in range(len(first_names)):
        print(first_names[i], last_names[i])

def main():
    names_str = enter_names()
    first_names, last_names = format_names(names_str)
    print_names(first_names, last_names)

if __name__ == "__main__":
    main()

