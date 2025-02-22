#calculating the area of triangle by creating a function
def area_triangle(base ,height):
    return base*height/2 # return krega area of triang
#intializing values in the functions
area_a = area_triangle(6,4) 
area_b = area_triangle(7,3)

#calc the sum of the triangle
sum = area_a + area_b
print("the sum of both area is: " + str(sum))
print("the area of triangle a is " + str(area_a) + " area of b is " + str(area_b))

# function to return hours min and seconds
def convert_seconds(seconds):
    hours = seconds // 3600 # // first div then floors down the value 
    minutes = (seconds - hours * 3600) // 60 # formula of mintues
    remaining_seconds =  seconds - hours * 3600 - minutes * 60 
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes,seconds)

#simple calculate function
def calculate(d):
    q = 23
    z = d * q
    print(z)
    
calculate(3)

def username():
    user_input = input("pls enter username")
    if len(user_input) < 3:
        print("pls enter correct username")
    else: 
        input(print("Username is: "))
