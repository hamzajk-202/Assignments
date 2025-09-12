print ('''Welcome to Python Programming!''')

a = float(input ( 'Enter 1st number: '))
b = float(input ( 'Enter 2nt number: '))

z = a
a = b
b = z
print("After Swapping: ")
print('First number: ',a)
print('Second number: ',b)

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 1.8 + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")