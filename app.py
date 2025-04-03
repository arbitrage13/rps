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
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "win"
    else:
        return "loss"

# Initialize session state
if "player_history" not in st.session_state:
    st.session_state.player_history = []

if "computer_history" not in st.session_state:
    st.session_state.computer_history = []

if "results" not in st.session_state:
    st.session_state.results = []

# Title
st.title("🪨📄✂️ Rock-Paper-Scissors with Adaptive AI")

st.write("Choose your move:")

# UI Buttons
col1, col2, col3 = st.columns(3)
move = None
with col1:
    if st.button("🪨 Rock"):
        move = "rock"
with col2:
    if st.button("📄 Paper"):
        move = "paper"
with col3:
    if st.button("✂️ Scissors"):
        move = "scissors"

# Game logic
if move:
    st.session_state.player_history.append(move)
    computer_move = adaptive_ai(st.session_state.player_history)
    st.session_state.computer_history.append(computer_move)
    
    result = determine_winner(move, computer_move)
    st.session_state.results.append(result)

    # Display round result
    st.markdown("---")
    st.subheader("🎯 Round Result")
    st.write(f"**You played:** {move}")
    st.write(f"**Computer played:** {computer_move}")
    
    if result == "win":
        st.success("✅ You win!")
    elif result == "loss":
        st.error("❌ Computer wins!")
    else:
        st.info("🤝 It's a draw!")

# Show result stats
if st.session_state.results:
    st.markdown("---")
    st.subheader("📊 Game Stats")

    total = len(st.session_state.results)
    wins = st.session_state.results.count("win")
    losses = st.session_state.results.count("loss")
    draws = st.session_state.results.count("draw")

    win_pct = wins / total * 100
    loss_pct = losses / total * 100
    draw_pct = draws / total * 100

    st.write(f"**Total Rounds:** {total}")

    st.table({
        "Result": ["Wins", "Losses", "Draws"],
        "Count": [wins, losses, draws],
        "Percent": [f"{win_pct:.1f}%", f"{loss_pct:.1f}%", f"{draw_pct:.1f}%"]
    })

# History
if st.session_state.player_history:
    st.markdown("---")
    st.write("📜 Your move history:")
    st.write(", ".join(st.session_state.player_history))

# Reset button
if st.button("🔄 Reset Game"):
    st.session_state.player_history = []
    st.session_state.computer_history = []
    st.session_state.results = []
    st.experimental_rerun()
