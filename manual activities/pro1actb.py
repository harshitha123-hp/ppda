def temperature_converter():
    print("Temperature Converter")
    print("Select conversion:")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        print(f"{celsius}°C = {fahrenheit}°F = {kelvin}K")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{fahrenheit}°F = {celsius}°C = {kelvin}K")
    elif choice == '3':
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{kelvin}K = {celsius}°C = {fahrenheit}°F")
    else:
        print("Invalid input, please enter a number between 1 and 3.")

# Run the temperature converter
temperature_converter()
