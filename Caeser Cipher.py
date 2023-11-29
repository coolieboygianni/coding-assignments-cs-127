#Name: Gianni Russell
#gianni.russell07@myhunter.cuny.edu
#Date: September 20, 2023
#This program prompts the user for a message then uses the caeser cipher to create a new one

word = input()
codedWord = ""
for ch in word:
  offset = ord(ch) - ord('a') + 13
  wrap = offset % 26  
  newChar = chr(ord('a') + wrap)  
  print(wrap, chr(ord('a') + wrap))   
  codedWord = codedWord + newChar 
  
print("The coded word (with wrap) is", codedWord)
