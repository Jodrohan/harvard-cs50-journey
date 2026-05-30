# Write a Python program that takes a meal cost and a tip percentage as input, calculates the tip amount, and prints the final total to leave.
def main():

    dollars = dollars_to_float(input("How much was the meal? "))
   
    tip = percent_to_float(input("What percentage would you like to tip? "))
    
    tip = tip * dollars

    print(f"Leave ${tip:.2f}")



def dollars_to_float(d):
   
    d = d.replace("$","")
    d = float(d)
    return(d)


def percent_to_float(p):
   
    p = p.replace("%","")
    p = float(p)
    p = p/100
    return(p)

main()
