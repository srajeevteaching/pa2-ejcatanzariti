# Emily Catanzariti
# CS151, Dr. Rajeev
# 10/1/2021
# Programming Assignment Number 2
# Program Inputs: month and year
# Program Outputs: Amount of days in month

# state purpose
print("The purpose of this program is to find how many days are in a specific month.")
print("When asked to input the number of the month, 1 would be January, 2 for February... and 12 for December.")
print("If you input 2 for february, you will be prompted for the year.")

# ask user for number of month
month = int(input("Please enter the number of the month."))

# if month is february and year is leap year
if month == 2:
    year = int(input("Please enter the year in which you are trying to find."))
    if year % 100 == 0:
        if year % 400 == 0:
            days_in_month = 29
    elif year % 4 == 0:
        days_in_month = 29
    else:
        days_in_month = 28
    print("The amount of days in your month is:", days_in_month)
elif month == (1, 3, 5, 7, 8, 10, 12):
    days_in_month = 31
    print("The amount of days in your month is:", days_in_month)
elif month == (4, 6, 9, 11):
    days_in_month = 30
    print("The amount of days in your month is:", days_in_month)
else:
    print("Sorry, your input is not valid.")

print("Thank you for using this program!")
