import streamlit as st
import urllib.parse

# Page configuration
st.set_page_config(page_title="Penguin AI", page_icon="🐧")

# Branding (Pengu hatakar Penguin AI kar diya)
st.title("🐧 Penguin AI")
st.subheader("Unlimited & Free AI Wallpapers")

# Input box
prompt = st.text_input("Enter your wallpaper idea (e.g., A cyberpunk city):", "")

if st.button("Generate Wallpaper"):
    if prompt:
        # Prompt encoding
        encoded_prompt = urllib.parse.quote(prompt)
        
        # Pollinations AI URL
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1080&height=1920&nologo=true"
        
        # Displaying the actual image
        st.image(image_url, caption=f"Created by Penguin AI", use_container_width=True)
        
        # Download link
        st.markdown(f"### [Download Wallpaper]({image_url})")
    else:
        st.warning("Please enter a prompt first!")

st.info("Tip: Mention colors and lighting for better results.")
