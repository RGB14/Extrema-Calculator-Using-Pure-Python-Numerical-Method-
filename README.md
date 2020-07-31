# Extrema-Calculator-Using-Pure-Python-Numerical-Method

###---CODE VERSIONS---###

There are 2 versions of code:
1. Numerical_Solution_v1 -> which uses direct method to solve the problems using methods
2. Numerical_Solution_v2 -> which iterates over an interval

Due to completexity, the code is incomplete and was tough to build as there was no library used.
However, with library, it could have been in a few lines.

###---HOW TO RUN SCRIPT---###

1) Download Python Library and compiler from
https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe

During installation, check Add Python 3.8 to PATH
At the end, Disable the PATH Limit

2) Open any Terminal or Command Prompt and use 'cd' command to redirect to the assignment folder

3) After redirection, use 'python numerical_solution_v1.py' to run the script 
			----OR----
			use 'python_numerical_solution_v2.py' 


###---INSTRUCTIONS TO SOLVE THE PROBLEM---###

Based on test cases, as given earlier, considering input as
(𝑥, 𝑓(𝑥)) = [(0,0), (1,1), (2,4), (3,9), (4,16), (−1,1), (−2,4), (−3,9), (−4,16)]
The values for 𝑥 and 𝑓(𝑥) are bisected and sorted in ascending order in
2 array lists as:
sorted_x [] which will contain -> [−4, −3, −2, −1, 0, 1, 2, 3, 4]
sorted_fx [], which will contain -> [16, 9, 4, 1, 0, 1, 4, 9, 16]
#CORNER POINTS
From this, we can deduce the corner points, where the value of 𝑥
reached at most, by the following code
corner_point_lowest = sorted_x[0]
corner_point_highest = sorted_x[-1],
where the initial value and the last value of the sorted_x are extracted
into the variable,
'corner_point_lowest' and 'corner_point_highest'
#EXTREMAS
By theory, we know the extremas happen at the point where there are
turning points in a graph.
Minima is the point where the graph is at minimum point and is an
increasing function.
Maxima is the point where the graph is at maximum point and is a
decreasing function.Based on test cases, as given earlier,
(𝑥, 𝑓(𝑥)) = [(0,0), (1,1), (2,4), (3,9), (4,16), (−1,1), (−2,4), (−3,9), (−4,16)]
The values for 𝑥 and 𝑓(𝑥) are used to form an equation by putting the
values into linear equation solver.
In this case, the values 𝑎, 𝑏, 𝑐 are returned by following the quadratic rule,
𝑎𝑥2 + 𝑏𝑥 + 𝑐
Then, using those values of 𝑎, 𝑏, 𝑐 an analytic equation is form.
Putting 𝑥 into the analytic_function(x) will give the same result as in
𝑓(𝑥)
Then, by deriving first order of the analytic equation, we will get the
first derivative, which is 𝑓’(𝑥)
Now, solve for the values of 𝑥 when 𝑓’(𝑥) = 0
The points of 𝑥 that are obtained are called critical values or extremas.
Now to determine, the mimima or maxima, we simply have to put the
critical values into the derivative function that is in this test case,
Extremas: 0, -4, 4
Put 𝑓’(0), 𝑓’(−4), 𝑓’(4) respectively and check for the sign of the value
whether it is negative or positive.
The value that gives 𝑓’(𝑥) positive value is the maxima and similarly,
the value that gives 𝑓’(𝑥) negative value is the minima.
