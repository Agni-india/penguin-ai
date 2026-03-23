import streamlit as st
import urllib.parse

# 1. Page Configuration
st.set_page_config(page_title="Penguin AI", page_icon="🐧", layout="wide")

# 2. Monkeytype Inspired Themes (CSS)
theme = st.sidebar.selectbox("🎨 Switch Theme", ["Dark Ocean", "Neon Frost", "Carbon", "Sakura"])

themes = {
    "Dark Ocean": {"bg": "#0f172a", "text": "#38bdf8", "btn": "#1d4ed8"},
    "Neon Frost": {"bg": "#000000", "text": "#00f2ff", "btn": "#008cff"},
    "Carbon": {"bg": "#121212", "text": "#e5e5e5", "btn": "#333333"},
    "Sakura": {"bg": "#1f1111", "text": "#ffb7c5", "btn": "#fb7185"}
}

active = themes[theme]

st.markdown(f"""
    <style>
    .stApp {{ background-color: {active['bg']}; color: {active['text']}; }}
    .stButton>button {{
        width: 100%; border-radius: 8px; height: 3.5em; 
        background-color: {active['btn']}; color: white;
        border: 2px solid {active['text']}; font-weight: bold; transition: 0.3s;
    }}
    .stButton>button:hover {{ transform: scale(1.02); border: 2px solid white; }}
    input {{ background-color: #1e293b !important; color: white !important; border: 1px solid {active['text']} !important; }}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Info
with st.sidebar:
    st.title("🐧 Penguin AI")
    st.write("The Ultimate AI Engine")
    st.divider()
    st.caption("Safe Search Enabled ✅")
    st.caption("No Login Required 🚀")

# 4. Main Interface
st.title("🐧 Penguin AI")
st.markdown(f"#### <span style='color:{active['text']}'>Create High-End Wallpapers Instantly</span>", unsafe_allow_html=True)

prompt = st.text_input("", placeholder="Describe your masterpiece (e.g. A cybernetic penguin in a rainy city)...")

if st.button("GENERATE IMAGE"):
    if prompt:
        # PENGUIN LOADER
        with st.status("🐧 Penguin is sliding through the ice to fetch your art...", expanded=True) as status:
            # QUALITY BOOSTER (The Secret Sauce)
            quality_tags = "8k resolution, highly detailed, cinematic lighting, masterpiece, unreal engine 5, trending on artstation"
            full_prompt = f"{prompt}, {quality_tags}"
            encoded_prompt = urllib.parse.quote(full_prompt)
            
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1080&height=1920&nologo=true"
            
            # Show Image on the same page
            st.image(image_url, caption="Final Artwork by Penguin AI", use_container_width=True)
            
            # Custom View/Download Link
            st.markdown(f'''
                <a href="{image_url}" target="_blank" style="text-decoration:none;">
                    <div style="background-color:#22c55e; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold;">
                        Open Full HD Version ↗️
                    </div>
                </a>
            ''', unsafe_allow_html=True)
            status.update(label="✅ Art Generated!", state="complete", expanded=False)
    else:
        st.error("Please type something first!")

# 5. Footer
st.divider()
st.markdown("<p style='text-align: center; opacity: 0.6;'>© 2026 Penguin AI | Built for the Future</p>", unsafe_allow_html=True)
