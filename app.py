import random
import urllib.parse

import requests
import streamlit as st

# --- 1. PAGE CONFIG (Locked) ---
st.set_page_config(page_title="Penguin AI", page_icon="🐧", layout="centered")

# --- 2. SESSION STATE (Locked) ---
if "p_val" not in st.session_state:
    st.session_state.p_val = ""

# --- 3. UI & GLOW CSS (LOCKED - NO CHANGES) ---
st.markdown(
    """
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
    """,
    unsafe_allow_html=True,
)

st.title("🐧 Penguin AI")
st.write(
    "<p style='text-align: center; color: #88C0D0;'>Pro Art Engine • 100% Free & Stable</p>",
    unsafe_allow_html=True,
)

# --- 4. INPUT AREA (Locked) ---
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input(
        "Describe your vision:",
        value=st.session_state.p_val,
        placeholder="E.g. A neon warrior...",
    )
with col2:
    st.write("<br>", unsafe_allow_html=True)
    if st.button("✨"):
        ideas = [
            "Cyberpunk Penguin",
            "Neon Samurai",
            "Galaxy in a bottle",
            "Ice Dragon",
            "Viking Warrior",
        ]
        st.session_state.p_val = random.choice(ideas)
        st.rerun()


def generate_image_url(prompt: str, seed: int) -> str:
    encoded = urllib.parse.quote(prompt.strip())
    return (
        "https://image.pollinations.ai/prompt/"
        f"{encoded}?seed={seed}&width=1024&height=1024&nologo=true"
    )


# --- 5. GENERATION LOGIC (Hardened) ---
if st.button("Generate Masterpiece 🚀", use_container_width=True):
    if user_input and user_input.strip():
        st.session_state.p_val = user_input

        with st.status("Generating Art from Public Nodes...", expanded=True) as status:
            image_bytes = None
            final_url = None
            errors = []

            # Retry a few times with different seeds if any upstream node gives non-image payload.
            for attempt in range(1, 4):
                seed = random.randint(1, 10_000_000)
                candidate_url = generate_image_url(user_input, seed)

                try:
                    response = requests.get(candidate_url, timeout=45)
                    content_type = response.headers.get("content-type", "")

                    if response.ok and content_type.startswith("image/") and response.content:
                        image_bytes = response.content
                        final_url = candidate_url
                        st.write(
                            f"Attempt {attempt}: image pipeline healthy (seed={seed})."
                        )
                        break

                    errors.append(
                        f"Attempt {attempt}: invalid payload ({response.status_code}, {content_type})."
                    )
                except requests.RequestException as exc:
                    errors.append(f"Attempt {attempt}: network error - {exc}")

            if image_bytes and final_url:
                status.update(label="Art Ready!", state="complete", expanded=False)
            else:
                status.update(label="Generation failed", state="error", expanded=True)

        if image_bytes and final_url:
            st.markdown(
                """
                <div class="result-card">
                    <h3 style="color:#00E676;">Creation Successful!</h3>
                    <p style="color:#A0A0A0; margin-bottom:25px;">No Login Required. Your high-res art is ready.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.image(image_bytes, caption="Generated Wallpaper", use_container_width=True)
            st.download_button(
                "VIEW & DOWNLOAD ART 📥",
                data=image_bytes,
                file_name="penguin_ai_wallpaper.png",
                mime="image/png",
                use_container_width=True,
            )
            st.markdown(
                f"[Open image in new tab]({final_url})",
                unsafe_allow_html=True,
            )
        else:
            st.error(
                "Wallpaper generate nahi ho paaya. Public nodes unstable lag rahe hain — please retry in a moment."
            )
            if errors:
                with st.expander("Debug details"):
                    for err in errors:
                        st.write(err)
    else:
        st.warning("Prompt likho pehle!")

st.markdown('<div class="footer">Built by Agni-India • 2026</div>', unsafe_allow_html=True)
