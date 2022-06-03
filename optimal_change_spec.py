from optimal_change import optimal_change
print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
print("3:", optimal_change(45.23, 60) == "The optimal change for an item that costs $45.23 with an amount paid of $60 is 1 $10 bill, 4 $1 bills, 3 quarters, and 2 pennies.")
print("4:", optimal_change(20.31, 25) == "The optimal change for an item that costs $20.31 with an amount paid of $25 is 4 $1 bills, 2 quarters, 1 dime, 1 nickel, and 4 pennies.")
print("5:", optimal_change(99.50, 100) == "The optimal change for an item that costs $99.5 with an amount paid of $100 is 2 quarters.")
print("6:", optimal_change(10, 20) == "The optimal change for an item that costs $10 with an amount paid of $20 is 1 $10 dollar bill.")
print("7:", optimal_change(40, 30) == "Uh oh, Looks like you haven't paid enough!")
print("8:", optimal_change(25, 25) == "Wow, You've payed with exact change and made this assessment way easier for me!")
