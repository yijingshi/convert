# Convert -1
For this portion of the lab you will design the solution so that you perform some conditional tests. For this lab:
-You will validate input to ensure that the user enters inputs within a certain range or larger than a certain minimum value. You will validate the inputs as follows:
-user cannot enter a negative number for:
Miles to kilometers; Gallons to liters; Pounds to kilograms; Inches to centimeters
-user cannot enter a value above 1000 degrees for Fahrenheit to Celsius
-If the user enters an invalid value, then the program will issue an error message and terminate immediately. (Do NOT accept further data).

# Convert - 2


For this portion of the lab, you will reuse the program you wrote in File 1. Redesign the solution so that some portions of the code are repeated. In lab 4 you validated input to ensure that the user entered inputs within certain values. If the user entered an invalid value, the program terminated. Now you will add a loop such that the user gets three chances to enter a valid value. If the user enters an invalid value more than three times in a row, the program should issue an error message and terminate

# Convert -3

For this portion of the lab, you will reuse the program you wrote in File 2. Redesign the solution using functions. For this lab:
1. You will define a function named main().
2. You will get input in the main function and pass it to the following functions:
a. milesToKm() 
b. FahToCel()
c. GalToLit()
d. PoundsToKg()
e. InchesToCm()
3. Each function will require that you have a local variable to store the result of the calculation. This result will then be displayed using the print statement from within the function.

# Convert -4
For this portion of the lab, you will reuse the program you wrote in File 3. Redesign the solution in the following manner:
1. All the functions used are value-returning functions.
2. Put the functions in an external module and let the main program import the module.

# Convert -5
1. Create a menu and ask the user which of the following conversions they wish to perform:
a. Miles to kilometers
b. Gallons to liters
c. Pounds to kilograms
d. Inchestocentimeters
e. Fahrenheit to Celsius
2. Your program must raise an exception if the user chooses any item not on the menu presented. Along with raising an exception, write the code to handle this exception.

3. Once the user has chosen a menu item the program should:
a. Ask the user for a value to convert. Refer to the input validations in Lab 4. Your
program must raise and exception, and handle the exception, if an input errors
occurs.
b. Performtheconversionandwritetheoriginalvalue,theoriginalunit,theconverted

value, and the converted unit to an output file named conversions.txt.
c. Repeat steps a and b 10 times (in a loop).
