p = float(input("Enter principle amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter the time period: "))

amount = p * (1 + (r/100)) ** t
CI = amount - p

print("The compound interest on the given principle Rs.",p," ,rate",r,"% , and for the given time period",t,
      " years is ",CI)