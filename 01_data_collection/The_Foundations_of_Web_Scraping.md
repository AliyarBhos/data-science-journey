# Web Scraping Foundations

> Comprehensive Notes – Part 1

---

# Table of Contents

1. Introduction
2. What is Web Scraping?
3. Why Web Scraping Exists
4. Real-World Applications
5. How the Internet Works
6. Client and Server
7. HTTP & HTTPS
8. Requests and Responses
9. URLs
10. Domains, Websites, and Webpages
11. HTTP Methods
12. HTTP Status Codes
13. HTML
14. CSS
15. JavaScript
16. Static vs Dynamic Websites
17. Frontend vs Backend
18. Typical Web Scraping Workflow
19. Ethical & Legal Considerations
20. Python Libraries for Web Scraping
21. Summary

---

# 1. Introduction

Web scraping is one of the most useful skills in data science, machine learning, business intelligence, and automation.

Many valuable datasets are not readily available for download. Instead of manually copying information from websites, we can automate the entire process.

A web scraper is simply a program that visits a website, reads its contents, extracts specific information, and stores it in a structured format such as CSV, JSON, or a database.

---

# 2. What is Web Scraping?

**Definition**

Web scraping is the automated process of extracting information from websites.

Instead of this:

```
Open website
↓

Copy information
↓

Paste into Excel
↓

Repeat 10,000 times
```

A scraper performs:

```
Open website
↓

Download webpage
↓

Extract required information
↓

Store it automatically
```

Example:

Website:

```
Product:
iPhone 17

Price:
$999

Rating:
4.8
```

Scraped result:

```json
{
    "product": "iPhone 17",
    "price": 999,
    "rating": 4.8
}
```

---

# 3. Why Web Scraping Exists

Not all information is available as downloadable datasets.

Suppose you need:

- Movie ratings
- House prices
- Job postings
- Weather history
- Football statistics
- Product prices

Many websites display this information but don't offer downloads.

Instead of manually collecting thousands of pages, web scraping automates the process.

---

# 4. Real-World Applications

## Data Science

Collect:

- Housing prices
- Weather data
- Population statistics
- Financial information
- Government data

---

## Machine Learning

Many ML datasets are created through scraping.

Examples:

- Image datasets
- Text corpora
- Product descriptions
- News articles

---

## Natural Language Processing (NLP)

Researchers scrape:

- News websites
- Forums
- Blogs
- Wikipedia
- Reddit discussions

---

## Business Intelligence

Companies monitor competitors.

Example:

```
Every hour

↓

Visit competitor website

↓

Collect product prices

↓

Compare with own prices

↓

Generate reports
```

---

## Academic Research

Researchers scrape:

- Scientific publications
- Election data
- Public government records
- Newspaper archives

---

# 5. How the Internet Works

Every time you visit a website:

```
Browser

↓

Internet

↓

Server

↓

Response

↓

Browser displays webpage
```

This happens in milliseconds.

---

# 6. Client and Server

## Client

The client is the program requesting information.

Examples:

- Chrome
- Firefox
- Edge
- Safari

Your browser is the client.

---

## Server

The server stores:

- webpages
- databases
- images
- videos

and responds to client requests.

---

Restaurant analogy:

Customer = Client

Kitchen = Server

---

# 7. HTTP & HTTPS

HTTP stands for:

**HyperText Transfer Protocol**

It is the communication language used between browsers and servers.

Example:

```
Client:
Can I have this webpage?

Server:
Sure.
```

HTTPS is the secure version.

It encrypts communication.

Today almost every website uses HTTPS.

---

# 8. Requests and Responses

## Request

The browser asks for something.

Example:

```
GET /
```

---

## Response

The server replies.

Example:

```
200 OK

<html>
...
</html>
```

The browser then renders the HTML.

---

# 9. URLs

URL stands for:

**Uniform Resource Locator**

Example:

```
https://example.com/products/phones?page=2
```

Breakdown:

Protocol

```
https
```

Domain

```
example.com
```

Path

```
/products/phones
```

Query Parameters

