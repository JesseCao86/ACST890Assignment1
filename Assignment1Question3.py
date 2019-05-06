def Question3():
    input_year_str = input("Please input an integer:", )
    year = int(input_year_str)

    ## It is the definition of leap year:
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):

        print("leap year".format(year))

    else:
        print("nonleap year".format(year))


## Test the function
Question3()
