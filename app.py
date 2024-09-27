import streamlit as st
import base64
import time

# Initialize session state variables
if 'count' not in st.session_state:
    st.session_state.count = 0
if 'timer_started' not in st.session_state:
    st.session_state.timer_started = False
if 'time_left' not in st.session_state:
    st.session_state.time_left = 60  # 60 seconds timer
if 'timer_end' not in st.session_state:
    st.session_state.timer_end = False

# Function to increment counter
def increment_counter():
    if st.session_state.timer_started and st.session_state.time_left > 0:
        st.session_state.count += 1

# Function to load and encode the image
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        print(f"Warning: Image file not found at {image_path}. Using a placeholder.")
        return ""

# Function to start the timer
def start_timer():
    st.session_state.timer_started = True
    st.session_state.time_left = 60  # Reset the timer to 60 seconds
    st.session_state.timer_end = False

# Set page config
st.set_page_config(page_title="Diamify", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: black;
    }
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: linear-gradient(90deg, #000000, #1a5e1a);
        padding: 1rem;
        color: white;
    }
    .logo {
        font-size: 24px;
        font-weight: bold;
    }
    .navbar .nav-button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    .card {
        background-color: #ffd700;
        border-radius: 10px;
        padding: 2rem;
        max-width: 600px;
        margin: 2rem auto;
        text-align: center;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    .counter-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }
    .counter-value {
        font-size: 24px;
        margin-bottom: 10px;
    }
    .stButton > button {
        background-color: #4CAF50 !important;
        color: white !important;
        font-size: 16px !important;
        padding: 10px 20px !important;
        border-radius: 5px !important;
        border: none !important;
        cursor: pointer !important;
        transition: background-color 0.3s !important;
    }
    .stButton > button:hover {
        background-color: #45a049 !important;
    }
    /* Hide Streamlit's default header */
    header {
        visibility: hidden;
    }
    /* Hide Streamlit's default footer */
    footer {
        visibility: hidden;
    }
    /* Adjust the main content area */
    .main .block-container {
        padding-top: 0;
        padding-bottom: 0;
    }
</style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
<div class="navbar">
    <div class="logo">Diamify</div>
    <a href="https://example.com" target="_blank" class="nav-button">Say Hello to Diamify!</a>
</div>
""", unsafe_allow_html=True)

# Try to get the image, use a placeholder if not found
image_path = "./images.jpeg"
image_base64 = get_image_base64(image_path)

# Card content
st.markdown(f"""
<div class="card">
    {'<img src="data:image/jpeg;base64,' + image_base64 + '" width="150">' if image_base64 else '<div style="width:150px;height:150px;background-color:#4CAF50;margin:auto;"></div>'}
    <h2 style="color: #333;">Diam Token</h2>
    <p style="color: #555;">Diam Token is a revolutionary cryptocurrency that aims to transform the digital asset landscape. With its innovative blockchain technology and commitment to sustainability, Diamante Token offers a secure and eco-friendly investment opportunity.</p>
    <div class="counter-container">
        <div class="counter-value">Counter: {st.session_state.count}</div>
        <div>Time left: {st.session_state.time_left} seconds</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Start Timer button
if not st.session_state.timer_started:
    if st.button('Start Timer'):
        start_timer()

# Timer logic
if st.session_state.timer_started and not st.session_state.timer_end:
    current_time = time.time()
    if st.session_state.time_left > 0:
        st.session_state.time_left -= 1
        time.sleep(1)  # Update every second
    else:
        st.session_state.timer_end = True

# Counter button, enabled only when the timer is running
if st.session_state.timer_started and not st.session_state.timer_end:
    _, button_col, _ = st.columns([1, 2, 1])
    with button_col:
        if st.button('Increment Counter'):
            increment_counter()

# When the timer ends, display the result
if st.session_state.timer_end:
    st.write(f"Wow, You earned {st.session_state.count} points!")
