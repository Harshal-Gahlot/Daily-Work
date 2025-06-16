from playwright.sync_api import sync_playwright

# Use a dedicated folder for Playwright's browser data
user_data_dir = "H:/PROGRAMMING/Daily Code/python/playwright-profile"

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False,
        args=["--start-maximized"]
    )
    page = browser.new_page()

    print("🔓 Please login manually...")
    input("✅ After login and page load, press ENTER...")

    # Optionally navigate to specific page
    # page.goto("https://some_url")

    with open("page.html", "w", encoding="utf-8") as f:
        f.write(page.content())

    print("✅ Done. HTML saved to page.html.")
