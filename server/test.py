import requests

url = "http://127.0.0.1:5000/api/trips"

test_data = {
    "destination": "Coorg",
    "groupType": "friends",
    "experience": "adventure",
    "budget": "affordable",
    "stayType": "luxurious",
    "duration": "2 days",
    "wantsHiddenSpots": True,
    "needsOfflineMap": False
}

response = requests.post(url, json=test_data)

print("Status Code:", response.status_code)
print("Response:", response.json())
