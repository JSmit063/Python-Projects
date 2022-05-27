'''
Justin Smith
Final Exam Part 2
12/16/2021

Decomposition:
This program will help track information for a schools bottle drive.
It will calculate some totals, averages, and print the information to
the user. Lastly, it will print out each grades totals at the end.

Inputs: There are none, the lists are hard coded to the program
Outputs: Every function outputs the result to the user

Function 1:
Uses a loop to get the total can value and prints to the user in main
This function uses parameters and returns a value

Function 2:
Gets the average can value and prints to the user in main
This function uses parameters and returns a value

Function 3:
Uses a loop to get the num of above average grades. Print within the function
This function uses parameters but does not return a value

Function 4:
This is my extra function that uses two parallel lists to list out the grade number
and cans collected for each grade. This function accepts parameters but does not return any values.
Values are printed within the module.
'''

# This module gathers the can total
def CanTotal(cans):
    Total = int()
    # Use a for loop to increment the cans
    for index in range(len(cans)):
        Total = Total + cans[index]
    # return the new total to the main module
    return Total

# This module gathers the average cans collected
def AvgCans(TotalCollected):
    Avg = float()
    Avg = TotalCollected / 9
    # Return the Avg back to main
    return Avg

# This module takes the average collected
# and prints how many grades are above average
def AboveAvg(cans, AvgCollected):
    count = int()
    # Loop to find the amount of higher than average grades
    for index in range(len(cans)):
        if cans[index] > AvgCollected:
            # Increment the counter if true
            count = count + 1
    # print the number of grades that were better than Average
    # Nothing is returned to main in this module
    print(str(count) + " grades were above average with their bottle drives. Good job Team!")

# This is my extra function
# It takes the two parallel lists and iterates through them
# For each loop, both the grade and number of cans is printed
# They use a common index to print correctly with the loop
def GradeScore(grade, cans):
    # Loop to print the information to the user
    for index in range(len(grade)):
        print("Grade:  ", "\t", grade[index])
        print("Bottles collected:  ", cans[index])

# Main module
def main():
    # Declare variable
    TotalCollected = int()
    AvgCollected = float()
    # Declare and load lists
    # They are parallel lists
    cans = [248, 379, 189, 457, 274, 532, 279, 296, 359]
    grade = ["Kindergarten", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"]
    # Call Function to get the total of cans collected
    # This fuction will return a variable
    # Then print the total collected
    TotalCollected = CanTotal(cans)
    print("The school collected a total of", TotalCollected, "cans for the drive!")
    # Call to the function that gets the average returned
    # This function will return a variable
    # Print the average from the function
    AvgCollected = AvgCans(TotalCollected)
    print("The school collected an average of", format(AvgCollected, '.0f'), "cans!")
    # This function does not return a variable
    # Output is done within the function
    AboveAvg(cans, AvgCollected)
    # Call to my selected extra function
    # This function will take the two parallel list
    # It will then print the grade and correspnding totals
    GradeScore(grade, cans)

# Call to main
main()