```
?page=2
```

---

# 10. Domain vs Website vs Webpage

Example:

```
https://amazon.com
```

Domain

```
amazon.com
```

Website

Entire Amazon platform.

Webpage

One individual page.

Example:

```
https://amazon.com/product/iphone17
```

---

# 11. HTTP Methods

## GET

Retrieve information.

Most web scraping uses GET requests.

---

## POST

Send information.

Examples:

- Login forms
- Registration
- Comments

---

## PUT

Update existing data.

---

## DELETE

Remove existing data.

---

# 12. HTTP Status Codes

## 200

Success.

---

## 301

Permanent redirect.

---

## 302

Temporary redirect.

---

## 403

Forbidden.

The server refuses access.

---

## 404

Page not found.

---

## 429

Too many requests.

You are sending requests too quickly.

---

## 500

Internal server error.

Problem on the website itself.

---

# 13. HTML

HTML stands for:

**HyperText Markup Language**

HTML defines the structure of webpages.

Example:

```html
<html>

<head>
<title>My Website</title>
</head>

<body>

<h1>Hello</h1>

<p>This is a paragraph.</p>

</body>

</html>
```

HTML contains:

- headings
- paragraphs
- images
- tables
- buttons
- links

Think of HTML as the skeleton of a webpage.

---

# 14. CSS

CSS stands for:

**Cascading Style Sheets**

CSS controls appearance.

Example:

```css
h1{

color:red;

font-size:40px;

}
```

Without CSS, webpages would look plain and unstyled.

Think of CSS as clothing and decoration.

---

# 15. JavaScript

JavaScript adds behavior.

Examples:

- animations
- buttons
- infinite scrolling
- dropdown menus
- interactive charts
- dynamic content

Without JavaScript, modern websites would be mostly static.

Think of JavaScript as the brain that makes webpages interactive.

---

# 16. Static vs Dynamic Websites

## Static Website

Server immediately sends complete HTML.

```
Browser

↓

Request

↓

Server

↓

Complete HTML

↓

Browser
```

Example HTML:

```html
<h1>iPhone</h1>

<p>$999</p>
```

BeautifulSoup can immediately extract the information.

---

## Dynamic Website

The server sends only a minimal HTML page.

JavaScript later loads the real content.

```
Browser

↓

Request

↓

Server

↓

Minimal HTML

↓

JavaScript runs

↓

Additional requests

↓

Content appears
```

Example initial HTML:

```html
<div id="app"></div>
```

BeautifulSoup only sees this empty container.

This is why many modern websites require browser automation tools.

---

# 17. Frontend vs Backend

## Frontend

Everything visible to users.

Examples:

- buttons
- menus
- images
- forms
- colors

---

## Backend

Hidden server-side logic.

Responsible for:

- databases
- authentication
- payments
- calculations
- APIs

---

Example:

Instagram

Frontend:

❤️ Like button

Backend:

Increase like count

↓

Update database

↓

Notify owner

---

# 18. Typical Web Scraping Workflow

```
Choose Website

↓

Inspect Page

↓

Send HTTP Request

↓

Receive HTML

↓

Parse HTML

↓

Locate Elements

↓

Extract Data

↓

Clean Data

↓

Save Results
```

---

# 19. Ethical & Legal Considerations

Always scrape responsibly.

Good practices include:

- Respect website Terms of Service.
- Use official APIs whenever available.
- Avoid sending requests too rapidly.
- Never overload servers.
- Respect robots.txt as guidance.
- Never bypass authentication or security measures.

Responsible scraping protects both your reputation and website stability.

---

# 20. Python Libraries for Web Scraping

## requests

Downloads webpages.

---

## BeautifulSoup

Parses HTML and extracts elements.

---

## lxml

Very fast HTML/XML parser.

---

## Scrapy

Industrial-strength scraping framework.

Suitable for very large projects.

---

## Selenium

Controls a real browser.

Useful for JavaScript-heavy websites.

---

## Playwright

Modern browser automation.

Often faster and more reliable than Selenium.

---

## pandas

