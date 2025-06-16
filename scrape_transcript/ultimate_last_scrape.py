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
        
    iframe_element = page.evaluate_handle("""
        () => {
            const root1 = document.querySelector('d2l-sequence-viewer')?.shadowRoot;
            if (!root1) return null;

            const root2 = root1.querySelector('d2l-sequences-content-router')?.shadowRoot;
            if (!root2) return null;

            const root3 = root2.querySelector('d2l-sequences-content-link')?.shadowRoot;
            if (!root3) return null;

            // Get the iframe inside the final shadow root
            return root3.querySelector('iframe');
        }
        """)

    if not iframe_element:
        print("❌ Could not locate iframe inside shadow roots.")
        browser.close()
        exit()

    # Step 2: Switch context to iframe
    iframe = iframe_element.content_frame()
    if not iframe:
        print("❌ Could not switch to iframe content.")
        browser.close()
        exit()

    # Step 3: Wait for transcript content and extract
    iframe.wait_for_selector("#transcript-list li > span:first-child", timeout=10000)

    # Step 3.5: Scroll transcript list to load all lines
    iframe.evaluate("""
    () => {
        const container = document.querySelector('#transcript-list');
        if (!container) return;

        container.scrollTop = 0;
        const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

        let previousHeight = -1;
        let tries = 0;

        const scrollUntilEnd = async () => {
            while (tries < 20) {
                container.scrollTop = container.scrollHeight;
                await delay(300);  // wait for lazy content to load

                const currentHeight = container.scrollHeight;
                if (currentHeight === previousHeight) break;

                previousHeight = currentHeight;
                tries++;
            }
        };

        return scrollUntilEnd();
    }
    """)


    transcript_lines = iframe.eval_on_selector_all(
        "#transcript-list li > span:first-child",
        "spans => spans.map(span => span.textContent.trim())"
    )


    # 💾 Save to file
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(transcript_lines))

    print("✅ Transcript saved to transcript.txt")
    input("not closing...")
    # browser.close()