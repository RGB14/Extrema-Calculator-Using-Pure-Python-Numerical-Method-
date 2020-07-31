
#
# ARRAY DECLARATIONS for plotting the graph
#
xarray = []
yarray = []
farray = []
minimum_value = 0
maximum_value = 0
local_minima = 0
local_maxima = 0
stationary_point_low = 0
stationary_point_high = 0
critical_value = 0
x_list = []
fx_list = []


#co_ordinate = [(0,0),(1,-1),(2,8),(3,63),(4,224),(-1,-1),(-2,8),(-3,63)]
#co_ordinate = [(0,0),(1,1),(2,4),(3,9),(4,16),(-1,1),(-2,4),(-3,9),(-4,16)]
#
#The analytic function is defined here
#

def analytic_function(x):
    fx = 2*x**3 - 15*x**2 + 36*x
    return float("%.3f" % fx)

#
# The derivation function is declared by using the NUMERICAL DIFFERENTIAL
#

def derive_function(a):
    h = 0.00000000001   
    top = (3*2*(a + h)**2 - 2*15*(a + h) + 36) - (3*2*(a)**2 - 2*15*(a) + 36)
    bottom = h
    slope = top / bottom
    return float("%.3f" % slope)


#Soring the list according to the value of x
co_ordinate.sort(key=lambda x:x[0])
sorted_x = [lis[0] for lis in co_ordinate]
sorted_fx =[lis[1] for lis in co_ordinate]


#Input from user for Interval
input_loop= 0  
input_message = int(input("How many inputs would you like to take: "))
while input_loop < input_message:
    print("Value for Input: " + str(input_loop + 1))
    x_value = int(input("Enter value for x: "))
    x_list.append(x_value)
    fx_value = int(input("Enter value for f(x): "))
    fx_list.append(fx_value)
    input_loop = input_loop + 1

corner_point_lowest = sorted_x[0]
corner_point_highest = sorted_x[-1]

minimum_interval = sorted_x[0]
maximum_interval = sorted_x[-1]
iteration_count = float(input("Enter the iteration difference from x0 to xn: "))

#DERIVATIVE ITERATIONS
print("DERIVATIVE VALUES: ")
# X is being reset for the while loop
x = minimum_interval
while x < maximum_interval:
    print("x = " + str("%.3f" % x) + " f'(x) = " + str(derive_function(x)))
    xarray.append(x)
    #d_normalize = derive_function(x) + 41
    yarray.append(derive_function(x))
    #yarray.append(d_normalize)
    if (derive_function(x) < 0.01 and derive_function(x) > -0.01):
        stationary_point_low = m.floor(x)
        stationary_point_high = m.ceil(x)
        critical_value = x
    #interpolation for iterations
    x = x + iteration_count  
        
#ANALYTIC ITERATIONS
print("ANALYTIC FUNCTIONAL VALUE: ")
# Again, X is being reset for the loop
x=minimum_interval
while x < maximum_interval:
    print("x = " + str("%.3f" % x) + " f(x) = " + str(analytic_function(x)))
    farray.append(analytic_function(x))
    if(analytic_function(minimum_interval)):
        minimum_value = analytic_function(minimum_interval)
    if(analytic_function(maximum_interval)):
        maximum_value = analytic_function(maximum_interval)
    #interpolation for iterations
    x = x + iteration_count



min_extrema = analytic_function(local_minima)
max_extrema = analytic_function(local_maxima)

print("Corner Points, x = " + str(corner_point_lowest) + ', ' + str(corner_point_highest))
print("Stationary Point (1) : " + str(stationary_point_low))
print("Stationary Point (2) : " + str(stationary_point_high))
print("MAXIMUM value of f(x): " + str(maximum_value))
print("MINIMUM value of f(x): " + str(minimum_value))
print("Total Interpolation count: " + str(len(xarray)))