Stores scraped data in tables.

Exports to:

- CSV
- Excel
- SQL

---

## json

Stores structured data.

---

## csv

Writes CSV files.

---

# 21. Summary

Before writing your first scraper, you should understand:

- What web scraping is
- Why it is useful
- Client-server architecture
- HTTP and HTTPS
- Requests and responses
- URLs
- Domains and webpages
- HTTP methods
- HTTP status codes
- HTML
- CSS
- JavaScript
- Static vs dynamic websites
- Frontend vs backend
- The complete scraping workflow
- Ethical scraping practices
- Common Python scraping libraries

These concepts form the foundation for all web scraping projects.


# Web Scraping Foundations - Part 3

# HTML Attributes, CSS Selectors & Browser Developer Tools

---

# Table of Contents

1. Why Attributes Exist
2. HTML Attributes
3. Common HTML Attributes
4. The class Attribute
5. The id Attribute
6. Other Important Attributes
7. Nested Attributes
8. Browser Developer Tools
9. Inspect Element
10. CSS Selectors
11. Types of CSS Selectors
12. Selector Priority
13. CSS Selector Examples
14. Chrome DevTools Search
15. BeautifulSoup vs CSS Selectors
16. Summary

---

# 1. Why Attributes Exist

Suppose you have a webpage like this:

```html
<button>Login</button>

<button>Register</button>

<button>Cancel</button>
```

Imagine you're writing code.

How do you know which button is which?

The browser has the same problem.

Buttons need extra information.

That's where attributes come in.

---

# 2. HTML Attributes

Attributes provide additional information about HTML elements.

General syntax:

```html
<tag attribute="value">
```

Example

```html
<img src="cat.jpg">
```

The tag is

```
img
```

The attribute is

```
src
```

The value is

```
cat.jpg
```

---

# General Structure

```html
<tag attribute="value">

Content

</tag>
```

Example

```html
<a href="https://google.com">

Google

</a>
```

Tag

```
a
```

Attribute

```
href
```

Value

```
https://google.com
```

Content

```
Google
```

---

# Multiple Attributes

Elements may have several attributes.

Example

```html
<img

src="phone.jpg"

alt="Phone"

width="500"

height="400"

class="product"

id="phone1"

>
```

One element.

Many attributes.

---

# 3. Common HTML Attributes

| Attribute | Purpose |
|------------|----------|
| class | Groups elements |
| id | Unique identifier |
| href | Link destination |
| src | Image/video source |
| alt | Alternative image text |
| title | Tooltip |
| style | Inline CSS |
| value | Input value |
| name | Form identifier |
| type | Input type |
| placeholder | Placeholder text |
| disabled | Disable element |

These appear on nearly every website.

---

# 4. The class Attribute

This is probably the most important attribute in web scraping.

Example

```html
<div class="product">

iPhone

</div>
```

Another

```html
<div class="product">

Samsung

</div>
```

Another

```html
<div class="product">

Google Pixel

</div>
```

Notice

Every product shares

```
class="product"
```

Classes group similar elements.

Think of them like categories.

---

# Real Example

Imagine an online shop.

```
Product

↓

Product

↓

Product

↓

Product
```

Every product card uses

```html
class="product"
```

BeautifulSoup can easily collect them all.

---

# Multiple Classes

An element can belong to several classes.

Example

```html
<div class="product featured sale">

Phone

</div>
```

This element belongs to

- product
- featured
- sale

simultaneously.

---

# 5. The id Attribute

Unlike classes,

IDs should be unique.

Example

```html
<div id="header">

</div>

<div id="footer">

</div>
```

Only one

```
header
```

Only one

```
footer
```

Think of IDs as passport numbers.

Every person has one unique passport.

---

# Difference Between Class and ID

Class

```
Many elements
```

ID

```
Exactly one element
```

Example

```
Students

↓

All belong to class "student"

↓

Each has a unique student ID
```

---

# 6. Other Important Attributes

## href

Destination of hyperlinks.

```html
<a href="https://openai.com">

OpenAI

</a>
```

---

