"""
CS50P Week 4 - Bitcoin Price Index

In a file called bitcoin.py, implement a program that:
1. Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
2. Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any requests.RequestException.
3. Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.

Notes:
- You will need to use the `requests` library to query the API.
- You will need to use `sys.argv` to read the command-line argument.
"""

import sys
import requests
def main():
    try:
        n = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command line argument")
    except ValueError:
        sys.exit("Command line argument is not a number")
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json() 
        price = data["bpi"]["USD"]["rate_float"]
        amount = n * price
        print(f"${amount:,.4f}")
    except requests.RequestException:
        sys.exit("Failed to connect to the API")

if __name__ == "__main__":
    main()
