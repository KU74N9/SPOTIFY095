import requests

signup_url = "https://www.spotify.com/signup"
payload = {
    "email": "your_email@example.com",
    "password": "your_secure_password123",
    "displayname": "YourDisplayName",
    "birth_day": "01",
    "birth_month": "01",
    "birth_year": "2000",
    "gender": "male",
    "key": "your_key_if_needed"  # Spotify may require extra fields
}

headers = {
    "User-Agent": "Mozilla/5.0 (Android; Mobile; rv:89.0) Gecko/89.0 Firefox/89.0"
}

response = requests.post(signup_url, data=payload, headers=headers)
print(response.text)
