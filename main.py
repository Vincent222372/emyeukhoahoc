import streamlit as st
import random

# Page config
st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊✋✌️")

# Title and Instructions
st.title("🪨📄✂️ Rock Paper Scissors")
st.subheader("Instructions:")
st.markdown("""
1. Select **Rock**, **Paper**, or **Scissors**.
2. Click the **Play** button.
3. The computer will make a random choice.
4. The winner is decided based on the classic rules:
   - Rock crushes Scissors  
   - Scissors cuts Paper  
   - Paper covers Rock
""")

# Game options
options = ["Rock", "Paper", "Scissors"]
user_choice = st.radio("Choose your move:", options)

# Play button
if st.button("Play"):
    computer_choice = random.choice(options)
    st.write(f"💻 **Computer chose:** {computer_choice}")
    st.write(f"🧑 **You chose:** {user_choice}")

    # Result logic
    if user_choice == computer_choice:
        st.info("🤝 It's a draw!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.success("🎉 You win!")
        st.balloons()
    else:
        st.error("😢 You lose. Try again!")

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
