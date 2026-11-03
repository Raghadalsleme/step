from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="كويز قرامر STEP", page_icon="📝", layout="wide")

# Hide Streamlit's own bars and padding so the quiz fills the whole screen
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}
      .block-container, [data-testid="stMainBlockContainer"] {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stVerticalBlock"] {gap: 0 !important;}
      [data-testid="stAppViewContainer"], [data-testid="stMain"], section.main {overflow: hidden !important;}
      iframe {display: block; border: 0; width: 100%;}
    </style>
    """,
    unsafe_allow_html=True,
)

QUIZ = Path(__file__).with_name("quiz.html").read_text(encoding="utf-8")

# The quiz sizes its own frame to the screen; height + scrolling are the fallback
components.html(QUIZ, height=820, scrolling=True)
