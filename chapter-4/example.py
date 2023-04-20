#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).

hrs = input("hours done:")
rte = input("hourly rate:")

nhts = float(hrs)
nrte = float(rte)

if nhts > 40:
    #print("overtime")
    ovpay = (nhts - 40) * (nrte * 0.5)
    pay = (nhts * nrte) + ovpay
    print(pay)
else:
    #print("regular")
    pay = nhts * nrte