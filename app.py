import openai
import streamlit as st

# Use secret key from Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

st.set_page_config(page_title="👕 AI Outfit Stylist", layout="centered")
st.title("👕 AI Outfit Stylist")
st.markdown("Get matching outfit ideas and images for Indian skin tone and style.")

query = st.text_input("🧥 Describe your outfit need (e.g. cream pant, white shirt):")

if query:
    with st.spinner("Styling your look..."):
        chat = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a fashion stylist for Indian men."},
                {"role": "user", "content": query}
            ]
        )
        suggestion = chat['choices'][0]['message']['content']
        st.subheader("🎯 Outfit Suggestion:")
        st.write(suggestion)

    if st.button("🖼️ Generate Outfit Image"):
        with st.spinner("Creating image..."):
            image = openai.Image.create(
                prompt=f"Stylish outfit for Indian man: {query}",
                n=1,
                size="512x512"
            )
            image_url = image['data'][0]['url']
            st.image(image_url, caption="AI Generated Outfit")
