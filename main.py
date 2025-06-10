import streamlit as st
import random
import time

st.set_page_config(page_title="Racing Game", page_icon="🏁")

st.title("🏎️💨 Racing Game")
st.subheader("Instructions:")
st.markdown("""
- Two players race to the finish line.
- Click the **Advance** button to move forward.
- First to reach the end wins!
""")

track_length = 30  # Number of track segments

# Session state initialization
if "p1_pos" not in st.session_state:
    st.session_state.p1_pos = 0
if "p2_pos" not in st.session_state:
    st.session_state.p2_pos = 0
if "winner" not in st.session_state:
    st.session_state.winner = None

# Draw track
def draw_track():
    track = ""
    for i in range(track_length):
        if i == st.session_state.p1_pos:
            track += "🏎️"
        else:
            track += "—"
    st.write("Player 1:", track)

    track = ""
    for i in range(track_length):
        if i == st.session_state.p2_pos:
            track += "🚗"
        else:
            track += "—"
    st.write("Player 2:", track)

draw_track()

# Advance buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Advance Player 1"):
        if not st.session_state.winner:
            st.session_state.p1_pos += random.randint(1, 3)
with col2:
    if st.button("Advance Player 2"):
        if not st.session_state.winner:
            st.session_state.p2_pos += random.randint(1, 3)

# Check for winner
if st.session_state.p1_pos >= track_length:
    st.session_state.winner = "Player 1 🏆"
elif st.session_state.p2_pos >= track_length:
    st.session_state.winner = "Player 2 🏆"

if st.session_state.winner:
    st.success(f"🎉 {st.session_state.winner} wins!")

# Restart game
if st.button("Restart Game"):
    st.session_state.p1_pos = 0
    st.session_state.p2_pos = 0
    st.session_state.winner = None
    st.experimental_rerun()
