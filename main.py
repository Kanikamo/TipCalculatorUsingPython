TotalofBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
PercentofTip = float(input("What percent of the total would you like to tip?: "))
TipPerPerson = float(((TotalofBill * (PercentofTip / 100)) / numberOfPeople))
Total = TipPerPerson + (TotalofBill/numberOfPeople) 
print("Tip per person", TipPerPerson)
print("Your total: ", Total)
