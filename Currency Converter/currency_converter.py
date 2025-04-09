# Task 05:
# Currency Converter Tool

import requests

def get_exchange_rates(base_currency="USD"):
    try:
        url = f"https://v6.exchangerate-api.com/v6/25ec29b9b837c037009c85ae/latest/{base_currency.upper()}"
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError if response code isn't 200
        data = response.json()
        if data.get("result") != "success":
            raise ValueError("Failed to fetch exchange rates from API.")
        return data["conversion_rates"]
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None


def get_user_input():
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("From currency (e.g., USD): ").upper()
        to_currency = input("To currency (e.g., PKR): ").upper()
        return amount, from_currency, to_currency
    except ValueError:
        print("Invalid input. Amount should be a number.")
        return None, None, None


def convert_currency(amount, from_currency, to_currency, rates):
    try:
        if from_currency not in rates:
            raise KeyError(f"Currency not supported: {from_currency}")
        if to_currency not in rates:
            raise KeyError(f"Currency not supported: {to_currency}")

        usd_amount = amount / rates[from_currency]
        converted = usd_amount * rates[to_currency]
        return round(converted, 2)
    except KeyError as ke:
        print(ke)
    except Exception as e:
        print(f"Error during conversion: {e}")
    return None


def main():
    amount, from_currency, to_currency = get_user_input()
    if None in (amount, from_currency, to_currency):
        print("Conversion none due to invalid input.")
        return
    print("\n Fetching real-time exchange rates...")
    rates = get_exchange_rates(base_currency=from_currency)
    if rates:
        result = convert_currency(amount, from_currency, to_currency, rates)
        if result is not None:
            print(f" {amount} {from_currency} = {result} {to_currency}")
        else:
            print(" Conversion could not be completed.")
    else:
        print(" Could not fetch exchange rates. Please check your internet or try again later.")


if __name__ == "__main__":
    main()
