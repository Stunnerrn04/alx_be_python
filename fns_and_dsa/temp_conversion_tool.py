# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_FREEZING_POINT = 32
CELSIUS_FREEZING_POINT = 0

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_FREEZING_POINT
    return (fahrenheit - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR, CELSIUS_FREEZING_POINT
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_FREEZING_POINT

def main():
    """
    Main function to handle user interaction and perform temperature conversions.
    """
    try:
        # Prompt the user for temperature input and unit
        temperature = float(input("Enter the temperature: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            # Convert from Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        elif unit == 'F':
            # Convert from Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()