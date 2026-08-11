from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def get_rendered_html(url, wait_selector=None):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        if wait_selector:
            page.wait_for_selector(wait_selector, timeout=10000)
        html = page.content()
        browser.close()
        return html


if __name__ == '__main__':
    html = get_rendered_html('http://quotes.toscrape.com/js/', wait_selector='span.text')
    print('Lenght of html', len(html))

    soup = BeautifulSoup(html, 'html.parser')
    quotes = soup.find_all('span', class_='text')
    print('Count of qoutes', len(quotes))

    for i in quotes[:3]:
        print(i.text)