import streamlit as st
from openai import OpenAI

# -----------------------------
# App Config
# -----------------------------
st.set_page_config(
    page_title="Understand This Property",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# OpenAI Client
# -----------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <div style="text-align:center; margin-bottom:16px;">
        <h2 style="margin-bottom:6px;">🏠 Understand This Property</h2>
        <p style="color:#555; font-size:15px; max-width:720px; margin:auto;">
            An objective breakdown of property listings — focused on clarity, gaps, and trade-offs.
            This tool does not promote or recommend properties.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Input Section
# -----------------------------
st.markdown("### 🧾 Paste the Property Listing")

st.caption(
    "Paste broker WhatsApp messages, website listings, or brochure text. "
    "Raw, unedited text works best."
)

listing_text = st.text_area(
    label="Property listing text",
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
# SYSTEM PROMPT (LOCKED)
# -----------------------------
SYSTEM_PROMPT = """
You are a neutral real estate analyst.

Your task:
Analyze and summarize the following property listing clearly and honestly for a homebuyer.

Rules:
- Do NOT promote or sell the property.
- Do NOT exaggerate positives.
- Clearly call out trade-offs, limitations, risks, or uncertainties.
- If information is missing, unclear, or vague, explicitly say "Not mentioned".
- Do NOT assume facts that are not stated.
- Use simple, plain language.
- Avoid marketing or emotional tone.
- Stay factual and balanced.

Output format (strict):

1. Property Snapshot
2. What the Listing Clearly States
3. Gaps, Risks, or Red Flags
4. Who This Property May Suit
5. Questions a Buyer Should Ask
"""

# -----------------------------
# Core Logic
# -----------------------------
def summarize_listing(text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

# -----------------------------
# Output Section
# -----------------------------
if analyze_clicked:
    if not listing_text.strip():
        st.warning("Please paste a property listing to analyze.")
    else:
        with st.spinner("Reviewing the listing objectively…"):
            try:
                result = summarize_listing(listing_text)

                st.divider()
                st.markdown("## 📊 PaXdom Summary")

                # ✅ SAFE OUTPUT CONTAINER (NO HTML)
                with st.container():
                    st.write(result)

            except Exception:
                st.error("Unable to analyze the listing right now. Please try again.")

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption("PaXdom AI Tools • Neutral analysis • Built for informed decisions")
