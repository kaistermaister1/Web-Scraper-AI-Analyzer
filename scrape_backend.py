from flask import Flask, request, jsonify, send_file
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from openai import OpenAI
import os

app = Flask(__name__)

# OpenAI API Key (Replace with a secure method if needed)
client = OpenAI(api_key='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',)
def scrape_website(url):
    visited_urls = set()
    data = []

    def scrape_page(url):
        if url in visited_urls:
            return
        visited_urls.add(url)

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            response = requests.get(url, headers=headers, timeout=30, verify=False)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"❌ Failed to fetch {url}: {e}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "No Title"
        text = " ".join([p.get_text() for p in soup.find_all("p")])  # Extract paragraph text

        if text.strip():  # ✅ Only save if there's actual text
            print(f"✅ Scraped: {url}")  # Debugging line
            print(f"📄 Extracted text preview: {text[:200]}...\n")  # Show first 200 chars
            data.append({"URL": url, "Title": title, "Text": text})
        else:
            print(f"⚠️ No readable text found on {url}")

        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link["href"])
            parsed_url = urlparse(full_url)
            if urlparse(url).netloc == parsed_url.netloc:
                scrape_page(full_url)

    scrape_page(url)

    if not data:
        print("❌ No data was scraped. The website might be blocking the scraper.")
    else:
        df = pd.DataFrame(data)
        df.to_csv("scraped_data.csv", index=False, encoding="utf-8")
        print("✅ Scraped data saved to scraped_data.csv")
    
def generate_ai_summary(user_goal):
    try:
        prompt = f"I scraped an entire website and saved the data into a CSV file. The user is interested in: {user_goal}. Please generate a concise prompt they can copy into ChatGPT to analyze the data effectively. Make sure the response you generate is the prompt they can copy paste, and nothing else."

        # Create a chat completion with the file content as the user's message
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt},
            ],
            model="gpt-4o",
        )

        # Extract and return the generated text from the API response
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating AI response: {e}"

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.json
    url = data.get("url")
    user_goal = data.get("goal")

    if not url or not user_goal:
        return jsonify({"error": "URL and goal description are required"}), 400

    csv_file = scrape_website(url)
    ai_response = generate_ai_summary(user_goal)

    return jsonify({"csv_file": csv_file, "ai_response": ai_response})

@app.route("/download")
def download_file():
    return send_file("scraped_data.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)