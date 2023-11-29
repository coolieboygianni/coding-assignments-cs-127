#Name: Gianni Russell
#gianni.russell07@myhunter.cuny.edu
#Date: September 29, 2023

def reverse_message(message):
    reversed_message = message[::-1]
    doubled_message = ""
    
    for char in reversed_message:
        doubled_message += char * 2
    
    return doubled_message

message = input("Enter a message: ")
reversed_output = reverse_message(message)

print("Reversed Message:")
for line in reversed_output:
    print(line)
