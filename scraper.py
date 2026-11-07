from playwright.sync_api import sync_playwright
import time
import re


def search_and_scrape(query, limit):
    url = f"https://divar.ir/s/tehran?q={query}"

    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('a[href^="/v/"]')
        time.sleep(3)

        cards = page.locator('a[href^="/v/"]')
        total = cards.count()

        links = []
        seen = set()

        for i in range(total):
            href = cards.nth(i).get_attribute("href")
            if not href:
                continue
            if href.startswith("/"):
                href = "https://divar.ir" + href
            if href not in seen:
                seen.add(href)
                links.append(href)
            if len(links) >= limit:
                break

        detail = browser.new_page()

        for link in links:
            detail.goto(link)
            time.sleep(2)

            try:
                title = detail.locator("h1").first.inner_text().strip()
            except:
                title = ""

            data.append({
                "title": title,
                "link": link
            })

        browser.close()

    return data
