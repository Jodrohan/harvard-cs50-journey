# Ask the user for the number of pizzas and cost per pizza, 
# use a custom function to calculate the total with a 10% service fee, and print it formatted as currency.
def main():
    pizza_quantity = quantity(input("No of pizzas: "))
    cost_per_pizza = cost(input("Cost per pizzas: "))
    total = (pizza_quantity * cost_per_pizza) * 1.10
    
    print(f"Bill Amount $ {total:,.2f}")


    

def quantity(q):
    q = float(q)
    return q



def cost(c):
    c = c.replace("$","")
    c = float(c)
    return c

    

main()