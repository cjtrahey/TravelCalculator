# Christopher-John Trahey
# Chapter 2 Homework - Travel Cost Calculator
# September 12, 2022
# This program takes in various values regarding travel distance and travel cost, and outputs the cost for the trip.
# Developed using Visual Studio code

# TASKS
# Total Miles Driven as an integer (totalMilesDriven)
# Gallons of gasoline bought as a decimal (gallonsGasBought) f function?
# Cost per gallon of gas in dollars + cents (costPerGallon)
# Formula 1: totalMilesDriven / gallonsGasBought
# Formula 2: gallonsGasBought / costPerGallon
# Display results
# Refer to Slide 36 for a template

# Define Variables
totalMilesDriven = int(input("Enter Miles Driven as an Integer: "))
gallonsGasBought = float(input("Enter Gallons of Gasoline Purchased as a Decimal: "))
costPerGallon = float(input("Enter Price Per Gallon in Dollars and Cents: "))

# Define Formulas
# Formula 1 - MPG Calculation
milesPerGallon = totalMilesDriven / gallonsGasBought
# Formula 2 - Trip Cost Calculation
tripCost = gallonsGasBought * costPerGallon

# Outputting Results

print("\nTravel Cost Calculator")
print("----------------------")
print("Numbers of Miles Travelled:", totalMilesDriven)
print("Numbers of Gallons Used:", gallonsGasBought)
print(f"Gas Mileage: {milesPerGallon:.2f} Miles Per Gallon")
print(f"Total trip Cost: ${tripCost:.2f}") 


# NOTE: The code above has been modified to only have two digits after the decimal point. 
# The original code that displays all of the information is as follows (commented out as to not interfere with current code):

# print(f"Gas Mileage: {milesPerGallon:.14f} Miles Per Gallon")
# print(f"Total trip Cost: ${tripCost:.14f}") 


