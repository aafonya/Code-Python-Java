#Create a list#
doors = []

#Fullfill the list#
#False - Door is closed#
for i in range(0,101):
     doors.append(False)

# j - number of the cycle - e.g. in the 2nd cycle every second door will change#
# i - index of the door#
for j in range(1,101):
     for i in range(1,101):
         if i%j == 0:
             doors[i] = not doors[i]
            

      


print(doors)

#searching every True element (opened door) in the list and print their indexes#
for i in range(1,101):
    if doors[i] == True:
        print(i)


