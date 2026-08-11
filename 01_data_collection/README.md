# 01_data_collection — Web Scraping Fundamentals

This folder documents a structured, from-first-principles progression through web scraping —
from raw HTTP requests to JavaScript-rendered pages and scaling techniques. Each level builds
directly on the one before it, moving from "what actually happens when you fetch a webpage"
to a production-shaped, respectful, fault-tolerant scraper.

The goal throughout was to understand *why* each tool and technique exists — not just how to
call it — by first hitting the problem it solves (manually, or via a real error) before
introducing the fix.

## Contents

| File | Level | Description |
|---|---|---|
| `The_Foundations_of_Web_Scraping.md` | — | Conceptual primer: what HTML/HTTP/DNS/TCP/TLS actually are, and how a request travels across the internet before any scraping code runs. |
| `level1_scraper.ipynb` | 1 | Fetching a page with `requests`; understanding headers, the `Response` object, status codes, and raw HTML text. |
| `level2_scraper.ipynb` | 2 | Parsing HTML into a real tree with BeautifulSoup; `.find()` / `.find_all()`; searching by tag, class, and attribute; why manual string search (`.find('<title>')`) breaks down. |
| `level3_scraper.ipynb` | 3 | Crawling a full site: the list → detail page pattern, pagination via `urljoin`, looping until no "next" link, collecting structured data instead of printing. |
| `level4_scraper.ipynb` | 4 | Production robustness: `robots.txt` parsing and compliance, timeouts, `raise_for_status()`, retries with exponential backoff, `requests.Session()`, randomized delays, and crash-safe incremental CSV writing. |
| `level5_scraper.ipynb` / `level5_scraper.py` | 5 | JavaScript-rendered pages: diagnosing server-rendered vs. client-rendered content, extracting inline JSON from `<script>` tags via regex, and full browser automation with Playwright. The `.py` version exists because Playwright's sync API cannot run inside Jupyter's background asyncio event loop on Windows — this is a real, documented environment constraint, not a stylistic choice. |
| `level6_scraper.ipynb` | 6 | Scaling techniques: concurrent requests with `ThreadPoolExecutor`, an introduction to the Scrapy framework (spiders, selectors, `yield`-based item pipelines, built-in retries/robots.txt/throttling), and notes on structured storage, deduplication, and logging for long-running jobs. |
| `books_from_toscrape_com.csv` | 3–4 | Output dataset: full book catalog (title, price) scraped from [books.toscrape.com](http://books.toscrape.com), collected via the Level 3/4 pagination-crawling scraper. |

## What each level covers, in more detail

### Level 1 — HTTP Fundamentals
- `requests.get(url, headers=..., timeout=...)`
- Why a custom `User-Agent` header matters (default `python-requests/x.x` is an instant bot signal)
- The `Response` object: `.status_code`, `.headers`, `.text` vs `.content`, `.url`
- Reading raw response bytes conceptually (status line → headers → blank line → body)

### Level 2 — Parsing with BeautifulSoup
- Why HTML is a tree, not a flat string — and why regex/`.find()` string-searching fails on nested/variable structure
- Building the parse tree: `BeautifulSoup(html, 'html.parser')`
- `soup.find()` vs `soup.find_all()`, tag objects, `.text`, `.get('attr')` / `tag['attr']`
- Searching by class (`class_='...'`, or `attrs={'class': '...'}`) and why `class_` exists (`class` is a reserved Python keyword)
- Using browser DevTools ("Inspect Element") to find real tag/class names — no class name should ever be guessed
- Caution around auto-generated/hashed CSS class names (`css-1a2b3c`) vs. stable selectors (semantic tags, `id`, meaningful class names)

### Level 3 — Site-Wide Crawling
- The list page → detail page pattern (repeating container elements, e.g. `<article class="product_pod">`)
- Following pagination via `urljoin(base_url, relative_href)` — correctly resolving relative URLs
- Loop termination via presence/absence of a "next" link (`while url:`)
- Collecting structured records (`list[dict]`) instead of printing
- Basic politeness: `time.sleep()` between requests

### Level 4 — Robustness & Politeness
- `robots.txt`: fetching and parsing with `urllib.robotparser.RobotFileParser`, `can_fetch(user_agent, url)`, and reading real `Disallow`/`Allow`/`Content-Signal` directives (using iFixit's live `robots.txt` as a worked example, including per-bot rules and why paths like `/Search` are commonly disallowed)
- Timeouts (`timeout=...`) to prevent indefinite hangs
- `response.raise_for_status()` and `try/except requests.exceptions.RequestException` for clean error handling
- Diagnosing real failures by class: DNS resolution errors, TLS/certificate errors, transient 5xx errors (e.g. distinguishing an application-level error from an upstream load balancer's `503`)
- Retries with exponential backoff
- `requests.Session()` for connection reuse and shared cookies across many requests to the same host
- Randomized delay ranges (`random.uniform(1, 3)`) instead of fixed sleeps
- Crash-safe incremental saving: writing/flushing each page's results to disk immediately, rather than holding everything in memory until the end

### Level 5 — JavaScript-Rendered Pages
- Diagnosing server-rendered vs. client-rendered pages (raw response length/content check, and the reliable DevTools "disable JavaScript and reload" test)
- Why `requests` + BeautifulSoup structurally cannot see content that JavaScript builds after page load (a substring existing in raw response text ≠ that content existing as real HTML structure)
- Extracting inline embedded JSON from a `<script>` tag via `re.search(..., re.DOTALL)` + `json.loads()`, as a lightweight alternative to full browser automation when data happens to be embedded directly
- Full browser automation with **Playwright**: `sync_playwright()`, `browser.new_page()`, `page.goto()`, `page.content()`, `page.wait_for_selector()` vs. blind `time.sleep()`
- Documented environment troubleshooting: Playwright's sync API cannot run inside an already-running asyncio loop (Jupyter always has one); the async API alternative then fails on Windows specifically because Jupyter's default `SelectorEventLoop` cannot spawn subprocesses, which Playwright's browser driver requires. Resolved by running Playwright from a standalone `.py` script instead of a notebook.
- The practical decision order for real projects: (1) does plain `requests` work? → (2) is there a hidden JSON API in DevTools' Network/Fetch-XHR tab you can call directly? → (3) only then, full browser automation

### Level 6 — Scaling Up
- Concurrency with `concurrent.futures.ThreadPoolExecutor` to run multiple requests in parallel, with the explicit caveat that concurrency increases the risk of overwhelming a server and must still be paired with reasonable `max_workers`, delays, and retry logic
- **Scrapy** as a framework: project structure (`scrapy startproject`), spiders (`scrapy genspider`), CSS selectors (`response.css(...)`), `yield`-based item generation, `response.follow()` for automatic relative-URL pagination, and built-in `robots.txt` compliance, throttling, retries, and deduplication that replace the hand-built Level 4 logic
- Notes on structured storage (SQLite/Postgres over flat files at scale), deduplication on re-runs, and the `logging` module for unattended long-running jobs

## Environment Notes

- Python packages used: `requests`, `beautifulsoup4`, `lxml` (optional, faster parser), `playwright`, `scrapy`
- Playwright requires a separate one-time browser install after `pip install`:
  ```bash
  playwright install chromium
  ```
- On Windows, run Playwright scripts as standalone `.py` files (`python level5_scraper.py`), not inside Jupyter — see Level 5 notes above.

## Tools/Sites Used for Practice

- [books.toscrape.com](http://books.toscrape.com) — static, purpose-built practice site (Levels 3, 4, 6/Scrapy)
- [quotes.toscrape.com](http://quotes.toscrape.com) / `/js/` variant — server-rendered vs. JS-rendered comparison (Level 5)
- [ifixit.com](https://www.ifixit.com) — real-world site used to practice reading a live, complex `robots.txt` (Level 4)
- [httpbin.org](https://httpbin.org) — controlled endpoint for simulating timeouts and error status codes (Level 4)

## Status

All six levels complete. Next: applying this skill set to real data-collection projects rather than
further isolated exercises.