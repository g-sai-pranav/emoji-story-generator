import streamlit as st
import google.generativeai as genai
import os
import random
from dotenv import load_dotenv

# --- CONFIGURATION & SETUP ---
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API Key not found. Please set it in your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# --- CORE FUNCTIONS ---
def cook_story(emojis: list[str]) -> str:
    """Generates a story from a list of emojis."""
    emoji_string = " ".join(emojis)
    prompt = (
        "Create a beautiful, short, and imaginative story (about 200 words) "
        f"based on the following sequence of emojis: {emoji_string}. "
        "The story should be magical and suitable for all ages."
    )
    try:
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def generate_random_emojis(count=8):
    """Generates a list of random emojis for selection."""
    emoji_ranges = [
        (0x1F600, 0x1F64F), (0x1F300, 0x1F5FF),
        (0x1F680, 0x1F6FF), (0x1F900, 0x1F9FF)
    ]
    emojis = set()
    while len(emojis) < count:
        selected_range = random.choice(emoji_ranges)
        code_point = random.randint(selected_range[0], selected_range[1])
        emojis.add(chr(code_point))
    return list(emojis)

# --- STREAMLIT UI ---
st.set_page_config(page_title="Emoji Story Generator", page_icon="✨")
st.title("📖 Emoji Story Generator")

# Initialize session state variables
if 'selected_emojis' not in st.session_state:
    st.session_state.selected_emojis = []
if 'emoji_options' not in st.session_state:
    st.session_state.emoji_options = generate_random_emojis()

st.info("Select 3 or 4 emojis by clicking on them, then cook your story!")

# Display the selection area
st.subheader("Your Chosen Emojis:")
selection_box = st.empty()

# --- Interactive Emoji Selection ---
st.write("---")
st.subheader("Click to Choose:")

cols = st.columns(8)
for i, emoji in enumerate(st.session_state.emoji_options):
    if cols[i].button(emoji, key=f"emoji_{i}"):
        if len(st.session_state.selected_emojis) < 4:
            st.session_state.selected_emojis.append(emoji)
        else:
            st.toast("You can only select up to 4 emojis!")

# Update the display of selected emojis
selection_box.text_input("Selected", " ".join(st.session_state.selected_emojis), disabled=True, label_visibility="collapsed")

# --- Action Buttons ---
st.write("---")
col1, col2, col3 = st.columns(3)

# Button to cook the story
if col1.button("Cook a Story! 🍳", type="primary"):
    if 3 <= len(st.session_state.selected_emojis) <= 4:
        with st.spinner("Cooking up your story... ✨"):
            story = cook_story(st.session_state.selected_emojis)
            st.success("Here is your story!")
            
            # --- THIS IS THE NEW PART ---
            # Display the emojis that generated the story
            st.markdown(f"### Story for: {' '.join(st.session_state.selected_emojis)}")
            st.write(story)
            # --- END OF NEW PART ---
            
    else:
        st.warning("Please select 3 or 4 emojis first.")

# Button to clear the current selection
if col2.button("Clear Selection ❌"):
    st.session_state.selected_emojis = []
    st.rerun()

# Button to get a new set of emoji options
if col3.button("Refresh Emojis 🔄"):
    st.session_state.emoji_options = generate_random_emojis()
    st.session_state.selected_emojis = [] # Also clear selection
    st.rerun()