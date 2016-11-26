age=input("how old are you")
age=float(age)
if age > 18:
    print("you can vote as long as it isnt ukip")
else:
    untilv=18-age
    print("you can vote in", untilv, "years")
