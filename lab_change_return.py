def change_return(change):
    change = int(change * 100)
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while change > 0:
        if change >= 100:
            dollars = dollars + 1
            change = change - 100
        if change < 100 and change >= 25:
            quarters = quarters + 1
            change = change - 25
        elif change < 25 and change >= 10:
            dimes = dimes + 1
            change = change - 10
        elif change < 10 and change >= 5:
            nickels = nickels + 1
            change = change - 5
        else:
            pennies = pennies + 1
            change = change - 1
    return("Dollars", dollars, "Quarters: ", quarters, "Dimes: ", dimes, "Nickels: ", nickels, "Pennies: ", pennies)

print(change_return(2.34))
print(change_return(6.45))
print(change_return(9.13))

change_needed = float(input("How much change is needed? "))
print(change_return(change_needed))
