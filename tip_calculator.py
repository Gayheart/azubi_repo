def tipAndTax(tip_percent:float, tax_percent:float, amount:float) -> float:
    """Calculate food tip and tax"""
    tip = tip_percent * amount
    tax = tax_percent * amount
    return (tip, tax)

def getFoodCharge():
    """Get food cost"""
    while True:
        try:
            amount = float(input("Food cost: "))
        except (ValueError, KeyboardInterrupt):
            print("Enter a food cost")
        else:
            return amount
        
def main():
    tip_percent = 0.18
    tax_percent = 0.07
    foodCharge = getFoodCharge()
    tip, tax = tipAndTax(tip_percent, tax_percent, foodCharge)
    print(f"Tip = ${tip} \nSales tax = ${tax} \n\
Grand total = ${round(foodCharge + tip + tax, 2)}")

if __name__ == "__main__":
    main()