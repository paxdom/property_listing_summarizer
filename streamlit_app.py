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
st.title("Understand This Property")
st.caption(
    "An objective breakdown of property listings — focused on clarity, gaps, and trade-offs. "
    "This tool does not promote or recommend properties."
)

st.divider()

# -----------------------------
# Input
# -----------------------------
listing_text = st.text_area(
    label="Paste the property listing text",
    placeholder=(
        "Paste broker WhatsApp messages, website listings, or brochure text here.\n\n"
        "Tip: The more raw the text, the better the analysis."
    ),
    height=220
)

analyze_clicked = st.button("Analyze listing")

# -----------------------------
# SYSTEM PROMPT (LOCKED – V1)
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

Output format (strict — use these exact headings):

1. Property Snapshot
2. What the Listing Clearly States
3. Gaps, Risks, or Red Flags
4. Who This Property May Suit
5. Questions a Buyer Should Ask
"""

# -----------------------------
# Core Logic
# -----------------------------
def summarize_listing(listing_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": listing_text}
        ]
    )

    return response.choices[0].message.content.strip()

# -----------------------------
# Output
# -----------------------------
if analyze_clicked:
    if listing_text.strip() == "":
        st.warning("Please paste a property listing to analyze.")
    else:
        with st.spinner("Reviewing the listing objectively..."):
            try:
                result = summarize_listing(listing_text)
                st.divider()
                st.markdown(result)
            except Exception:
                st.error("Unable to analyze the listing right now. Please try again.")
