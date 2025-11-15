from playwright.sync_api import sync_playwright
import json
import time
from collections import OrderedDict

COOKIE_FILE = "cookies.json"
TARGET_URL = ""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # Load cookies
    with open(COOKIE_FILE, "r", encoding="utf-8") as f:
        raw_cookies = json.load(f)

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
            const root2 = root1?.querySelector('d2l-sequences-content-router')?.shadowRoot;
            const root3 = root2?.querySelector('d2l-sequences-content-link')?.shadowRoot;
            return root3?.querySelector('iframe');
        }
    """)

    if not iframe_element:
        print("❌ Could not locate iframe.")
        browser.close()
        exit()

    iframe = iframe_element.content_frame()
    if not iframe:
        print("❌ Could not switch to iframe content.")
        browser.close()
        exit()

    iframe.wait_for_selector("#transcript-list li", timeout=10000)

    print("🔁 Scrolling and capturing transcript...")

    # Use OrderedDict to preserve order
    transcript_dict = OrderedDict()
    scroll_attempts = 0
    max_scroll_attempts = 50
    last_total_lines = -1

    while scroll_attempts < max_scroll_attempts:
        print(f"🔄 Scroll attempt {scroll_attempts + 1}/{max_scroll_attempts}")
        items = iframe.eval_on_selector_all(
            "#transcript-list li",
            """els => els.map(li => {
                const spans = li.querySelectorAll("span");
                return spans.length >= 2
                    ? { timestamp: spans[1].textContent.trim(), text: spans[0].textContent.trim() }
                    : null;
            }).filter(Boolean)"""
        )

        print("items:", items)

        new_added = 0
        for item in items:
            print("for", item, "in items")
            if item["timestamp"] not in transcript_dict:
                print(item," not in transcript_dict.")
                transcript_dict[item["timestamp"]] = item["text"]
                new_added += 1

        if new_added == 0 and len(transcript_dict) == last_total_lines:
            print("breaking out...")
            break  # No new lines after scroll, probably done

        last_total_lines = len(transcript_dict)

        # Scroll down one screen worth
        iframe.evaluate("""
            () => {
                let el = document.querySelector('#transcript-list');
                while (el && el.parentElement) {
                    const style = getComputedStyle(el);
                    if (style.overflowY === 'scroll' || style.overflowY === 'auto') {
                        el.scrollBy(0, el.clientHeight * 0.9);
                        return;
                    }
                    el = el.parentElement;
                }
            }
        """)




        time.sleep(0.1)  # Give time for new lines to load
        scroll_attempts += 1

    with open("transcript.txt", "w", encoding="utf-8") as f:
        for ts, text in transcript_dict.items():
            f.write(f"{ts} {text}\n")

    print(f"✅ Transcript saved. Total lines: {len(transcript_dict)}")
    # input("Press ENTER to exit...")
    browser.close()
