import requests
from bs4 import BeautifulSoup
import os 
from dotenv import load_dotenv

load_dotenv()

my_token = os.getenv("TELEGRAM_BOT_TOKEN")
my_chat = os.getenv("TELEGRAM_CHAT_ID")

url = "https://news.ycombinator.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        all_news = soup.find_all(class_="titleline")

        for news in all_news [:5]:
            headline = news.get_text().strip()
            headline = news.get_text().strip()
            link_tag = news.find("a")
            link = link_tag.get("href")

            msg = f"top 5 news\nheadline: {headline}\nlink: {link}\n JOB DONE!"
            tele_url = f"https://api.telegram.org/bot{my_token}/sendMessage"
        
            requests.get(tele_url, params={"chat_id": my_chat, "text": msg})
            print("Telegram Sent!")
            
            print(f"📢 {headline}")
            print(f"🔗 {link}")
            print("-" * 20)

    else:
        print("❌ Server Error")


except Exception as e:
    print(f"ERROR : {e}")
    
