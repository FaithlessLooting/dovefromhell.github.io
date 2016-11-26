import math
d=math.radians(int(input("please enter your distance")))
a=math.radians(int(input("please enter your angle")))
north= d*math.cos(a)*-1
east= d*math.sin(a)*-1
print(north)
print(east)
