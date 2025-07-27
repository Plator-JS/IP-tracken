import requests

def check_ip(ip):
    print(f"IP-Adresse analysieren: {ip}\n")
    
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)

    if response.status_code != 200:
        print("Fehler beim Abrufen der IP-Daten.")
        return

    data = response.json()

    city = data.get("city", "Unbekannt")
    region = data.get("region", "Unbekannt")
    country = data.get("country", "Unbekannt")
    org = data.get("org", "Unbekannt")
    loc = data.get("loc", None)

    print(f"Land: {country}")
    print(f"Stadt/Region: {city}, {region}")
    print(f"Provider/Organisation: {org}")

    suspicious_keywords = ["Tor", "Proxy", "VPN", "Hosting", "Data Center", "DigitalOcean", "Amazon", "Google", "Hetzner"]
    if any(word.lower() in org.lower() for word in suspicious_keywords):
        print("Warnung: Verdächtiger Provider (möglicherweise VPN, Tor oder Rechenzentrum)")

    if loc:
        print(f"Google Maps Link: https://www.google.com/maps?q={loc}")
    else:
        print("Kein Standort verfügbar.")

ip_input = input("Gib eine IP-Adresse ein: ")
check_ip(ip_input)
