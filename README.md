# Tech News Scraper

An automated Python bot that scrapes the latest trending tech stories from **Hacker News (YCombinator)** and sends a clean summary to your Telegram.

## Features
* **Web Scraping:** Extracts headlines and links using `BeautifulSoup`.
* **Smart Filtering:** Fetches only the top 5 trending stories.
* **Batch Notification:** Consolidates all news into a single organized Telegram message (no spamming).
* **Security:** Uses `.env` to protect API keys.

## Tech Stack
* **Python 3**
* **BeautifulSoup4** (Web Scraping)
* **Requests** (HTTP Calls)
* **Telegram Bot API**

## How it Works
1. Connects to `news.ycombinator.com`.
2. Parses HTML to find the `titleline` class.
3. Extracts the headline and the article link.
4. Formats a message and sends it via Telegram Bot.

## Author
**shubham-s-dev**