## src

Location of images.

```html
<img src="cat.jpg">
```

---

## alt

Alternative description.

```html
<img

src="cat.jpg"

alt="Cute cat"

>
```

Useful for accessibility.

---

## title

Tooltip.

```html
<button title="Delete">

Delete

</button>
```

---

## value

Input value.

```html
<input value="Ali">
```

---

## placeholder

Hint shown before typing.

```html
<input

placeholder="Enter email"

>
```

---

## type

Specifies input type.

```html
<input type="password">
```

or

```html
<input type="email">
```

---

# 7. Nested Attributes

Example

```html
<div class="product">

<img src="phone.jpg">

<h2>iPhone</h2>

<p class="price">

$999

</p>

</div>
```

Notice

The div has

```
class
```

Image has

```
src
```

Paragraph has

```
class
```

Every element may have different attributes.

---

# 8. Browser Developer Tools

Every web scraper should master Developer Tools.

Shortcut:

Windows

```
F12
```

or

```
Ctrl + Shift + I
```

Mac

```
Cmd + Option + I
```

Developer Tools allow you to inspect the actual HTML sent to the browser.

---

# 9. Inspect Element

Right click

↓

Inspect

Example

```
Amazon Product

↓

Right Click

↓

Inspect
```

Chrome immediately highlights

```html
<div class="product">

...

</div>
```

This is one of the fastest ways to locate the data you want.

---

# 10. CSS Selectors

CSS selectors describe how to locate HTML elements.

Think of them as addresses.

Instead of saying

```
Find everything.
```

You say

```
Find every paragraph.

Find every image.

Find the product with ID "main".

Find all prices.
```

---

# 11. Types of CSS Selectors

## Tag Selector

```css
p
```

Selects

```html
<p>

<p>

<p>
```

---

## Class Selector

```css
.product
```

Notice the dot.

Matches

```html
<div class="product">
```

---

## ID Selector

```css
#header
```

Notice the #

Matches

```html
<div id="header">
```

---

## Descendant Selector

```css
.product p
```

Means

Find every paragraph

inside

product.

---

## Child Selector

```css
.product > p
```

Only direct children.

---

## Multiple Classes

```css
.product.sale
```

Matches

```html
<div class="product sale">
```

---

## Attribute Selector

```css
img[src]
```

Every image with

```
src
```

---

Another

```css
input[type="password"]
```

Find password boxes.

---

# 12. Selector Priority

Suppose

```html
<div

class="product"

id="phone"

>
```

Possible selectors

```
div
```

or

```
.product
```

or

```
#phone
```

The ID selector is the most specific because IDs are intended to be unique.

---

# 13. CSS Selector Examples

Example HTML

```html
<div class="product">

<h2>

iPhone

</h2>

<p class="price">

$999

</p>

</div>
```

Possible selectors

```
div

.product

h2

.price

.product h2

.product .price
```

Each one selects something different.

---

# 14. Chrome DevTools Search

Inside DevTools

Press

```
Ctrl + F
```

Now search

```
product
```

or

```
.price
```

or

```
#header
```

Chrome jumps directly to matching HTML.

This is extremely useful for scraping.

---

# 15. BeautifulSoup vs CSS Selectors

BeautifulSoup understands CSS selectors.

Example

```python
soup.select(".product")
```

means

Find every element whose class is

```
product
```

Another

```python
soup.select("#header")
```

Find the element whose ID is

```
header
```

Another

```python
soup.select("img")
```

Find every image.

BeautifulSoup simply applies CSS selector rules to the HTML tree.

---

# 16. Summary

Before writing your first scraper, you should be comfortable with:

- HTML attributes
- class vs id
- href
- src
- alt
- title
- placeholder
- value
- Browser Developer Tools
- Inspect Element
- CSS selectors
- Tag selectors
- Class selectors
- ID selectors
- Descendant selectors
- Child selectors
- Attribute selectors

These concepts are the bridge between HTML and BeautifulSoup. Once you know how to inspect a webpage and identify the correct CSS selector, extracting data becomes much easier.