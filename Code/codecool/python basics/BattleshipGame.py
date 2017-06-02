import os 

<<<<<<< HEAD
shipnumber = 0
shipsize = 0
shipdirection = 0

shipsizes1 = []
shipsizes2 = []

coord_abc = ["A","B","C","D","E","F","G","H","I","J"]
coord_numbers = [1,2,3,4,5,6,7,8,9,10]

=======
>>>>>>> 803965605f7f1d767c9c08169ab36e92dbe83e9c
table1 = [[0,0,0,0,0,0,0,0,0,0],  #for store the coordinates of the ships of the first player
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

table2 = [[0,0,0,0,0,0,0,0,0,0], #for store the coordinates of the ships of the second player
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

<<<<<<< HEAD
#-------------------------------------------------------------------------------------------------------------------
#Placing the ships
#-----------------------------------------------------------------------------------------------------------------------------


# player1 placing the ships in the table1
def makingships1():
     
     global shipnumber
     global shipsize
     global shipdirection

     os.system('cls' if os.name == 'nt' else 'clear')
     print("Hello first player! Now you can place 9 ships to your table")
    
     while shipnumber < 7: 
         shipsize = int(input("How big ship do you want to make? 1,2 or 3"))
         
         if shipsize_check1(shipsize) == False:
             print("You already have two " + "%2d" % shipsize + " unit long ships!")
             input("Press Enter to continue")
             continue

         if shipsize ==1:
             print("Let's make your " + "%d" % shipsize + " units long ships" )
             printthetableplayer1ships()

             print("Where to begin the ship? ") 
             column=str(input("Choose the first coordinate (e.g. A): " + " "))
             if convert(column) == False:
                 print("Please choose a character from A-J")
                 input("Press Enter to continue")
                 continue
             else:
                 column = convert(column)

             row =int(input("Choose the second coordinate (e.g. 1): "+" "))

             if check1(row,column, shipsize, shipdirection) == False:
                 continue
             table1[row-1][column-1] = 1
             shipnumber = shipnumber + 1

             os.system('cls' if os.name == 'nt' else 'clear')
             printthetableplayer1ships()

=======
# player1 placing the ships in the table1
def makingships1():
     os.system('cls' if os.name == 'nt' else 'clear')
     print("Hello first player! Now you can place 9 ships to your table")
     for shipnumber in range(0,8): 
         shipsize = int(input("How big ship do you want to make? 1,2 or 3"))
         if shipsize ==1:
             print("Let's make your " + "%d" % shipsize + " units long ships" )
             printthetableplayer1ships()
             print("Where to begin the ship? ")                                            
             x=int(input("Choose the first coordinate: "))
             y=int(input("Choose the second coordinate: "))
             table1[x-1][y-1] = 1
             printthetableplayer1ships()
>>>>>>> 803965605f7f1d767c9c08169ab36e92dbe83e9c
         if shipsize >1:
             shipdirection = int(input("Horizontally (0) or vertically (1)?  ")) 
             print("Let's make your " + "%d" % shipsize + " units long ships" )
             printthetableplayer1ships()
<<<<<<< HEAD

             print("Where to begin the ship? ")                                            
             column=str(input("Choose the first coordinate(e.g. A): " + " "))
             if convert(column) == False:
                 print("Please choose a character from A-J")
                 input("Press Enter to continue")
                 continue
             else:
                 column = convert(column)


             row=int(input("Choose the second coordinate: "))

             if check1(row,column,shipsize, shipdirection) == False:
                 continue

             if shipdirection == 0:
                  for h in range(1,shipsize+1):                                 #for making as many shipunit as big ship is making in the cycle
                       table1[row-1][column+h-2] = 1
                       shipnumber = shipnumber +1
                       os.system('cls' if os.name == 'nt' else 'clear')
                       printthetableplayer1ships()
             
             if shipdirection == 1:
                  for h in range(1,shipsize+1):                                 #for making as many shipunit as big ship is making in the cycle
                       table1[row+h-2][column-1] = 1
                       shipnumber = shipnumber +1
                       os.system('cls' if os.name == 'nt' else 'clear')
                       printthetableplayer1ships()  
                                      
# player2 placing the ships in his table2
def makingships2():

     global shipnumber
     global shipsize
     global shipdirection

     os.system('cls' if os.name == 'nt' else 'clear')
     print("Hello second player! Now you can place 9 ships to your table")

     while shipnumber < 7: 
         shipsize = int(input("How big ship do you want to make? 1,2 or 3"))

         if shipsize_check2(shipsize) == False:
             print("You already have two " + "%2d" % shipsize + " unit long ships! Choose again!")
             input("Press Enter to continue")
             continue
         
         if shipsize ==1:
             print("Let's make your " + "%d" % shipsize + " units long ships" )
             printthetableplayer2ships()
             
             print("Where to begin the ship? ")                                            
             column=str(input("Choose the first coordinate (e.g. A): " + " "))
             if convert(column) == False:
                 print("Please choose a character from A-J")
                 input("Press Enter to continue")
                 continue
             else:
                 column = convert(column)
             
             row=int(input("Choose the second coordinate(e.g. 1): "+" "))
             
             if check2(row,column, shipsize, shipdirection) == False:
                 continue

             table2[row-1][column-1] = 1
             shipnumber = shipnumber + 1
             
             os.system('cls' if os.name == 'nt' else 'clear')
             printthetableplayer2ships()
         
=======
             print("Where to begin the ship? ")                                            
             x=int(input("Choose the first coordinate: "))
             y=int(input("Choose the second coordinate: "))
             if shipdirection == 0:
                  for h in range(1,shipsize+1):                                 #for making as many shipunit as big ship is making in the cycle
                       table1[x-1][y+h-2] = 1
                       os.system('cls' if os.name == 'nt' else 'clear')
                       printthetableplayer1ships()
             if shipdirection == 1:
                  for h in range(1,shipsize+1):                                 #for making as many shipunit as big ship is making in the cycle
                       table1[x+h-2][y-1] = 1
                       os.system('cls' if os.name == 'nt' else 'clear')
                       printthetableplayer1ships()                                       
      


# player2 placing the ships in his table2
def makingships2():
     os.system('cls' if os.name == 'nt' else 'clear')
     print("Hello second player! Now you can place 9 ships to your table")
     for shipnumber in range(0,8): 
         shipsize = int(input("How big ship do you want to make? 1,2 or 3"))
         if shipsize ==1:
             print("Let's make your " + "%d" % shipsize + " units long ships" )
             printthetableplayer2ships()
             print("Where to begin the ship? ")                                            
             x=int(input("Choose the first coordinate: "))
             y=int(input("Choose the second coordinate: "))
             table2[x-1][y-1] = 1
             printthetableplayer1ships()
>>>>>>> 803965605f7f1d767c9c08169ab36e92dbe83e9c
         if shipsize >1:
             shipdirection = int(input("Horizontally (0) or vertically (1)?  ")) 
             print("Let's make your " + "%d" % shipsize + " units long ships" )
             printthetableplayer2ships()
<<<<<<< HEAD
             
             print("Where to begin the ship? ")                                            
             column=str(input("Choose the first coordinate(e.g. A): " + " "))
             if convert(column) == False:
                 print("Please choose a character from A-J")
                 input("Press Enter to continue")
                 continue
             else:
                 column = convert(column)

             row=int(input("Choose the second coordinate: "))

             if check2(row,column,shipsize,shipdirection) == False:
                 continue

             if shipdirection == 0:
                  for h in range(1,shipsize+1):                                 #for making as many shipunit as big ship is making in the cycle
                       table2[row-1][column+h-2] = 1
                       shipnumber = shipnumber +1
                       os.system('cls' if os.name == 'nt' else 'clear')
                       printthetableplayer2ships()
             
             if shipdirection == 1:
                  for h in range(1,shipsize+1):                                 #for making as many shipunit as big ship is making in the cycle
                       table2[row+h-2][column-1] = 1
                       shipnumber = shipnumber +1
                       os.system('cls' if os.name == 'nt' else 'clear')
                       printthetableplayer2ships()                                       

def convert(firstcoordinate):
    global coord_abc
    global coord_numbers

    for i in range (0, len(coord_abc)):
        if coord_abc[i] == firstcoordinate:
            firstcoordinate = int(coord_numbers[i])
            return firstcoordinate
        
    return False
        
         
        
def check1(x,y,shipsize,shipdirection):
    global shipnumber
    if shipsize == 1:
        if table1[x-1][y-1] == 1:
            print("Oops, it looks if you already had a ship right here. So please try again!")
            input("Press enter to try again")
            return False
        else:
            return True
    if shipsize > 1:
        if shipdirection == 0:
                  for h in range(1,shipsize+1):                                 
                       if table1[x-1][y+h-2] == 1:
                            print("Oops, it looks if you already had a ship right here. So please try again!")
                            input("Press enter to try again")
                            return False 
                  return True
                        
        if shipdirection == 1:
                  for h in range(1,shipsize+1): 
                      if table1[x+h-2][y-1] == 1:
                          print("Oops, it looks if you already had a ship right here. So please try again!")
                          input("Press enter to try again")
                          return False 
                  return True                                
                        
def check2(x,y,shipsize,shipdirection):
    global shipnumber
    if shipsize == 1:
        if table2[x][y] == 1:
            print("Oops, it looks if you already had a ship right here. So please try again!")
            input("Press enter to try again")
            return False
        else:
            return True
    if shipsize > 1:
         if shipdirection == 0:
             for h in range(1,shipsize+1):
                 if table1[x-1][y+h-2] == 1:
                     print("Oops, it looks if you already had a ship right here. So please try again!")
                     input("Press enter to try again")
                     return False    
             return True
                                             
         if shipdirection == 1:
                  for h in range(1,shipsize+1): 
                      if table1[x+h-2][y-1] == 1:
                          print("Oops, it looks if you already had a ship right here. So please try again!")
                          input("Press enter to try again")
                          return False    
                  return True   

def shipsize_check1(shipsize):
    global shipsizes1
    shipsizes1.append(shipsize)

    shipfound = 0
    for i in range (0, len(shipsizes1)):
        if shipsize == shipsizes1[i]:
            shipfound = shipfound + 1
            if shipfound > 2:
                return False
    
def shipsize_check2(shipsize):
    global shipsizes2
    shipsizes2.append(shipsize)

    shipfound = 0
    for i in range (0, len(shipsizes2)):
        if shipsize == shipsizes2[i]:
            shipfound = shipfound + 1
            if shipfound > 2:
                return False

        




=======
             print("Where to begin the ship? ")                                            
             x=int(input("Choose the first coordinate: "))
             y=int(input("Choose the second coordinate: "))
             if shipdirection == 0:
                  for h in range(1,shipsize+1):                                 #for making as many shipunit as big ship is making in the cycle
                       table2[x-1][y+h-2] = 1
                       os.system('cls' if os.name == 'nt' else 'clear')
                       printthetableplayer2ships()
             if shipdirection == 1:
                  for h in range(1,shipsize+1):                                 #for making as many shipunit as big ship is making in the cycle
                       table2[x+h-2][y-1] = 1
                       os.system('cls' if os.name == 'nt' else 'clear')
                       printthetableplayer2ships()                                       
     
>>>>>>> 803965605f7f1d767c9c08169ab36e92dbe83e9c

# printing the table1 with the ships
def printthetableplayer1ships():
   print("   ABCDEFGHIJ")
   for row in range(0,10):
       print( "%2d " % (row+1), end= "")
       for column in range(0,10):
              if table1[row][column] == 0:
                  print("~", end= "")
              if table1[row][column] == 1:
                  print("O", end= "")
              if table1[row][column] == 2:
                  print("X", end= "")
              if table1[row][column] == 3:
                  print("*", end= "")
       print("") # print a newline char

# printing the table2 with the ships
def printthetableplayer2ships():
   print("   ABCDEFGHIJ")
   for row in range(0,10):
       print( "%2d " % (row+1), end= "")
       for column in range(0,10):
              if table2[row][column] == 0:
                  print("~", end= "")
              if table2[row][column] == 1:
                  print("O", end= "")
              if table2[row][column] == 2:
                  print("X", end= "")
              if table2[row][column] == 3:
                  print("*", end= "")
       print("") # print a newline char

# printing the table2 with the hits and/or misses but hidding the ships
def printthetableplayer1shoots():
   print("   ABCDEFGHIJ")
   for row in range(0,10):
       print( "%2d " % (row+1), end= "")
       for column in range(0,10):
              if table2[row][column] == 0:
                  print("~", end= "")
              if table2[row][column] == 1:
                  print("~", end= "")
              if table2[row][column] == 2:
                  print("X", end= "")
              if table2[row][column] == 3:
                  print("*", end= "")
       print("") # print a newline char

# printing the table1 with the hits and/or misses but hidding the ships
def printthetableplayer2shoots():
   print("   ABCDEFGHIJ")
   for row in range(0,10):
       print( "%2d " % (row+1), end= "")
       for column in range(0,10):
              if table1[row][column] == 0:
                  print("~", end= "")
              if table1[row][column] == 1:
                  print("~", end= "")
              if table1[row][column] == 2:
                  print("X", end= "")
              if table1[row][column] == 3:
                  print("*", end= "")
       print("") # print a newline char

<<<<<<< HEAD

#---------------------------------------------------------------------------------------------------------
#Shooting
#------------------------------------------------------------------------------------------------------------

=======
>>>>>>> 803965605f7f1d767c9c08169ab36e92dbe83e9c
# player1 shoot in table2
def shootplayer1():
    print("")
    print("PLAYER1")
    printthetableplayer1shoots()
    a = int(input("First shoot1 coordinate"))
    b = int(input("Second shot1 coordinate"))

    if table2[a-1][b-1] == 1:
        table2[a-1][b-1] = 2
    if table2[a-1][b-1] == 0:
        table2[a-1][b-1] = 3
    os.system('cls' if os.name == 'nt' else 'clear')
    printthetableplayer1shoots()
    e = counthit1()
    print("PLAYER1 SCORE:", e)
    if e == 12:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("***PLAYER1 WINS***")
        return True

# player2 shoot in table1
def shootplayer2():
    print("")
    print("PLAYER2")
    printthetableplayer2shoots()
    a = int(input("First shot2 coordinate"))
    b = int(input("Second shot2 coordinate"))

    if table1[a-1][b-1] == 1:
        table1[a-1][b-1] = 2
    if table1[a-1][b-1] == 0:
        table1[a-1][b-1] = 3
    os.system('cls' if os.name == 'nt' else 'clear')
    printthetableplayer2shoots()
    u = counthit2()
    print("PLAYER2 SCORE:", u)
    if u == 12:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("***PLAYER2 WINS***")
        return True

# counts the scores of player1
def counthit1():
    q = 0
    for a in range(0, 10):
        table2[a].count(2)
        q = q + table2[a].count(2)
    return q

# counts the scores of player2
def counthit2():
    r = 0
    for z in range(0, 10):
        table1[z].count(2)
        r = r + table1[z].count(2)
    return r
<<<<<<< HEAD
#---------------------------------------------------------------------------------------------------------------- 

#-----------------------------------------------------------------------------------------------------------------------------


=======
>>>>>>> 803965605f7f1d767c9c08169ab36e92dbe83e9c

print("Hello, let's begin the play.")
print("Someone has to go out or close his/her eyes while the other player places his/her ships in the table")
input("Enter if you're ready")

<<<<<<< HEAD
shipnumber = 0
=======
>>>>>>> 803965605f7f1d767c9c08169ab36e92dbe83e9c
makingships1()
print("Now you're ready, it's the other player's turn")
input("Enter to continue with the second player")
os.system('cls' if os.name == 'nt' else 'clear')

<<<<<<< HEAD
shipnumber = 0
=======
>>>>>>> 803965605f7f1d767c9c08169ab36e92dbe83e9c
makingships2()
os.system('cls' if os.name == 'nt' else 'clear')

# gives 100 possible shoots and if player1 or player2 reach 12 score then end the game
shootnum = 0
while(shootnum<=100):
    k = shootplayer1()
    if k == True:
        break
    l = shootplayer2()
    if l == True:
        break
<<<<<<< HEAD
    shootnum = shootnum + 1

userInput = 0
while True:
  try:
     userInput = int(input("Enter a number to exit:"))
  except ValueError:
     print("error, error, error")
     continue
  else:
     print("bye-bye")
  exit() 
=======
    shootnum = shootnum + 1 
>>>>>>> 803965605f7f1d767c9c08169ab36e92dbe83e9c
