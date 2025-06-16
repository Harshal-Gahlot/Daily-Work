from playwright.sync_api import sync_playwright

user_data_dir = "C:/Users/samud/AppData/Local/Google/Chrome/User Data" # 🔁 Put your real path here

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False,
        args=["--start-maximized"]
    )
    page = browser.new_page()
    
    print("🔓 Use this real browser to navigate & log in fully.")
    input("✅ After you're on the content page with video/notes loaded, press ENTER...")

    with open("page.html", "w", encoding="utf-8") as f:
        f.write(page.content())

    print("📄 Page saved as 'page.html'")
