import re
'''
This code takes input from user and does input validation
If invalid input is given, it prints message and continues back to take correct input
What is left to be done:
Call the API and get the JSON response, parse the response
Take the values which user gave and do the math to convert 
print the converted value
'''
while True:
    val = input("amount to be converted (Q or q to quit): ")
    print("The type of val is", type(val))
    if val == 'q' or val == 'Q':
        exit(0)
    valid_flag = True
    for item in val:
        resp1 = re.match("[0-9]*\.[0-9]*|[0-9]+", item)
        if not resp1:
            valid_flag = False
            print("The value should be only in numbers")
            break
    if not valid_flag:
        continue

    print("The value you have entered is: ", val)
    from_currency = input("From Currency: ")
    valid_flag_1 = True

    # ---------------------------------------------------------------------

    count = 0
    for item1 in from_currency:
        count += 1
        if count > 3:
            valid_flag_1 = False
            print("Please give only 3 characters for from currency or to currency")
            break
        resp1 = re.match("[A-Z]", item1)
        if not resp1:
            valid_flag_1 = False
            print("Please enter only capital letters for from currency or to currency")
            break

    if not valid_flag_1:
         continue
     # -----------------------------------------------------------------------