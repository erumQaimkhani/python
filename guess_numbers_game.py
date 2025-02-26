


import random
import streamlit as st

def guess_numbers_game():
    """Play the Guess the Number game using Streamlit."""
    
    # Initialize session state variables
    if 'number' not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.guess_right = 7
        st.session_state.feedback = ""
    
    st.title("🎲 Guess the Number Game 🎲")
    st.subheader("I am thinking of a number between 1 and 100.")
    st.write(f"You have {st.session_state.guess_right} guess{'es' if st.session_state.guess_right > 1 else ''} remaining.")
    
    # Display feedback message
    if st.session_state.feedback:
        st.write(st.session_state.feedback)
    
    # User input
    guess = st.text_input("Make a guess:", key="guess_input")
    
    # Submit button for making a guess
    if st.button("Submit Guess"):
        # Input validation
        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                st.session_state.feedback = "Please guess a number between 1 and 100."
                st.experimental_rerun()
        except ValueError:
            st.session_state.feedback = "Invalid input! Please enter a valid number."
            st.experimental_rerun()
        
        # Check the guess
        if guess < st.session_state.number:
            st.session_state.feedback = "Your guess is too low, try again."
        elif guess > st.session_state.number:
            st.session_state.feedback = "Your guess is too high, try again."
        else:
            # If the guess is correct
            st.success(f"🎉 Congratulations! You guessed the number {st.session_state.number} correctly in {7 - st.session_state.guess_right + 1} tries! 🎉")
            st.balloons()
            if st.button("Play Again"):
                # Reset the game state
                st.session_state.number = random.randint(1, 100)
                st.session_state.guess_right = 7
                st.session_state.feedback = ""
                st.experimental_rerun()
            return
        
        # Decrease the number of guesses remaining
        st.session_state.guess_right -= 1
        
        # If no guesses are left
        if st.session_state.guess_right == 0:
            st.error(f"😢 Sorry! You have run out of guesses. The number was {st.session_state.number}.")
            if st.button("Play Again"):
                # Reset the game state
                st.session_state.number = random.randint(1, 100)
                st.session_state.guess_right = 7
                st.session_state.feedback = ""
                st.experimental_rerun()

guess_numbers_game()

