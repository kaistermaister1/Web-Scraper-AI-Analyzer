# 🕵️‍♂️ AI-Powered Web Scraper & Analyzer 🚀

## **📌 Overview**
This project is a **fully automated web scraper and AI-powered analyzer** that:
- Extracts **all text-based content** from any given website.
- Saves the data as a **structured CSV file**.
- Uses **OpenAI’s GPT-4 API** to generate a **custom ChatGPT prompt** based on user goals.
- Provides an **interactive frontend** using **Streamlit** for ease of use.

💡 **How to Use It:**
1. **Enter a website URL and a goal** (e.g., "Find internship opportunities").
2. **Scrape & download the website's content** as a **CSV file**.
3. **Copy the AI-generated prompt** and paste it into **a model of your choice (e.g., ChatGPT/GPT-4)**.
4. **Upload the CSV file** to the model to **analyze the extracted data**.

Developed **in a short timeframe using AI**, this project demonstrates **automation, AI-driven insights, and real-world scraping techniques**.

---
## **🎨 User Interface**
![Streamlit UI Preview](https://github.com/kaistermaister1/Web-Scraper-AI-Analyzer/blob/main/screenshot.png?raw=true)
---

## **🔧 Technologies Used**
| **Technology** | **Purpose** |
|---------------|------------|
| **Python** | Core programming language |
| **Flask** | Backend API for handling requests |
| **Streamlit** | Frontend UI for user interaction |
| **BeautifulSoup** | HTML parsing & web scraping |
| **OpenAI API (GPT-4o)** | AI-driven content analysis |
| **Pandas** | CSV data handling |

---

## **🎯 Features**
✅ **Scrape any website** and extract structured text data  
✅ **Download scraped content as a CSV file**  
✅ **AI-generated analysis prompts** for ChatGPT  
✅ **User-friendly Streamlit interface**  

---

## **🚀 How It Works**
1. **User Inputs**:
   - Enters a **website URL**.
   - Describes their **goal** (e.g., "Find all internship opportunities").
   
2. **Backend Processing**:
   - Scrapes the entire website and **saves content** in CSV.
   - Sends the user’s goal to **OpenAI GPT-4o** to generate a **smart ChatGPT prompt**.

3. **Frontend Output**:
   - Displays the **AI-generated analysis prompt**.
   - Provides a **CSV download button** for the scraped data.

---

## **📥 Installation & Setup**

### **1️⃣ Clone the Repository**
git clone https://github.com/YOUR-USERNAME/web-scraper-ai-analyzer.git
cd web-scraper-ai-analyzer

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run the Flask Backend
python scrape_backend.py

### 4️⃣ Run the Streamlit Frontend
streamlit run app.py
