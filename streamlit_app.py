import streamlit as st
import time
import random
from openai import OpenAI, RateLimitError
import streamlit.components.v1 as components # Added for resizing

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Understand This Property",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# GLOBAL SAFE CSS (MATCH APP 2 & 3)
# -----------------------------
st.markdown("""
<style>
html, body, .stApp {
    background-color: #ffffff !important;
    color: #111827 !important;
}

h1, h2, h3 {
    color: #111827 !important;
}

/* Inputs */
textarea, input {
    background-color: #ffffff !important;
    color: #111827 !important;
    border: 1px solid #D1D5DB !important;
}

/* Placeholder visibility */
textarea::placeholder,
input::placeholder {
    color: #6B7280 !important;
    opacity: 1 !important;
}

/* Button */
button {
    background-color: #111827 !important;
    color: #ffffff !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

/* Prevent scroll traps */
.main, .block-container {
    overflow: visible !important;
    max-height: none !important;
}

/* Output spacing */
.stMarkdown ul {
    padding-left: 1.2em;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    """
    <div style="text-align:center; margin-bottom:18px;">
        <h1>🏠 Understand This Property</h1>
        <p style="color:#555; font-size:15px; max-width:720px; margin:auto;">
            An objective breakdown of property listings — focused on clarity, gaps, and trade-offs.
            No promotion. No recommendations.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# INPUT SECTION
# -----------------------------
st.markdown("### 🧾 Paste the Property Listing")

st.caption(
    "Paste broker WhatsApp messages, website listings, or brochure text. "
    "Raw, unedited text works best."
)

listing_text = st.text_area(
    label="",
    placeholder=(
        "Example:\n"
        "• 2 BHK, 1150 sq ft, near Metro\n"
        "• Pre-launch price, limited units\n"
        "• Possession in 2027\n\n"
        "Tip: Include everything you received from the broker."
    ),
    height=220,
    key="listing_input"
)

st.markdown("<br>", unsafe_allow_html=True)

analyze_clicked = st.button(
    "🔍 Analyze listing with clarity",
    use_container_width=True
)

# -----------------------------
# SYSTEM PROMPT (LOCKED – FINAL)
# -----------------------------
SYSTEM_PROMPT = """
You are a neutral real estate analyst.

Task:
Analyze and summarize the property listing clearly and honestly for a homebuyer.

Rules:
- Do NOT promote, sell, or persuade.
- Do NOT exaggerate positives.
- Clearly highlight trade-offs, risks, limitations, and uncertainty.
- If information is missing or vague, explicitly state: "Not mentioned".
- Do NOT assume or infer facts.
- Use simple, plain, non-marketing language.
- Stay factual and balanced.

Output format (strict):

1. Property Snapshot
2. What the Listing Clearly States
3. Gaps, Risks, or Red Flags
4. Who This Property May Suit
5. Questions a Buyer Should Ask
"""

# -----------------------------
# OPENAI SAFE CLIENT
# -----------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def summarize_listing(text: str, retries=3) -> str:
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=0.2,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": text}
                ]
            )
            return response.choices[0].message.content.strip()

        except RateLimitError:
            if attempt < retries - 1:
                time.sleep((2 ** attempt) + random.uniform(0.5, 1.5))
            else:
                raise

# -----------------------------
# OUTPUT SECTION
# -----------------------------
if analyze_clicked:
    if not listing_text.strip():
        st.warning("Please paste a property listing to analyze.")
    else:
        with st.spinner("Reviewing the listing objectively…"):
            try:
                result = summarize_listing(listing_text)

                st.markdown("---")
                st.markdown("## 📊 Property Summary")

                # ✅ SAFE OUTPUT (NO HTML, MOBILE FRIENDLY)
                st.markdown(result)

            except RateLimitError:
                st.error(
                    "The tool is temporarily busy due to high usage. "
                    "Please wait a moment and try again."
                )

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Neutral analysis • Built for clarity • No recommendations")

# --- NEW: THE RESIZER COMPONENT ---
# This tells the Wix iframe to change size whenever the result appears
components.html(
    """
    <script>
        const sendHeight = () => {
            const height = document.body.scrollHeight;
            window.parent.postMessage({
                source: 'streamlit-resize',
                height: height
            }, '*');
        }
        const observer = new ResizeObserver(sendHeight);
        observer.observe(document.body);
        sendHeight(); // Initial call
    </script>
    """,
    height=0,
)
