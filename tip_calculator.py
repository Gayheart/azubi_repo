TIP_PERCENT = 0.18
TAX_PERCENT = 0.07

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
    foodCharge = getFoodCharge()
    tip, tax = tipAndTax(TIP_PERCENT, TAX_PERCENT, foodCharge)
    print(f"Tip = ${tip: .2f} \nSales tax = ${tax: .2f} \n\
Grand total = ${foodCharge + tip + tax: .2f}")

if __name__ == "__main__":
    main()