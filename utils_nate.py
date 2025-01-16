"""
Module: utils_nate

Purpose: To gain familiarity with variables and functions in Python

Description: 
This module will import a statistics library, create variables and lists, use the statistics library and run functions.  This is basic programming format to get familiar with the various
data types and syntax of python. 

Author: Nate Sloss


"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
has_international_clients: bool = True
is_pet_friendly: bool = False

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
years_in_operation: int = 10
age: int = 66

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_client_satisfaction: float = 4.7
average_student_gpa: float = 3.1

# declare a list of strings
# TODO: Add or replace this with your own list  
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
classes_available: list = ["Calculus","English","Biology"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
daily_temperatures_farenheit: list = [19.2, 23.5, 33.1, 28.9, 35.7]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_score: float = min(daily_temperatures_farenheit)  
max_score: float = max(daily_temperatures_farenheit)  
mean_score: float = statistics.mean(daily_temperatures_farenheit)  
stdev_score: float = statistics.stdev(daily_temperatures_farenheit)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Is Pet Friendly:  {is_pet_friendly}
Age:         {age}
Classes Available:             {classes_available}
Daily Temp Farenheit: {daily_temperatures_farenheit}
Minimum Temperature: {min_score}
Maximum Temperature: {max_score}
Mean Temperature: {mean_score:.2f}
Standard Deviation of Temperature: {stdev_score:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
