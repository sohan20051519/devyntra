from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:3000/verification")

    # Expect the heading to be visible to ensure the page has loaded
    expect(page.get_by_role("heading", name="Badge Component Verification")).to_be_visible()

    page.screenshot(path="/app/jules-scratch/verification/badge_verification.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)