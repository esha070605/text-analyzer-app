import streamlit as st

st.set_page_config(page_title="Text Analyzer", layout="centered")

st.title("📝 Text Analyzer App")
st.write("Paste your text below and get quick insights!")

# Text input
text_input = st.text_area("Enter your text here:", height=200)

if text_input:
    # Word count
    words = text_input.split()
    word_count = len(words)

    # Character count
    char_count = len(text_input)

    # Reading time (avg: 200 words per min)
    reading_time = round(word_count / 200, 2)

    # Display results
    st.subheader("📊 Analysis")
    st.write(f"**Words:** {word_count}")
    st.write(f"**Characters:** {char_count}")
    st.write(f"**Estimated Reading Time:** {reading_time} minutes")

