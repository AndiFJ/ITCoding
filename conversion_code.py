# Take kilos input from the user
kilo = float(input("Enter value in kilograms: "))
"""
Note: this also works ~~~
# user inputs their value
kilo_input = input("Enter value in kilograms: ")  

# capture the data entered user
kilo = float(kilo_input)
""" 

# conversion factor
conv_fac = 2.205 

# convert input to lb (pounds)
lb = kilo * conv_fac

# display the result
print('%0.2f kilograms is equal to %0.2f lb' %(kilo,lb))