#Question 3
#Write a function `convert_temperature(temp, scale)` that:
#1. Takes a temperature value and a scale ("C" for Celsius, "F" for Fahrenheit) as inputs.
#2. Converts the temperature to the other scale.
#3. Returns the converted temperature.
#4. Display the converted temperature

#Code:

def convert_temperature(temp, scale):
    if scale == "C":
        # Convert from Celsius to Fahrenheit
        converted_temp = (temp * 9/5) + 32
        print(f"{temp} degrees Celsius is equal to {converted_temp:.2f} degrees Fahrenheit.")
    elif scale == "F":
        # Convert from Fahrenheit to Celsius
        converted_temp = (temp - 32) * 5/9
        print(f"{temp} degrees Fahrenheit is equal to {converted_temp:.2f} degrees Celsius.")
    else:
        print("Invalid scale. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        return None
    
    return converted_temp

# Example usage
temp = float(input("Enter the temperature value: "))
scale = input("Enter the scale ('C' for Celsius, 'F' for Fahrenheit): ").upper()
convert_temperature(temp, scale)