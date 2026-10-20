Currency Converter
A command-line Python program that converts between currencies using the Open Exchange Rates API.

Concepts Used
requests Library — fetches live exchange rates from an HTTP API endpoint.

Exception Handling — try/except catches ValueError for amounts and RequestException for network/API errors.

Functions with Return Values — input, rate lookup, conversion, and display are split into separate functions.

Features
Live Exchange Rates — pulls current rates based on the from_currency code.

Currency Validation — checks both codes exist in the API's rates dict before converting.

Formatted Output — shows the converted total to 2 decimals plus the unit rate.

Improvements
Fix Recursion & Fallthrough — main() calls itself on errors and again on "convert again", stacking frames; return early instead. Also user_input() continues after a bad amount instead of stopping.

Dead Code & Misplaced Check — rate() checks to_currency before from_currency, and the from_currency check prints but never returns, so it falls through to a KeyError.

Cache & Exit Cleanly — the API is re-fetched every call and exit() appears in a helper; cache the response and use a while loop with a proper quit path.
