#*****************************************************************************
# Author:       	AJ Alstadt
# Assignment:       Assignment 1
# Date:         	1/26/2025
# Description:  	This program prompts a user to enter an amount of grams 
#                   and converts the number into kilograms.
# Input:        	Amount of grams
# Output:       	The same amount, displayed in kilograms
# Sources:      	LJ helped by showing me his project. Assignment 1 
#                   instructions helped with formatting.
# Notes:            Created in Github Codespaces, since Replit isn't 
#                   recommended
#*****************************************************************************
# Neither comments nor code should be wider than 79 characters.
# The lines of asterisks above are 79 characters long for easy reference.

# defines main 
def main():
    # Assigns grams a value
    # Stops the program and asks for a floating point number as input
    grams =  float(input("Please enter an amount in grams:"))

    # Converts grams to kilograms
    kilograms = grams / 1000
    
    # Displays the output message 
    print (grams, "grams is equivalent to", kilograms, "kilograms")

# Runs the main program
main()