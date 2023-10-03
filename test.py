from forex_python.converter import CurrencyRates

# Create an instance of the CurrencyRates class
c = CurrencyRates()

# Define the amount and the currencies you want to convert from and to
amount = 1.00  # Change this to the amount you want to convert
from_currency = "USD"  # Change this to the source currency code
to_currency = "INR"    # Change this to the target currency code

# Convert the currency
result = c.convert(from_currency, to_currency, amount)

# Display the result
print(f"{amount} {from_currency} is equal to {round(result)} {to_currency}")
