import requests
import json

# Load cookies from file
with open("cookies.json", "r") as f:
    cookie_list = json.load(f)

# Convert cookie list to a dictionary
cookies = {cookie['name']: cookie['value'] for cookie in cookie_list}

# Target page (should be the full video/notes URL)
url = "https://learning.onlinemanipal.com/d2l/le/enhancedSequenceViewer/14270?url=https%3A%2F%2F0ff6df2b-fb79-4be6-9d7f-9428edd0fa0a.sequences.api.brightspace.com%2F14270%2Factivity%2F723958%3FfilterOnDatesAndDepth%3D1"  

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers, cookies=cookies)

with open("page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("✅ Saved page.html")
