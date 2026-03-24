import streamlit as st
import random
import urllib.parse

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Penguin AI", page_icon="🐧", layout="centered")

# --- 2. SESSION STATE (Memory) ---
if "prompt_text" not in st.session_state:
    st.session_state.prompt_text = ""
if "history_list" not in st.session_state:
    st.session_state.history_list = []

# --- 3. PREMIUM DARK UI (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stTextInput>div>div>input {
        background-color: #1A1C23 !important; color: white !important;
        border: 1px solid #333 !important; border-radius: 12px !important;
        padding: 12px !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #4CAF50, #00E676);
        color: white !important; border: none !important;
        border-radius: 12px !important; font-weight: bold !important;
        height: 3em !important; width: 100% !important;
    }
    .main-card { width: 100%; border-radius: 20px; border: 2px solid #222; margin-top: 20px; }
    .footer { text-align: center; padding: 20px; color: #666; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🐧 Penguin AI")
st.write("The Ultimate Art Engine • No Login • Unlimited")

# --- 4. INPUT SECTION ---
col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input("Describe your imagination:", value=st.session_state.prompt_text, placeholder="A futuristic penguin in space...")

with col2:
    st.write("<br>", unsafe_allow_html=True)
    if st.button("✨"):
        ideas = ["Cyberpunk Indian City", "Astronaut Penguin on Moon", "Majestic fire lion", "Robot painting a portrait"]
        st.session_state.prompt_text = random.choice(ideas)
        st.rerun()

# --- 5. GENERATION LOGIC ---
if st.button("Generate Masterpiece 🚀"):
    if user_input:
        st.session_state.prompt_text = user_input # Input save karo
        with st.spinner("Wait... Penguin is painting 🎨"):
            # Sabse stable URL format
            seed = random.randint(1, 1000000)
            clean_prompt = urllib.parse.quote(user_input)
            img_url = f"https://pollinations.ai/p/{clean_prompt}?seed={seed}&width=1024&height=1024&model=flux&nologo=true"
            
            # Direct Image Display (Bypassing internal processing)
            st.markdown(f'<img src="{img_url}" class="main-card">', unsafe_allow_html=True)
            
            # Download/Save Link
            st.write("<br>", unsafe_allow_html=True)
            st.markdown(f'''
                <a href="{img_url}" target="_blank">
                    <button style="width:100%; background-color:#4CAF50; color:white; padding:12px; border-radius:10px; border:none; cursor:pointer; font-weight:bold;">
                        Download High-Res (Full HD) 📥
                    </button>
                </a>
            ''', unsafe_allow_html=True)
            
            # History Update
            if img_url not in st.session_state.history_list:
                st.session_state.history_list.insert(0, img_url)
    else:
        st.warning("Pehle kuch likho toh sahi!")

# --- 6. GALLERY ---
if st.session_state.history_list:
    st.write("---")
    st.subheader("🕒 Recent Art")
    g_cols = st.columns(3)
    for i, url in enumerate(st.session_state.history_list[:9]):
        with g_cols[i % 3]:
            st.image(url, use_container_width=True)

st.markdown('<div class="footer">Built with Passion by Agni-India • No Credits Required</div>', unsafe_allow_html=True)
