print("welcome to fridgelift.com")
Lhight = float(input("how high is the lift in m  "))
Lwidth = float(input("how wide is the lift in m  "))
Ldepth = float(input("how deep is the lift in m  "))
Fhight = float(input("how high is the fridge in m  "))
Fwidth = float(input("how wide is the fridge in m  "))
Fdepth = float(input("how deep is the fridge in m  "))

leftup = Lhight-Fhight
leftside = Lwidth-Fwidth
leftfront = Ldepth-Fdepth

if leftup>0 and leftside>0 and leftfront>0:
    print("you have", leftup*leftside*leftfront,"m^3 space left")
elif leftup<0:
    print("you don't have enough room")
elif leftside<0:
    print("you don't have enough room")
else:
    print("you dont have enough room")
