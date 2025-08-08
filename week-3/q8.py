def vending_machine():
    items = {}
    with open("VendingItems.txt", "r") as f:
        for line in f:
            name, price = line.strip().split('|')
            items[name] = int(price)

    while True:
        item = input("Enter item name: ")
        if item not in items:
            print(f"Available Items are {list(items.keys())}. Try Again.")
            continue
        break

    while True:
        try:
            money = int(input("Enter money: "))
            if money >= items[item]:
                change = money - items[item]
                print(f"Thank you for your purchase. Enjoy. Collect your change: {change} Rs.")
                break
            else:
                print("Insufficient money. Try Again.")
        except ValueError:
            print("Bad Input. Try Again.")


vending_machine()