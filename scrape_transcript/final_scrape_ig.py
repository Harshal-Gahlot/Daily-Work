from playwright.sync_api import sync_playwright
import json

# 🔧 UPDATE THIS: Replace with your actual cookie JSON file (exported from browser using "EditThisCookie")
COOKIE_FILE = "cookies.json"

# 🔧 UPDATE THIS: Target URL (the page with the transcript you want)
TARGET_URL = "https://learning.onlinemanipal.com/d2l/le/enhancedSequenceViewer/14270?url=https%3A%2F%2F0ff6df2b-fb79-4be6-9d7f-9428edd0fa0a.sequences.api.brightspace.com%2F14270%2Factivity%2F723958%3FfilterOnDatesAndDepth%3D1"

# 🔧 UPDATE THIS: Output file name
OUTPUT_FILE = "transcript.txt"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) 
    context = browser.new_context()

    # Load and apply cookies
    with open(COOKIE_FILE, "r", encoding="utf-8") as f:
        raw_cookies = json.load(f)

    # Fix Playwright cookie format (especially sameSite value)
    cookies = []
    for cookie in raw_cookies:
        if cookie.get("sameSite") not in ("Strict", "Lax", "None"):
            cookie["sameSite"] = "Lax"
        cookies.append({
            "name": cookie["name"],
            "value": cookie["value"],
            "domain": cookie["domain"],
            "path": cookie.get("path", "/"),
            "expires": cookie.get("expirationDate", -1),
            "httpOnly": cookie.get("httpOnly", False),
            "secure": cookie.get("secure", False),
            "sameSite": cookie["sameSite"]
        })

    context.add_cookies(cookies)

    # Open new page and go to target URL
    page = context.new_page()
    page.goto(TARGET_URL)
    page.wait_for_load_state("networkidle")

    # 🔧 Optional: click on transcript button manually (pause until you do)
    input("➡️ Click on the transcript icon manually, then press ENTER to continue scraping...")

    # Wait for transcript list to load
    page.wait_for_selector("#transcript-list li > span:first-child", timeout=10000)

    # Extract only the first <span> inside each <li>
    items = page.query_selector_all("#transcript-list li > span:first-child")
    lines = [item.inner_text() for item in items]

    # Save to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"✅ Saved transcript to {OUTPUT_FILE}")
    browser.close()
