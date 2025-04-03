import streamlit as st
import random
from collections import Counter

# Helper functions
def get_counter_move(move):
    beats = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }
    return beats[move]

def adaptive_ai(player_history):
    if not player_history:
        return random.choice(["rock", "paper", "scissors"])
    
    counts = Counter(player_history)
    most_common = counts.most_common(1)[0][0]
    return get_counter_move(most_common)

def determine_winner(player, computer):
    if player == computer:
        return "It's a draw!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Initialize session state
if "player_history" not in st.session_state:
    st.session_state.player_history = []

if "result" not in st.session_state:
    st.session_state.result = ""

if "computer_move" not in st.session_state:
    st.session_state.computer_move = ""

# Title
st.title("🪨📄✂️ Rock-Paper-Scissors with Adaptive AI")

# Instructions
st.write("Choose your move:")

# UI Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🪨 Rock"):
        move = "rock"
elif_selected = True
with col2:
    if st.button("📄 Paper"):
        move = "paper"
        elif_selected = True
with col3:
    if st.button("✂️ Scissors"):
        move = "scissors"
        elif_selected = True

# Game logic
if 'move' in locals():
    st.session_state.player_history.append(move)
    st.session_state.computer_move = adaptive_ai(st.session_state.player_history)
    st.session_state.result = determine_winner(move, st.session_state.computer_move)

# Display result
if st.session_state.result:
    st.markdown("---")
    st.subheader("Result:")
    st.write(f"**You played:** {st.session_state.player_history[-1]}")
    st.write(f"**Computer played:** {st.session_state.computer_move}")
    st.success(st.session_state.result)

# History
if st.session_state.player_history:
    st.markdown("---")
    st.write("📜 Your move history:")
    st.write(", ".join(st.session_state.player_history))

# Reset button
if st.button("🔄 Reset Game"):
    st.session_state.player_history = []
    st.session_state.result = ""
    st.session_state.computer_move = ""
    st.experimental_rerun()
