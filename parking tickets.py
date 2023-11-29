#Gianni Russell
#October 31, 2023

import pandas as pd

csvFile = input('Enter CSV file name: ')      

tickets = pd.read_csv(csvFile)     

attribute = input('Enter attribute: ')     

attribute_counts = tickets[attribute].value_counts()

print("The 10 worst offenders are:")
print(attribute_counts[:10])