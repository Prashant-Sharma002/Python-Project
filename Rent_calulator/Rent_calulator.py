# Needs from the User input ......
# Total roomRent.............
# Total foodOrderedAmount...........
# how electroicUnits..........
# Total members in your room..........


roomRent = int(input("Enter  Total of  Your Room Rent= "))
foodOrderedAmount = int(input("Enter Total of  Your Food Ordered Amounts= "))
electroicUnits = int(input("Enter Total of  Your  Electronic Units= "))
charge_per_units = int(input("Enter Your Charge Pre Unit= "))
memebers = int(input("How many member living in your room= "))

totalBill=  electroicUnits * charge_per_units
finalResult= (foodOrderedAmount+roomRent+totalBill) // memebers 


# Output
# Total amount paying perMember living in room.............

print("Each Member will pay= ", finalResult )