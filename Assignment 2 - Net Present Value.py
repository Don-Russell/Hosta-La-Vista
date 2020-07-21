
####################
##Reflection:

##There are a number of errors I had with my initial attempt.  Firstly, I had executed the three functions, but did not include the format specification in the Get_Values and the final output function.
##I was able to get the correct values on the year variables in the NPV calculation, given that we reviewed it from Exercise 1.  The iteration on the year (variable t) also made sense as we covered that in class.  One issue I did have was with text wrapping on the output function as my output was quite wordy.  I had tried to manually ctrl+enter it to the next list, but it gave me an incorrect syntax error without much description when I tried to right click + ‘Run Current File from Python Interactive Window’.  
##Lastly, there was some initializing of the list of values at the bottom portion of code which we have not yet covered in class.  I found the last four statements particularly confusing and needed to look at the solution before adjusting my own code to execute properly.  
##In retrospect, I would have read the textbook for more examples prior to trying to blunder and google my way through the code before using the solution as a crutch to get it to be error free.  I would also like to know how to properly text wrap -- I went through the preferences and settings but did not find anything there.  I’m looking forward to learning about Dictionaries, Lists, and Tuples.

####################

def Get_Values(): 
    X0 = float(input('Initial Investment: '))
    X1 = float(input('Year 1 Investment: '))
    X2 = float(input('Year 2 Investment: '))
    X3 = float(input('Year 3 Investment: '))
    R = float(input('What is the discount rate? '))
    t = 0
    return (X0, X1, X2, X3, R, t) 

def NPV(X0,X1,X2,X3,R,t):
    year0=-X0/(1+R)**t
    t+=1
    year1=X1/(1+R)**t
    t+=1
    year2=X2/(1+R)**t
    t+=1
    year3=X3/(1+R)**t
    net_present_value= year0+year1+year2+year3
    return (net_present_value)

def output(X0,X1,X2,X3,R,net_present_value):
    result = f'The net present value of investment is $' + str(net_present_value) + ' given the initial investment of $' + str(X0) + ', a year 1 contribution of $' + str(X1) + ', year 2 contribution of $' + str(X2) + ', and a year 3 contribution of ' + str(X3) + '.'
    print(result)

#The 

#Call function to get the values from the user
values = Get_Values() 

#Initialize the individual variables
X0, X1, X2, X3, R, t = values[0], values[1], values[2], values[3], values[4], values[5] 

#Call the function to calculate NPV
net_present_value = NPV(X0, X1, X2, X3, R, t) 

#Call the function to print the results
output(X0, X1, X2, X3, R, net_present_value) 


####################
# SOLUTION
####################

# def Get_Values(): 
#   '''Collects the users information''' 
#   X0 = int(input('Initial Investment: '))
#   X1 = int(input('First year income: '))
#   X2 = int(input('Second year income: '))
#   X3 = int(input('Third year income: '))
#   R = float(input("Discount rate: "))
#   t = 0
#   return (X0, X1, X2, X3, R, t) 

# def Calculate_NPV (X0, X1, X2, X3, R, t): 
#   '''Calculate NPV''' 
#   year0 = -X0/(1+R)**t
#   t += 1
#   year1 = X1/(1+R)**t
#   t += 1
#   year2 = X2/(1+R)**t
#   t += 1
#   year3 = X3/(1+R)**t
#   npv = round(year0 + year1 + year2 + year3)
#   return npv

# def Print_Result (X0, X1, X2, X3, R, npv): 
#   '''Printing the result''' 
#   result = 'The NPV of an initial investment of $' + str(X0) + ' earning $' + str(X1) + ', $' + str(X2) + ', $' + str(X3) + ' each year with a ' + str(R) + '% discount rate is $' + str(npv) 
#   print(result) 

# #Call function to get the values from the user
# values = Get_Values() 

# #Initialize the individual variables
# X0, X1, X2, X3, R, t = values[0], values[1], values[2], values[3], values[4], values[5] 

# #Call the function to calculate NPV
# npv = Calculate_NPV(X0, X1, X2, X3, R, t) 

# #Call the function to print the results
# Print_Result(X0, X1, X2, X3, R, npv) 