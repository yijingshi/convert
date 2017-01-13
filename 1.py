miles = float(input('William, tell me how many miles you want to converted to kilometer: '))
if miles >= 0 :
    mileTokm = miles*1.6
    print (miles, "miles is equal to", mileTokm, "kilometer. Isn't that amazing!")
else:
    print ("invalid number")
    exit()

gallons = float(input('William, tell me how many gallons you want to converted to liters: '))
if gallons >= 0:
    galTolit = gallons*3.9
    print (gallons, "gallons is equal to", galTolit, "liters. Isn't that amazing!")
else:
    print ("invalid number")
    exit()

pounds = float(input('William, tell me how many pounds you want to converted to kilograms: '))
if pounds >= 0:
    lbTokg = pounds*0.45
    print (pounds, "pounds is equal to", lbTokg, "kilograms. Isn't that amazing!")
else:
    print ("invalid number")
    exit()

inches = float(input('William, tell me how many inches you want to converted to centimeters: '))
if inches >= 0:
    inTocm = inches*2.54
    print (inches, "inches is equal to", inTocm, "centimeters. Isn't that amazing!")
else:
    print ("invalid number")
    exit()

fahrenheit = float(input('William, tell me how many fahrenheit you want to converted to celsius: '))
if fahrenheit < 1000:
    fToc = (fahrenheit -32)*5/9
    print (fahrenheit, "fahrenheit is equal to", fToc, "celsius. Isn't that amazing!")
else:
    print ("invalid number")
    exit()

exit()
