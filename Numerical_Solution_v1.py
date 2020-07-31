#List definitions for global access
x_list = []
fx_list = []
co_ordinate = []
left_half_fx = []
right_half_fx = []
left_half_x = []
right_half_x = []
fX = []
non_linear_constants = []

#Input from User
input_loop= 0  
input_message = int(input("How many inputs would you like to take: "))
while input_loop < input_message:
    print("Value for Input: " + str(input_loop + 1))
    x_value = int(input("Enter value for x: "))
    x_list.append(x_value)
    fx_value = int(input("Enter value for f(x): "))
    fx_list.append(fx_value)
    co_ordinate.append([x_value,fx_value])
    input_loop = input_loop + 1

#Pre-defined test cases for debugging
#co_ordinate = [(0,0),(1,-1),(2,8),(3,63),(4,224),(-1,-1),(-2,8),(-3,63)]
#co_ordinate = [(0,0),(1,1),(2,4),(3,9),(4,16),(-1,1),(-2,4),(-3,9),(-4,16)]

#Soring the list according to the value of x
co_ordinate.sort(key=lambda x:x[0])
sorted_x = [lis[0] for lis in co_ordinate]
sorted_fx =[lis[1] for lis in co_ordinate]

#Functions or modules
def linear_solver(x,fx):
    x_1 = x[0]
    x_2 = x[1]
    x_3 = x[2]
    fx_1 = fx[0]
    fx_2 = fx[1]
    fx_3 = fx[2]

    a = fx_1/((x_1-x_2)*(x_1-x_3)) + fx_2/((x_2-x_1)*(x_2-x_3)) + fx_3/((x_3-x_1)*(x_3-x_2))

    b = (-fx_1*(x_2+x_3)/((x_1-x_2)*(x_1-x_3))
         -fx_2*(x_1+x_3)/((x_2-x_1)*(x_2-x_3))
         -fx_3*(x_1+x_2)/((x_3-x_1)*(x_3-x_2)))

    c = (fx_1*x_2*x_3/((x_1-x_2)*(x_1-x_3))
        +fx_2*x_1*x_3/((x_2-x_1)*(x_2-x_3))
        +fx_3*x_1*x_2/((x_3-x_1)*(x_3-x_2)))

    return a,b,c
non_linear_constants = (linear_solver(sorted_x,sorted_fx))
print(non_linear_constants)

def root_finder(a,b,c):
    root = b**2 - 4*a*c
    if root > 0:
        x1 = (((-b) + (root)**0.5)/(2*a))     
        x2 = (((-b) - (root)**0.5)/(2*a))
        return float("%.0f" % x1), float("%.0f" % x2)
    elif root == 0:
        x = (-b) / 2*a
        return float("%.0f" % x)
    else:
        print("No root!")

#It follows ax^2 + bx + c        
def analytic_function(x):
    fx = non_linear_constants[0]*x**2 + non_linear_constants[1]*x + non_linear_constants[2]
    return float("%.3f" % fx)

#It follow derivative of ax^2 + bx + c
def extrema_function(x):   
    fXX = 2*non_linear_constants[0]*x + non_linear_constants[1]
    return float("%.3f" % fXX)

#Corner Points
corner_point_lowest = sorted_x[0]
corner_point_highest = sorted_x[-1]

#Bi-secting the values for f(x) and x into 2 lists to determin the extremas
index = 0
length = len(sorted_x)
while index < length:
    output_X = analytic_function(sorted_x[index])
    output_eX = extrema_function(sorted_x[index])
    index = index + 1

#Root
print("Roots: " + str(root_finder(non_linear_constants[0],non_linear_constants[1],non_linear_constants[2])))
#PRINT LINES
print("Corner Points, x = " + str(corner_point_lowest) + ', ' + str(corner_point_highest))
print("f(x): " + str(sorted_fx))
print("x: " + str(sorted_x))

