import requests

def main():
    url = "https://www.boredapi.com/api/activity"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # erreur si code != 200

        data = response.json()
        print("🔹 Activité proposée :", data["activity"])
        print("🔹 Type :", data["type"])

    except requests.exceptions.RequestException as e:
        print("Erreur lors de l'appel à l'API :", e)

if __name__ == "__main__":
    main()
