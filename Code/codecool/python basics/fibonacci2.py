Fn2 = 0
Fn1 = 1

i = 1
j = int(input())

print (Fn2)
print (Fn1)

while i <= j-2:
   Fn1 = Fn1 + Fn2
   print ( str(Fn1) )
   i = i+1
   if i <= j-2:
    Fn2 = Fn2 + Fn1
    print ( str(Fn2))
    i = i+1
