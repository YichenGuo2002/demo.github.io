import requests

def get_api_data():
    x = 10
    url = 'http://127.0.0.1:5000/api/data'  # Sample public API
    try:
        response = requests.get(url)
        data = response.json()       # Parse the JSON response
        # print("✅ Data received:")
        print(data)
    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)

if __name__ == "__main__":
    get_api_data()