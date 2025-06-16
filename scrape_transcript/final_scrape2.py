from playwright.sync_api import sync_playwright
import json

# Update this with the cookie JSON file path
COOKIE_FILE = "cookies.json"

# Update this with the URL of the page to scrape
TARGET_URL = "https://learning.onlinemanipal.com/d2l/le/enhancedSequenceViewer/14270?url=https%3A%2F%2F0ff6df2b-fb79-4be6-9d7f-9428edd0fa0a.sequences.api.brightspace.com%2F14270%2Factivity%2F723958%3FfilterOnDatesAndDepth%3D1"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # Load cookies
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

    page = context.new_page()
    page.goto(TARGET_URL)
    page.wait_for_load_state("networkidle")

    input("➡️ Click on the transcript icon manually, then press ENTER to continue scraping...")
    
    # 🧠 Evaluate JS inside the page to get transcript
    transcript_lines = page.evaluate("""
    () => {
        const log = (...args) => console.log('[Debug]', ...args);

        const root1 = document.querySelector('d2l-sequence-viewer')?.shadowRoot;
        if (!root1) return ['❌ root1 not found'];
        log('✅ root1 ok');

        const root2 = root1.querySelector('d2l-sequences-content-router')?.shadowRoot;
        if (!root2) return ['❌ root2 not found'];
        log('✅ root2 ok');

        const root3 = root2.querySelector('d2l-sequences-content-link')?.shadowRoot;
        if (!root3) return ['❌ root3 not found'];
        log('✅ root3 ok');

        const spans = root3.querySelectorAll('#transcript-list li > span:first-child');
        if (!spans || spans.length === 0) return ['❌ spans not found'];

        return Array.from(spans).map(span => span.textContent.trim());
    }
    """)

    print("🧪 Extracted lines:", transcript_lines)


    # 💾 Save to file
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(transcript_lines))

    print("✅ Transcript saved to transcript.txt")
    input("not closing...")
    # browser.close()