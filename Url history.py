import requests

url = "https://na01.safelinks.protection.outlook.com/"
response = requests.get(url, allow_redirects=True)

for i, r in enumerate(response.history, 1):
    print(f"Step {i}: {r.url} -> {r.status_code}")

print(f"Final URL: {response.url}")