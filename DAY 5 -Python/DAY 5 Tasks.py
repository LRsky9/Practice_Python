#Task1



#Task2

mynum = (input("Enter a number "))
try:
    mynum = int(mynum)
    mynum = float(mynum)
    if mynum %2 == 0: #how we find even numbers
        print("the numbers is even")
    else:
        print("the number is odd")
except:
    print("not a number, try again")




#Task 3
namesList = ['bob','Jim','Harold']
print("enter three names please")
toBeAdded = input("Name 1 ")
namesList.append(toBeAdded)
print(namesList)
toBeAdded = input("Name 2 ")
namesList.append(toBeAdded)
print(namesList)
toBeAdded = input("name 3 ")
namesList.append(toBeAdded)
print(namesList)
