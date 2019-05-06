## For convenience, let’s use datetime module for this question.
## Datetime module can help us identify all illegal date directly.
import datetime

## Then we can define a function to solve this question:
def Question5():
    input_date_str = input("Please input a date(d/m):", )

    ## The following code can transfer our input into a standard datetime format
    input_date = datetime.datetime.strptime(input_date_str, "%d/%m")


    ## Then, we need to set the range of our judgement.
    March_20 = datetime.datetime.strptime('20/03', "%d/%m")
    June_20 = datetime.datetime.strptime('20/06', "%d/%m")


    ## Then, we use if statements to judge the true and false
    if (input_date >= March_20) and (input_date <= June_20):
        print("True")

    else:
        print("False")


## Test the function
Question5()
