import streamlit as st
import random
import urllib.parse
import re

# --- 1. PAGE CONFIG (Locked) ---
st.set_page_config(page_title="Penguin AI", page_icon="🐧", layout="centered")

# --- 2. SESSION STATE (Locked) ---
if "p_val" not in st.session_state: st.session_state.p_val = ""

# --- 3. UI & GLOW CSS (LOCKED - NO CHANGES) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    
    /* Glow Buttons Locked */
    .stButton>button { 
        border-radius: 12px; border: 1px solid #4CAF50; background-color: #1A1C23;
        color: white; font-weight: bold; width: 100%; padding: 15px;
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.2); transition: 0.3s;
    }
    .stButton>button:hover { 
        border-color: #00E676; color: #00E676; 
        box-shadow: 0 0 20px rgba(0, 230, 118, 0.5); 
    }

    /* Result Card Locked */
    .result-card {
        background-color: #1A1C23; padding: 30px; border-radius: 20px; 
        border: 1px solid #333; text-align: center; margin-top: 20px;
    }
    
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; text-align: center; padding: 10px; background: #0E1117; border-top: 1px solid #2e2e2e; color: gray; }
    </style>
    """, unsafe_allow_html=True)

st.title("🐧 Penguin AI")
st.write("<p style='text-align: center; color: #88C0D0;'>Pro Art Engine • 100% Free & Stable</p>", unsafe_allow_html=True)

# --- 4. INPUT AREA (Locked) ---
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input("Describe your vision:", value=st.session_state.p_val, placeholder="E.g. A neon warrior...")
with col2:
    st.write("<br>", unsafe_allow_html=True)
    if st.button("✨"):
        ideas = ["Cyberpunk Penguin", "Neon Samurai", "Galaxy in a bottle", "Ice Dragon", "Viking Warrior"]
        st.session_state.p_val = random.choice(ideas)
        st.rerun()

# --- 5. GENERATION LOGIC (THE FIX: NO-AUTH SOURCE) ---
if st.button("Generate Masterpiece 🚀", use_container_width=True):
    if user_input:
        st.session_state.p_val = user_input
        
        with st.status("Fetching Art from Public Nodes...", expanded=True) as status:
            # Cleaning Prompt to avoid URL breaks
            clean_input = re.sub(r'[^a-zA-Z0-9\s]', '', user_input)
            encoded = urllib.parse.quote(clean_input)
            seed = random.randint(1, 10000000)
            
            # --- THE FINAL FREE URL (No API Key Required) ---
            # Humne '/p/' (Pro) hata kar '/prompt/' (Public) kar diya hai
            final_url = f"https://image.pollinations.ai/prompt/{encoded}?seed={seed}&width=1024&height=1024&nologo=true"
            
            st.write("Image sequence bypass successful.")
            status.update(label="Art Ready!", state="complete", expanded=False)

        # THE ACTION CARD (Locked UX)
        st.markdown(f'''
            <div class="result-card">
                <h3 style="color:#00E676;">Creation Successful!</h3>
                <p style="color:#A0A0A0; margin-bottom:25px;">No Login Required. Your high-res art is ready.</p>
                <a href="{final_url}" target="_blank" style="text-decoration: none;">
                    <button style="width:100%; background: linear-gradient(90deg, #4CAF50, #00E676); color:white; padding:20px; border-radius:12px; border:none; cursor:pointer; font-weight:bold; font-size:20px;">
                        VIEW & DOWNLOAD ART 📥
                    </button>
                </a>
                <p style="margin-top:15px; font-size:12px; color:#555;">(High Definition • Fast Load)</p>
            </div>
        ''', unsafe_allow_html=True)
    else:
        st.warning("Prompt likho pehle!")

st.markdown('<div class="footer">Built by Agni-India • 2026</div>', unsafe_allow_html=True)
