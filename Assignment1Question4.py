## First, we need use random module for this question
import random

## Then we can define a function to solve this question:
def Question4():
    input_x_str = input("Please input an integer as starting point:", )
    x = int(input_x_str)

    input_y_str = input("Please input an integer as ending point:", )
    y = int(input_y_str)

    print(random.randint(x, y))

## Test the function
Question4()
