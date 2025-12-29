import streamlit as st
from agent import agent_response

st.title("🎵 Mood-Based Playlist Agent")

user_input = st.text_input(
    "What do you want to listen to?",
    placeholder="..."
)

if st.button("Generate Playlist"):
    if not user_input.strip():
        st.warning("Please enter a request.")
    else:
        playlist = agent_response(user_input)

        if not playlist:
            st.error("No songs found.")
        else:
            st.subheader("🎧 Your Playlist")
            for i, url in enumerate(playlist, 1):
                st.markdown(f"{i}. [Open song]({url})")
