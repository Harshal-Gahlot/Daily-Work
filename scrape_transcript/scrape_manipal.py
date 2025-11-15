from playwright.sync_api import sync_playwright

email = "" 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Opening login page...")
    page.goto("") # enter the link

    # Fill UIN/email
    page.fill('input[type="email"]', email)

    
    print("Please finish login manually (SSO, password, etc.)")
    input("👉 Press ENTER once you're logged in and have manually clicked into the video/content page...")

    print("✅ Now saving HTML content of the current page...")

    # print("Please finish login manually (password, SSO, etc)...")
    # input("Press ENTER here when you're fully logged in and on dashboard...")

    # # Now go to target course page
    # target_url = ""
    # page.goto(target_url)
    # page.wait_for_load_state("networkidle")

    # print("Now at the course page.")
    # print("Page title:", page.title())
    # print("Saving HTML to file...")

    # input("Press ENTER here when you're fully logged in and on dashboard...")

    with open("page.html", "w", encoding="utf-8") as f:
        f.write(page.content())


    print("✅ Saved as 'page.html'. You can now inspect or extract elements.")
    # browser.close()