import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"

st.title("Web Scraper & AI Analyzer")

# User input fields
url = st.text_input("Enter website URL", "")
goal = st.text_area("Describe your goal", "")

# Ensure session state variables exist
if "ai_response" not in st.session_state:
    st.session_state.ai_response = None
if "csv_download_ready" not in st.session_state:
    st.session_state.csv_download_ready = False

# Scrape button
if st.button("Scrape Website"):
    if not url or not goal:
        st.warning("⚠️ Please enter a URL and a goal.")
    else:
        with st.spinner("Scraping website and generating AI prompt..."):
            response = requests.post(f"{API_URL}/scrape", json={"url": url, "goal": goal})
            
            if response.status_code == 200:
                data = response.json()
                st.session_state.ai_response = data["ai_response"]  # Store AI response
                st.session_state.csv_download_ready = True  # Enable download button
            else:
                st.error("❌ Failed to scrape the website. Please try again.")

# Display AI-generated prompt if available
if st.session_state.ai_response:
    st.subheader("🔍 AI-Generated ChatGPT Prompt")
    st.write(st.session_state.ai_response)

# Show download button if scraping was successful
if st.session_state.csv_download_ready:
    st.download_button(
        label="📂 Download Scraped Data",
        data=requests.get(f"{API_URL}/download").content,
        file_name="scraped_data.csv",
        mime="text/csv"
    )