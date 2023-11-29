import pandas as pd
import matplotlib.pyplot as plt

input_file = input("Enter name of input file: ")

output_file = input("Enter name of output file: ")

children = pd.read_csv("input_file")
children.plot(x = "Date of Census", y = "Total Individuals in Shelter")
plt.show()
