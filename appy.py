import streamlit as st

st.title("Breather.pro")
st.subheader("Mindful Trading for Real People")

st.write("Welcome to Breather.pro — a minimalist trading app that combines signals with emotional wellness.")

# Example placeholder for a trade signal
st.success("Today's Signal: BUY BTC/USDT at 4H candle")

# Mood check-in
mood = st.radio("How do you feel right now?", ["Calm", "Anxious", "Confident", "Doubtful"])
if st.button("Submit Mood"):
    st.write(f"Logged mood: {mood}")