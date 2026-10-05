💱 Python Currency Converter
A simple command-line currency converter built with Python. It uses the ExchangeRate-API to fetch live exchange rates and converts any amount between two currencies. It's a great beginner-to-intermediate project for learning about APIs, HTTP requests, error handling, and modular function design in Python.

📖 Python Currency Converter
The Python Currency Converter is a console-based tool that converts money from one currency to another using real-time exchange rates. The user enters an amount, a source currency code (e.g., USD), and a target currency code (e.g., EUR), and the program fetches the latest rate from the free open.er-api.com endpoint.

Once the rate is retrieved, the program calculates the converted amount and displays both the final result and the exchange rate used (e.g., 1 USD = 0.92 EUR). After each conversion, the user can choose to convert again or exit.

All inputs are normalized to uppercase and stripped of whitespace, and errors like invalid amounts, unreachable APIs, or unknown currency codes are handled gracefully with helpful messages.

This project is ideal for anyone learning how to work with web APIs, JSON responses, and robust error handling in Python.

✨ Features
Live exchange rates – Fetches current rates from the ExchangeRate-API.

Supports any currency – Works with any valid 3-letter currency code the API recognizes (e.g., USD, EUR, GBP, JPY).

Decimal amounts – Accepts whole numbers and decimal values.

Auto-formatting of currency codes – Converts input like usd to USD automatically.

Case-insensitive and whitespace-tolerant – Uses .upper() and .strip().

Input validation – Catches non-numeric amounts and re-prompts.

API error handling – Catches network errors, timeouts, and HTTP failures.

Invalid currency detection – Checks whether the target currency exists in the API's rate list.

Rate display – Shows both the converted amount and the per-unit exchange rate.

Repeat option – Convert again without restarting the program.

Entry-point guard – Uses if __name__ == "__main__": for clean script execution.

🛠️ What It Uses
Language & Library
Python 3

requests – A popular third-party library for making HTTP requests.

Install with: pip install requests

External API
ExchangeRate-API (open access) — https://open.er-api.com/v6/latest/{currency}

Free, no API key required.

Returns a JSON object containing exchange rates relative to the requested base currency.

Key Functions
Function	Purpose
user_input()	Prompts for the amount, source currency, and target currency. Handles invalid amounts.
rate(from_currency, to_currency)	Fetches the exchange rate for the target currency from the API. Handles network and currency errors.
convert(amount, rate)	Multiplies the amount by the exchange rate to get the converted value.
result(amount, from_currency, to_currency, rate, converted)	Prints the conversion result and the exchange rate used.
main()	Runs the full program flow and handles the repeat prompt.
Key Variables
Variable	Purpose
amount	The amount of money to convert.
from_currency	The currency being converted from (e.g., USD).
to_currency	The currency being converted to (e.g., EUR).
rated	The exchange rate returned by the API.
converted	The final converted amount.
Python Concepts Demonstrated
The requests library – Making HTTP GET requests.

JSON parsing – Using response.json() to get structured data.

Exception handling – try/except blocks for both ValueError and requests.exceptions.RequestException.

F-strings – Formatting URLs and output messages.

String methods – .upper() and .strip() for clean input.

Functions – Modular, single-purpose function design.

Recursion – main() calls itself when the user chooses to convert again.

if __name__ == "__main__": – Standard Python entry-point pattern.

Dictionary access – Using .get() to safely retrieve the "rates" key.

Float formatting – :.2f to round the converted result to two decimal places.

Type-agnostic conversion – Converting amount and rate via multiplication.

Built-in Functions Used
input() – Reads user input from the console.

print() – Displays messages and results.

float() – Converts the amount input into a number.

exit() – Terminates the program when the user chooses to quit.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
currency_converter.py
Then install the required library:

bash
pip install requests
▶️ How to Run
Make sure you have Python 3 installed (python.org).

Install the requests library:

bash
pip install requests
Save the code as currency_converter.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python currency_converter.py
Enter an amount, a source currency code, and a target currency code — and the program will fetch the latest rate and print the converted value.

🐍 Made with Python
This project is written in Python 3 and uses the requests library to communicate with a free exchange-rate API. It's a clean, practical example of how to integrate a real web service into a small command-line application.

Whether you're a beginner learning about APIs or someone who wants a quick currency conversion tool, this project is a great starting point.

💡 Possible Future Improvements
Cache rates locally to reduce API calls and speed up repeated conversions.

Validate currency codes before calling the API using a built-in list of valid codes.

Handle the from_currency error consistently – Currently, if the base currency is invalid, the API returns an error response rather than raising an exception. Add a check for the "error" field in the JSON.

Fix the recursion flow – main() calls itself, which can eventually hit Python's recursion limit if used many times. Consider using a while True loop instead.

Fix the "Try again" branch – Returning again from main() doesn't do anything because the return value is discarded. Should re-prompt or restart main().

Add a list of common currencies for the user to choose from.

Show historical rates or a chart of rate trends.

Add a GUI using Tkinter or a web interface using Flask.

Support crypto currencies in addition to fiat.

📄 License
This project is free to use, modify, and distribute for personal or educational purposes.
