import json
from playwright.sync_api import sync_playwright

# Load cookies
with open("cookies.json", "r") as f:
    raw_cookies = json.load(f)

# Convert EditThisCookie format to Playwright format
def convert_cookie(cookie):
    same_site = cookie.get("sameSite", "Lax")
    if same_site not in ["Strict", "Lax", "None"]:
        same_site = "Lax"
    return {
        "name": cookie["name"],
        "value": cookie["value"],
        "domain": cookie["domain"].lstrip("."),
        "path": cookie.get("path", "/"),
        "httpOnly": cookie.get("httpOnly", False),
        "secure": cookie.get("secure", False),
        "sameSite": same_site
    }


cookies = [convert_cookie(c) for c in raw_cookies]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    
    # Set cookies
    context.add_cookies(cookies)
    page = context.new_page()

    # Go to target page
    page.goto("")
    page.wait_for_load_state("networkidle")
    
    # Click Transcript button
    # page.click("button:has-text('Transcript')")  # You may need to refine this selector
    print("👉 Manually click on the Transcript SVG or any interactive element.")
    input("Press ENTER once you see the transcript loaded...")
    print("Waiting 2 sec for transcript to load...")
    page.wait_for_timeout(2000)  # Wait for transcript to load

    with open("transcript_page.html", "w", encoding="utf-8") as f:
        f.write(page.content())

    print("✅ Done. Transcript page saved.")
    browser.close()