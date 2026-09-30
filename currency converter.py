import requests


def user_input():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Choose a numerical amount.")
        main()
    from_currency = input("What currency would you like to convert from? (enter the 3 letter currency code.) ").upper().strip()
    to_currency = input("What currency would you like to convert to? (enter the 3 letter currency code.) ").upper().strip()
    return amount, from_currency, to_currency


def rate(from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"The API can not be reached: {e}")
        main()

    rates = data.get("rates", {})
    if to_currency not in rates:
        print(f"{to_currency} not found.")
        main()
    
    if from_currency not in rates:
        print(f"{from_currency} not found.")

    return rates[to_currency]


def convert(amount, rate):
    return amount * rate


def result(amount, from_currency, to_currency, rate, converted):
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
    print(f"1 {from_currency} = {rate} {to_currency}")


def main():
    print("=====CURRENCY CONVERTER=====")

    amount, from_currency, to_currency = user_input()

    rated = rate(from_currency, to_currency)
    if rated is None:
        print("Conversion failed. Check currency code.")
        return

    converted = convert(amount, rated)
    result(amount, from_currency, to_currency, rated, converted)

    again = input("Would you like to convert again? (y/n) ").lower().strip()
    if again == "y":
        main()
    elif again == "n":
        exit()
    else:
        print("Try again. ")
        return again


if __name__ == "__main__":
    main()