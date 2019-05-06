## We need use math module to calculate e
import math


## Then we can define a function to solve this question:
def Question6():
    input_InterestrRate_str = input("Interest rate(r):", )
    input_NumberofYears_str = input("number of years(t):", )
    input_Principal_str = input("Principal(P):", )

    ## Convert input string to float.
    r = float(input_InterestrRate_str)
    t = float(input_NumberofYears_str)
    P = float(input_Principal_str)

    ## Calculate future value.
    Future_Value = P * math.exp(r * t)

    print("The money you will have is $", round(Future_Value, 2))

## Test the function
Question6()
