# if , else , elif = else if
print(2 == 2)
print(3 != 3)
print(4 > 3 & 8 == 8)
print( "hello" == "hello")
print('dog' != 'cat')

name = input("enter your name: ") #user se input aese lete
if name == "Mary":
    print("Hello Mary")
    password = input('enter your password: ')
    if password == "blackout":
        print("correct password")
    else:
        print("incorrect password")
else:
    print('acces denied, you are not mary')

number = int(input("entr a number: "))
number = float(input("enter a decimal no: "))
x, y = input("enter 2 numbers : ").split()
print('first number: ',x, "the second number is ", y)


name = input("pls enter name")
age = int(input('enter ur age'))
    
if name == "alice":
     print('hi alice')
elif age < 12:
    print('u are not alice')

def get_remainder(x, y):
 
  if x == 0 or y == 0 or x == y:
    remainder = 0
  else:
    remainder = (x % y) / y
  return remainder
print(get_remainder(10, 3))

        
      

