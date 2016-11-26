print("welcome to moneystealerservices")


pounds = int(input("how many £ do you want to convert"))

print("you get €", pounds*1.36)    

euros = (pounds*1.36)
euros = int(euros)
euros = euros//1

notes1 = euros//50
euros = euros-(50*notes1)
notes2 = euros//20
euros = euros-(20*notes2)
notes3= euros//10
euros = euros-(10*notes3)

print("you get", notes1, "50€ notes")
print("you get", notes2, "20€ notes")
print("you get", notes3, "10€ notes")

input("press enter to close")
