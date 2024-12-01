#Step 1: Input the measurement in feet
feet = float(input("Enter the measurement in feet: "))

#Step 2: Conversion factor
#1foot= 12×2.54=30.48centimeters
conversion_factor = 30.48

# Step 3: Convert feet to centimeters
centimeters = feet * conversion_factor

# Step 4: Display the result
print("Number of feets:",feet)
print("Foot into centimeter:",conversion_factor)
print(feet, "feet is equal to", centimeters, "centimeters.")