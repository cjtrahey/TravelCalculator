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


