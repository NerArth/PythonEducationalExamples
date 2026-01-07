# 3. Exercise. Conditionals Intermediate
# Alter the code demonstrating how when required conditions are met, the code allows for an alternative
# action to take place if none of the conditions are met, with the use of an `else`.

product = "Milk"
price = 3
currency = "USD"
dateofproduction = 1767818536.745559

milk_collection = [product, price, currency, dateofproduction]

# Alter the code below to print a variable only if it's the price integer value.
# - You MUST keep the for loop but can alter the code inside. However, you are not expected to demonstrate an integer type check.
# - You MUST use the `if` keyword.
# - You MUST also print a message when the variable is NOT an integer, i.e. with the use of an `else`.

for item in milk_collection:
    print(item)