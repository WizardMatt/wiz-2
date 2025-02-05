def convert_currency(amount, currency):
    rates = {"EUR": 0.85, "GBP": 0.75, "INR": 74.50, "JPY": 110.53}
    return amount * rates.get(currency, 1)

amount = float(input("Enter amount in USD: "))
currency = input("Convert to (EUR/GBP/INR/JPY): ").upper()
converted_amount = convert_currency(amount, currency)

if converted_amount != amount:
    print(f"{amount} USD is {converted_amount:.2f} {currency}")
else:
    print("Invalid currency code!")
