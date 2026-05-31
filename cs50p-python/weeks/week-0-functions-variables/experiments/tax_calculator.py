# Ask for a price and tax rate, clean the text, calculate the total using: price + (price * (tax / 100)), and print it as currency.

def main():
    price_str = price_int(input("Enter price: "))
    tax_rate_str = tax_rate_int(input("Enter tax rate: "))

    total = price_str + (price_str * (tax_rate_str / 100))
    
    print(f"${total:.2f}")
   
def price_int(p):
    p = p.replace("$","")
    p = float(p)
    return p

def tax_rate_int(t):
    t = t.replace("%","")
    t = float(t)
    return t


main()