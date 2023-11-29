#Name: Gianni Russell
#gianni.russell07@myhunter.cuny.edu
#Date: november 9, 2023
import pandas as pd

def read_collision_data(file_name):
    return pd.read_csv(file_name)

def get_top_three_contributing_factors(collision_data):
    factors = collision_data['CONTRIBUTING FACTOR VEHICLE 1'].value_counts()
    return factors.head(3)

def main():
    file_name = input("Enter CSV file name: ")
    collision_data = read_collision_data(file_name)
    top_three_factors = get_top_three_contributing_factors(collision_data)

    print("Top three contributing factors for collisions:")
    print("CONTRIBUTING FACTOR VEHICLE 1")
    print(top_three_factors)

if __name__ == "__main__":
    main()
