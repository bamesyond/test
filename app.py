import streamlit as st

st.title("Hello World")

#create a text input field that says 'Enter your name'
name = st.text_input('Enter your name')

#create a button that says 'Orusbucucu'
if st.button('Orusbucucu'):
    st.write(f'Hello {name}')

#create a text input field that says 'Enter your age'
age = st.text_input('Enter your age')

# Add some styling and animations
# Add a colorful sidebar
st.sidebar.title("Fun Interactive Elements! 🎨")
st.sidebar.markdown("---")

# 1. Color picker
favorite_color = st.sidebar.color_picker('Pick your favorite color', '#00f900')
st.markdown(f'<div style="background-color: {favorite_color}; padding: 10px; border-radius: 10px;">Your chosen color!</div>', unsafe_allow_html=True)

# 2. Slider for happiness level
happiness = st.slider('How happy are you today? 😊', 0, 100, 50)
st.write(f'Happiness level: {happiness}%')

# 3. Select box for favorite animal
animal = st.selectbox(
    'What\'s your favorite animal? 🐾',
    ('🐶 Dog', '🐱 Cat', '🐨 Koala', '🦊 Fox', '🐼 Panda', '🦁 Lion')
)
st.write(f'You selected: {animal}')

# 4. Radio buttons for preferred weather
weather = st.radio(
    "What's your ideal weather? ⛅",
    ('Sunny ☀️', 'Rainy 🌧️', 'Snowy ❄️', 'Cloudy ☁️')
)

# 5. Multi-select for hobbies
hobbies = st.multiselect(
    'Select your hobbies 🎨',
    ['Reading 📚', 'Gaming 🎮', 'Cooking 🍳', 'Sports 🏃‍♂️', 'Music 🎵', 'Art 🎨', 'Travel ✈️']
)

# 6. Number input for lucky number
lucky_number = st.number_input('What\'s your lucky number? 🎲', min_value=1, max_value=100)

# 7. Date input
special_date = st.date_input('Pick a special date 📅')

# 8. Time input
favorite_time = st.time_input('What\'s your favorite time of day? ⏰')

# 9. Text area for life motto
life_motto = st.text_area('Share your life motto! 💭')

# 10. File uploader
uploaded_file = st.file_uploader("Upload a fun picture! 📸", type=['jpg', 'png', 'gif'])
if uploaded_file is not None:
    st.image(uploaded_file, caption='Your uploaded image')

# 11. Progress bar animation
import time
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)

# 12. Balloons animation when clicking a button
if st.button('Click for a surprise! 🎉'):
    st.balloons()

# Add some custom CSS styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 20px;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Display a summary of selections
st.markdown("### Your Profile Summary 📋")
st.write(f"Name: {name}")
st.write(f"Age: {age}")
st.write(f"Favorite Color: {favorite_color}")
st.write(f"Favorite Animal: {animal}")
st.write(f"Weather Preference: {weather}")
st.write(f"Lucky Number: {lucky_number}")
st.write(f"Special Date: {special_date}")
st.write(f"Hobbies: {', '.join(hobbies) if hobbies else 'None selected'}")
