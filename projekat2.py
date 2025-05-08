import requests

def get_exchange_rate(crypto='bitcoin', currency='eur'):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[crypto][currency]
    else:
        raise Exception("Neuspelo povezivanje sa API-jem.")

def main():
    print("=== Kripto Konverter ===")
    iznos_eur = float(input("Unesite iznos u evrima: "))
    crypto = input("Unesite naziv kriptovalute (npr. bitcoin, ethereum): ").lower()

    try:
        kurs = get_exchange_rate(crypto)
        iznos_kripto = iznos_eur / kurs
        print(f"{iznos_eur} EUR = {iznos_kripto:.6f} {crypto.upper()}")
    except Exception as e:
        print("Greška:", e)

if __name__ == "__main__":
    main()
