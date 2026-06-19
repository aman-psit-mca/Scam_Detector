import streamlit as st
import google.generativeai as genai

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="AI Scam Detector",
    page_icon="🛡️",
    layout="wide"
)

# -------------------------------
# GEMINI CONFIG
# -------------------------------
API_KEY = "AQ.Ab8RN6LULxv61gaed0xNqgpRvND8TRlBIUQAtF_VGXskWXGeEw"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------------
# HEADER
# -------------------------------
st.title("🛡️ AI-Powered Scam & Fraud Message Detector")
st.markdown(
    """
    Detect suspicious messages using Google's Gemini AI.
    Paste any SMS, Email, WhatsApp or Social Media message.
    """
)

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.header("About")

st.sidebar.info(
    """
    Mini Project using:
    
    • Streamlit
    
    • Google Gemini API
    
    • Prompt Engineering
    
    • Risk Analysis
    """
)

# -------------------------------
# INPUT AREA
# -------------------------------
message = st.text_area(
    "Enter Message",
    height=250,
    placeholder="Congratulations! You won ₹50,000. Click here to claim..."
)

# -------------------------------
# ANALYSIS FUNCTION
# -------------------------------
def analyze_message(msg):
    
    prompt = f"""
    You are a cybersecurity expert.

    Analyze the following message.

    Message:
    {msg}

    Return:
    1. Scam Probability (High/Medium/Low)
    2. Reasons
    3. Red Flags
    4. Safety Advice

    Use clear formatting.
    """

    response = model.generate_content(prompt)

    return response.text


# -------------------------------
# BUTTON
# -------------------------------
if st.button("Analyze Message"):

    if not message.strip():
        st.warning("Please enter a message.")
    else:

        with st.spinner("Analyzing..."):

            try:
                result = analyze_message(message)

                st.success("Analysis Complete")

                st.markdown(result)

            except Exception as e:
                st.error(f"Error: {e}")

# -------------------------------
# EXAMPLES
# -------------------------------
st.divider()

st.subheader("Example Scam Messages")

examples = [
    "Your bank account will be blocked. Click this link immediately.",
    "You have won a free iPhone. Claim now!",
    "Share your OTP to verify your account."
]

for ex in examples:
    st.code(ex)

# -------------------------------
# FOOTER
# -------------------------------
st.divider()

st.caption(
    "Built using Streamlit + Google Gemini API"
)