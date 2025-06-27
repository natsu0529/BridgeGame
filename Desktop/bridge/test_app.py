import streamlit as st
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Bridge Test", page_icon="🃏")

st.title("🃏 Bridge Game Test")
st.write("Testing basic Streamlit functionality...")

# 環境変数テスト
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

if api_key:
    st.success(f"✅ API Key loaded (length: {len(api_key)})")
else:
    st.error("❌ API Key not found")

# 基本的なウィジェットテスト
if st.button("Test Button"):
    st.write("Button clicked!")

col1, col2, col3 = st.columns(3)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")
with col3:
    st.write("Column 3")

st.write("Test completed.")
