
conversionFile = open('conversions.txt', 'w')
def main():
    try:
        i = 0

        while i <10:
            menu()
            choice  = raw_input("Pick a number: ")
            if choice == "a":
                count = 0
                miles = 0
                while count <3:
                    if miles >= 0 :
                        miles = input('William, tell me how many miles you want to converted to kilometer: ')
                        mileTokm = miles*1.6
                        print (miles, "miles is equal to", format(mileTokm,'.2f'), "kilometer. Isn't that amazing!")
                        conversionFile.write(format(miles, '.2f')+ " Miles were converted to " + format(mileTokm, '.2f')+ " kilometers" + '\n')

                        count = count+1

                    else:
                        print ("invalid number")
                        exit()

            elif choice == "b":
                count = 0
                gallons = 0
                while count<3:
                    if gallons >= 0:
                        gallons = input('William, tell me how many gallons you want to converted to liters: ')
                        galTolit = gallons*3.9
                        print (gallons, "gallons is equal to", format(galTolit,'.2f'), "liters. Isn't that amazing!")
                        conversionFile.write(format(gallons, '.2f')+ " gallons were converted to " + format(galTolit, '.2f')+ "liters" + '\n')

                        count = count+1
                    else:
                        print ("invalid number")
                        exit()

            elif choice == "c":
                count = 0
                pounds = 0
                while count<3:
                    if pounds >= 0:
                        pounds = input('William, tell me how many pounds you want to converted to kilograms: ')
                        lbTokg = pounds*0.45
                        print (pounds, "pounds is equal to", format(lbTokg,'.2f'), "kilograms. Isn't that amazing!")
                        conversionFile.write(format(pounds, '.2f')+ " Pounds were converted to " + format(lbTokg, '.2f')+ "kilograms" + '\n')

                        count = count+1
                    else:
                        print ("invalid number")
                        exit()

            elif choice == "d":
                count = 0
                inches = 0
                while count<3:
                    if inches >= 0:
                        inches = input('William, tell me how many inches you want to converted to centimeters: ')
                        inTocm = inches*2.54
                        print (inches, "inches is equal to", format(inTocm,'.2f'), "centimeters. Isn't that amazing!")
                        conversionFile.write(format(inches, '.2f')+ " inches were converted to " + format(inTocm, '.2f')+ " centimeters" + '\n')

                        count = count+1
                    else:
                        print ("invalid number")
                        exit()

            elif choice == "e":
                count = 0
                fahrenheit = 0
                while count<3:
                    if fahrenheit < 1000:
                        fahrenheit = input('William, tell me how many fahrenheit you want to converted to celsius: ')
                        fToc = (fahrenheit -32)*5/9
                        print (fahrenheit, "fahrenheit is equal to", format(fToc ,'.2f'), "celsius. Isn't that amazing!")
                        conversionFile.write(format(fahrenheit, '.2f')+ " fahrenheit were converted to " + format(fToc, '.2f')+ " celsius" + '\n')

                        count = count+1
                    else:
                        print ("invalid number")
                        exit()
            else:
                print('\n\nInvalid Selection')
                exit()

            i = i+1
    except ValueError:
    		# most common error from testing was Value Error..
    	print('\n\n\n***** PLEASE MAKE A VALID SELECTION *****')

def menu():
            print "a. Miles to kilometers"
            print "b. Gallons to liters"
            print "c. Pounds to kilograms"
            print "d. Inchestocentimeters"
            print "e. Fahrenheit to Celsius"

main ()
