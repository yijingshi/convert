miles = 0
i= 0
while i<3:
    if miles >= 0 :
        miles = float(input('William, tell me how many miles you want to converted to kilometer: '))
        mileTokm = miles*1.6
        print (miles, "miles is equal to", mileTokm, "kilometer. Isn't that amazing!")
        i=i+1
    else:
        print ("invalid number")
        exit()

gallons = 0
i=0
while i<3:
    if gallons >= 0:
        gallons = float(input('William, tell me how many gallons you want to converted to liters: '))
        galTolit = gallons*3.9
        print (gallons, "gallons is equal to", galTolit, "liters. Isn't that amazing!")
        i=i+1
    else:
        print ("invalid number")
        exit()

pounds = 0
i = 0
while i<3:
    if pounds >= 0:
        pounds = float(input('William, tell me how many pounds you want to converted to kilograms: '))
        lbTokg = pounds*0.45
        print (pounds, "pounds is equal to", lbTokg, "kilograms. Isn't that amazing!")
        i = i+1
    else:
        print ("invalid number")
        exit()

inches = 0
i=0
while i<3:
    if inches >= 0:
        inches = float(input('William, tell me how many inches you want to converted to centimeters: '))
        inTocm = inches*2.54
        print (inches, "inches is equal to", inTocm, "centimeters. Isn't that amazing!")
        i = i+1
    else:
        print ("invalid number")
        exit()

fahrenheit = 0
i= 0
while i<3:
    if fahrenheit < 1000:
        fahrenheit = float(input('William, tell me how many fahrenheit you want to converted to celsius: '))
        fToc = (fahrenheit -32)*5/9
        print (fahrenheit, "fahrenheit is equal to", fToc, "celsius. Isn't that amazing!")
    else:
        print ("invalid number")
        exit()

exit()
