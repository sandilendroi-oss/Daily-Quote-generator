import streamlit as st
import random
from quotes import quotes

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Daily Quote Generator",
    page_icon="💡",
    layout="centered"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp{
    background:
    linear-gradient(
        rgba(0,0,0,0.45),
        rgba(0,0,0,0.45)
    ),
    url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Buttons */
.stButton > button{
    width:100%;
    background:linear-gradient(90deg,#ff512f,#dd2476);
    color:white;
    font-size:18px;
    font-weight:bold;
    padding:14px;
    border:none;
    border-radius:12px;
}

.stButton > button:hover{
    transform:scale(1.03);
    transition:0.3s;
    cursor:pointer;
}

/* Quote Card */
.quote-card{
    background:rgba(255,255,255,0.12);
    backdrop-filter:blur(10px);
    padding:30px;
    border-radius:20px;
    margin-top:20px;
    border:1px solid rgba(255,255,255,0.25);
}

/* Author Card */
.author-card{
    background:rgba(46,125,50,0.90);
    padding:15px;
    border-radius:12px;
    margin-top:15px;
    text-align:center;
}

/* Footer */
.footer{
    text-align:center;
    color:white;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("💡 Daily Quote Generator")
st.sidebar.write("Generate a new inspirational quote anytime!")
st.sidebar.metric("Quotes Available", len(quotes))
st.sidebar.markdown("---")
st.sidebar.success("Built with Python + Streamlit")

# --------------------------------------------------
# Title
# --------------------------------------------------

st.markdown("""
<h1 style="
text-align:center;
color:white;
font-size:60px;
text-shadow:3px 3px 8px black;
">
💡 Daily Quote Generator
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
font-size:22px;
color:white;
text-shadow:2px 2px 6px black;
">
Click the button below to receive a random inspirational quote.
</p>
""", unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)

# --------------------------------------------------
# Generate Button
# --------------------------------------------------

if st.button("✨ Generate New Quote"):
    st.session_state.quote = random.choice(quotes)

selected_quote = st.session_state.quote

# --------------------------------------------------
# Quote Section
# --------------------------------------------------

st.markdown("## 📖 Today's Quote")

st.markdown(
    f"""
    <div class="quote-card">
        <h2 style="color:white;text-align:center;">
            "{selected_quote['quote']}"
        </h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="author-card">
        <h3 style="color:white;">
            ✍️ {selected_quote['author']}
        </h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# --------------------------------------------------
# Favourite Button
# --------------------------------------------------

if st.button("❤️ Save Favourite"):
    st.success("Quote saved!")

st.write("")

# --------------------------------------------------
# Share Section
# --------------------------------------------------

st.subheader("📤 Copy and Share")

share_text = f'"{selected_quote["quote"]}"\n\n— {selected_quote["author"]}'

st.code(share_text)

st.caption("Copy the text above and share it on social media.")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("""
<div class="footer">
<hr>
<h4>Built with ❤️ using Python & Streamlit</h4>
<p>© 2026 Sandile Thabede</p>
</div>
""", unsafe_allow_html=True)