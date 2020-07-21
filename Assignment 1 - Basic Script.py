#My first try
Rate = 10000
Year1 = 500
Year2 = 750
Year3 = 1000
Interest = 0.05

print(f'The NPV of an initial investment of {Rate} earning 
${Year1} in the first year, ${Year2} in the second year, and 
${Year3} in the third year.  With a discount unit rate of 5% is 
{(Rate+Year1)/(1+Interest)+(Rate+Year2)/(1+Interest)+(Rate+Year3)/(1+Interest)}')


# Although I got an error defining my variables, the right click + ‘run current python in interactive window’ produced the correct result.  Retrospectively, I would have defined each separate year as a formula instead of trying to accumulate it all in the f-string.  Also, I did like the Jupyter notebook for the way it allowed for the separation of code to incrementally create the script.
# Overall, I quite like python as compared to C+ -- way back in university we were forced to learn C and Python, at this level of complexity, seems far more user-friendly.  The syntax and ease of use is refreshing.  
# Visual studio code is also quite slick; the interface is straightforward and the versatility of being able to code in various languages is convenient.  Also, the default for dark mode is easier on the eyes.  
# Lastly, I just asked if there is a currency format which would be convenient to use.  In excel there is a future value and net present value formula which are built in.  This isn’t quite the 250 word limit, but I’ve run out of things to say at just over 200 words.  I’ll have more to reflect on in future assignments.  


