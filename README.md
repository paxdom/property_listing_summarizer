````md
# 🏠 Understand This Property by PaXdom Realty  
### A Neutral AI Tool for Decoding Real Estate Listings

**Understand This Property** is an AI-powered tool built by **PaXdom Realty** to help homebuyers objectively analyze property listings.

It transforms raw, often marketing-heavy listing text into a **clear, structured, and honest breakdown** — highlighting what is stated, what is missing, and what buyers should question **before engaging with a broker**.

This tool is fully neutral: it does **not** promote properties, sell, or provide buying advice. Its goal is **clarity, trust, and informed decision-making**.

---

## Why PaXdom Built This Tool

At PaXdom Realty, we noticed that:
- Most listings exaggerate positives
- Trade-offs or limitations are often hidden
- Vague or emotional language confuses buyers
- Buyers feel pressured and uncertain

**Understand This Property** applies a neutral analytical lens so buyers can:
- Spot gaps and risks early  
- Ask better questions  
- Understand listings clearly  
- Make more confident decisions

---

## What the App Does (V1)

**Input**
- Raw property listing text  
  (WhatsApp messages, website listings, brochure content)

**Output**
A structured, easy-to-read summary with:
1. Property Snapshot  
2. What the Listing Clearly States  
3. Gaps, Risks, or Red Flags  
4. Who This Property May Suit  
5. Questions a Buyer Should Ask  

**Key Principles**
- Neutral, factual, and unbiased  
- No marketing language  
- Missing information explicitly flagged  

---

## What the App Does NOT Do

- ❌ Promote or rank properties  
- ❌ Recommend buying or investing  
- ❌ Replace legal, financial, or site due diligence  
- ❌ Scrape or analyze external links (V1 is text-only)  

---

## Technology Stack

- **Frontend**: Streamlit  
- **AI Model**: OpenAI (`gpt-4o-mini`)  
- **Language**: Python 3.11  

Chosen for simplicity, reliability, and low operating cost.

---

## Running the App Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
````

### 2. Set OpenAI API key

Create the file:

```
.streamlit/secrets.toml
```

Add:

```toml
OPENAI_API_KEY = "sk-xxxx"
```

### 3. Run the app

```bash
streamlit run streamlit_app.py
```

---

## Cost Notes

Approximate usage cost:

* ₹0.10 – ₹0.30 per analysis (depends on text length)

---

## Product Philosophy

PaXdom Realty built this tool based on three principles:

1. **Clarity over persuasion**
2. **Transparency over conversion**
3. **Buyer trust over short-term sales**

It is a **standalone clarity tool**, not a sales funnel.
Our goal: empower buyers to make confident property decisions.

---

## Try It & Learn More

Explore more PaXdom Realty tools and listings at:
**[paxdomrealty.com](https://paxdomrealty.com)**

---

## Disclaimer

This tool provides **informational analysis only**.
It does **not** constitute legal, financial, or investment advice.

Users should always verify details independently and consult professionals when needed.

---

## License

---
