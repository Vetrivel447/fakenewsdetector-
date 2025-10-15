
import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
if api_key:
    client = genai.Client(api_key=api_key)
else:
    st.error("❌ Gemini API key not found. Add it to .env file.")

# Streamlit App UI
st.set_page_config(page_title="Fake News Detector for Students", layout="wide")
st.title("📰 Fake News Detector for Students")
st.write(
    "Misinformation spreads quickly online. Paste an article below and let our AI analyze it for credibility and provide a concise summary."
)

# User input
news_input = st.text_area("Paste the news article or link here:", height=250)

if st.button("Analyze"):
    if not news_input.strip():
        st.warning("Please enter a news article or link to analyze.")
    else:
        try:
            # Wrap the input in an analysis prompt
            prompt = (
                "You are an AI that detects fake news. "
                "Analyze the following news article for credibility, "
                "determine whether it is Fake, Likely Fake, or Reliable, "
                "and provide a concise, trustworthy summary.\n\n"
                f"Article:\n{news_input}"
            )

            # Gemini API call
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=[prompt]
            )

            result = response.text

            # Display results
            st.subheader("AI Analysis Result")
            st.info(result)

        except Exception as e:
            st.error(f"Error analyzing the article: {e}")
