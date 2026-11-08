## Currency Converter
A command-line currency converter written in Python. It uses the requests module to fetch live exchange rates from the open.er-api.com API and converts an amount between two currency codes.

## Features
Amount Input — Prompts for a numeric amount and rejects non-numeric input.

Currency Codes — Takes 3-letter currency codes for the source and target currencies, uppercased and stripped automatically.

Live Exchange Rates — Fetches current rates from https://open.er-api.com/v6/latest/{from_currency}.

Conversion — Multiplies the amount by the fetched rate to get the converted value.

Formatted Result — Prints the converted amount to 2 decimal places along with the rate used.

Error Handling — Catches network errors with requests.exceptions.RequestException and handles unknown currency codes.

Convert Again — Restarts the converter if the user answers y.

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `requests` | Sends HTTP requests to the exchange rate API |
| open.er-api.com | Provides live exchange rates |
| f-strings | Builds the API URL and output messages |
| `try / except` | Handles invalid amounts and network errors |
| `raise_for_status()` | Detects HTTP error responses |
| `input()` / `print()` | Console interaction |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Install the requests library by running pip install requests.

Save the code as currency_converter.py.

Open a terminal in the folder containing the file.

Run python currency_converter.py.

Enter an amount, the source currency code (e.g. USD), and the target currency code (e.g. EUR), then answer y or n when asked to convert again.

## Improvements
Fix the function naming clash — the rate() function and the rate variable returned from it share a name; renaming one (e.g. get_rate() and exchange_rate) would avoid confusion.

Use a loop instead of recursion — main() calls itself on retry and on several error paths, which stacks frames and will eventually hit Python's recursion limit; a while True loop is safer.
