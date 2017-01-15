# convert -1
For this portion of the lab you will design the solution so that you perform some conditional tests. For this lab:
-You will validate input to ensure that the user enters inputs within a certain range or larger than a certain minimum value. You will validate the inputs as follows:
-user cannot enter a negative number for:
Miles to kilometers; Gallons to liters; Pounds to kilograms; Inches to centimeters
-user cannot enter a value above 1000 degrees for Fahrenheit to Celsius
-If the user enters an invalid value, then the program will issue an error message and terminate immediately. (Do NOT accept further data).

# convert - 2


For this portion of the lab, you will reuse the program you wrote in File 1. Redesign the solution so that some portions of the code are repeated. In lab 4 you validated input to ensure that the user entered inputs within certain values. If the user entered an invalid value, the program terminated. Now you will add a loop such that the user gets three chances to enter a valid value. If the user enters an invalid value more than three times in a row, the program should issue an error message and terminate

# convert -3

For this portion of the lab, you will reuse the program you wrote in File 2. Redesign the solution using functions. For this lab:
1. You will define a function named main().
2. You will get input in the main function and pass it to the following functions:
a. milesT oKm() b. FahT oCel()
c. GalT oLit()
d. PoundsToKg() e. InchesT oCm()
3. Each function will require that you have a local variable to store the result of the calculation. This result will then be displayed using the print statement from within the function.

# convert -4
For this portion of the lab, you will reuse the program you wrote in File 3. Redesign the solution in the following manner:
1. All the functions used are value-returning functions.
2. Put the functions in an external module and let the main program import the module.
