import requests
import json
import os

API_KEY = "Y6m2OzB6PtI67PkMaAFnzDx0dtixSKVt"
BASE_URL = "https://api.massive.com/v3/reference/tickers"

CACHE_FILE = "cache.json"


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as file:
            return json.load(file)
    return {}


def save_cache(cache):
    with open(CACHE_FILE, "w") as file:
        json.dump(cache, file)


cache = load_cache()


def get_stock(symbol):
    symbol = symbol.upper()

    if symbol in cache:
        print("Using cached data...")
        return cache[symbol]

    url = f"{BASE_URL}/{symbol}?apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        cache[symbol] = data
        save_cache(cache)
        return data
    else:
        return None


def menu():
    while True:
        print("\nStock Explorer")
        print("1. Search Stock by Ticker")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            symbol = input("Enter stock ticker: ")
            data = get_stock(symbol)

            if data:
                print(json.dumps(data, indent=2))
            else:
                print("Error retrieving stock data.")

        elif choice == "2":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()