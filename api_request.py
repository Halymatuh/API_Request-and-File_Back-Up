import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    data = response.json()

    print("Users from API:\n")

    for user in data:
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("----------------------")

except requests.exceptions.Timeout:
    print("Error: The request took too long. Please try again.")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the internet.")

except requests.exceptions.HTTPError:
    print("Error: The website returned an invalid response.")

except ValueError:
    print("Error: Could not read the data from the API.")

except Exception as e:
    print("An unexpected error occurred:", e)
