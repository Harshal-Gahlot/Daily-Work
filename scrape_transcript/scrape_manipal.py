from playwright.sync_api import sync_playwright

uin_email = "2414503623@mujonline.edu.in" 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Opening login page...")
    page.goto("https://learning.onlinemanipal.com")

    # Fill UIN/email
    page.fill('input[type="email"]', uin_email)

    
    print("Please finish login manually (SSO, password, etc.)")
    input("👉 Press ENTER once you're logged in and have manually clicked into the video/content page...")

    print("✅ Now saving HTML content of the current page...")

    # print("Please finish login manually (password, SSO, etc)...")
    # input("Press ENTER here when you're fully logged in and on dashboard...")

    # # Now go to target course page
    # target_url = "https://learning.onlinemanipal.com/d2l/le/enhancedSequenceViewer/14270?url=https%3A%2F%2F0ff6df2b-fb79-4be6-9d7f-9428edd0fa0a.sequences.api.brightspace.com%2F14270%2Factivity%2F723958%3FfilterOnDatesAndDepth%3D1"
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