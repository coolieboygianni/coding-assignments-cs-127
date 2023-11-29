#Name: Gianni Russell
#Date: November 13, 2023
#a program that computes LIRR transit fares.


def computeFare(zone, ticket_type):
    if zone == 1:
        if ticket_type == "peak":
            return 8.75
        elif ticket_type == "off-peak":
            return 6.25
    elif zone == 2 or zone == 3:
        if ticket_type == "peak":
            return 10.25
        elif ticket_type == "off-peak":
            return 7.50
    elif zone == 4:
        if ticket_type == "peak":
            return 12.00
        elif ticket_type == "off-peak":
            return 8.75
    elif zone == 5 or zone == 6 or zone == 7:
        if ticket_type == "peak":
            return 13.50
        elif ticket_type == "off-peak":
            return 9.75
    else:
        return -1
    return(computeFare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()