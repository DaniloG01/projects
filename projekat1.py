import re
from collections import Counter

def ucitaj_log(putanja):
    with open(putanja, 'r', encoding='utf-8') as f:
        return f.readlines()

def analiziraj_log(logovi):
    ip_adrese = []
    metode = []
    statusi = []

    for linija in logovi:
        ip = re.search(r'^(\d{1,3}(\.\d{1,3}){3})', linija)
        metoda = re.search(r'"(GET|POST|PUT|DELETE|PATCH)', linija)
        status = re.search(r'" \d{3} ', linija)
        
        if ip:
            ip_adrese.append(ip.group(1))
        if metoda:
            metode.append(metoda.group(1))
        if status:
            statusi.append(status.group(0).strip().replace('" ', ''))

    return {
        "ukupno": len(logovi),
        "najcesce_ip": Counter(ip_adrese).most_common(5),
        "metode": Counter(metode),
        "statusi": Counter(statusi)
    }

def ispisi_rezultate(statistika):
    print(f"Ukupno zahteva: {statistika['ukupno']}")
    print("Top 5 IP adresa:")
    for ip, br in statistika['najcesce_ip']:
        print(f" - {ip}: {br} puta")
    print("HTTP metode:")
    for m, br in statistika['metode'].items():
        print(f" - {m}: {br}")
    print("HTTP statusi:")
    for s, br in statistika['statusi'].items():
        print(f" - {s}: {br}")

if __name__ == "__main__":
    try:
        logovi = ucitaj_log("access.log")
        statistika = analiziraj_log(logovi)
        ispisi_rezultate(statistika)
    except FileNotFoundError:
        print("Fajl 'access.log' nije pronađen.")
