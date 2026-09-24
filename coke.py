def run_coke_machine():                                                                 # Definesgit remote -v function
    price = 50
    amount_due = price

    while amount_due > 0:                                                               # Begins loop because multiple coins may be provided
        print(f"Amount due: {amount_due}")

        try:                                                                            # Requests coin value and produces error message if non-integer value entered
            coin = int(input("Insert coin: "))
        except ValueError:
            print("Invalid input. Please insert a valid coin (25, 10, or 5).")
            continue

        if coin in [25, 10, 5]:                                                         # Reduces amount due if coin is an accepted denomination and reminds user of accepted coins if not
            amount_due -= coin
        else:
            print("Accepted coins are: 25, 10, 5 cents")

    change = abs(amount_due)                                                            # Prints change owed as a positive value
    print(f"Change Owed: {change}")

if __name__ == "__main__":                                                              # ends function
    run_coke_machine()


