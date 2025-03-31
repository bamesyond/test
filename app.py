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
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #f8f9fa, #e9ecef);
}
.big-font {
    font-size:30px !important;
    color: #1f77b4;
}
</style>
""", unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="big-font">Personal Information</p>', unsafe_allow_html=True)
    
    # Add emoji to name input
    name = st.text_input('👤 Enter your name', value=name if 'name' in locals() else '')
    
    # Add age validation
    try:
        age = int(st.text_input('🎂 Enter your age', value=age if 'age' in locals() else ''))
        if age < 0 or age > 150:
            st.warning('Please enter a valid age between 0 and 150')
    except ValueError:
        if age:  # Only show warning if something was entered
            st.warning('Please enter a valid number for age')
        age = None

with col2:
    st.markdown('<p class="big-font">Fun Cooking Animation!</p>', unsafe_allow_html=True)
    
    # Cooking animation using ASCII art and streamlit
    cooking_stages = [
        "🥘 Preparing...",
        "🔥 Heating up...",
        "♨️ Cooking...",
        "👨‍🍳 Almost done...",
        "✨ Bon appétit!"
    ]
    
    if st.button('Start Cooking!'):
        with st.spinner('Cooking in progress...'):
            for stage in cooking_stages:
                st.write(stage)
                st.balloons()
                st.sleep(1)
            st.success('Your virtual meal is ready! 🎉')

# Add a fun fact section
st.markdown("---")
if age:
    fun_facts = {
        "child": "Did you know? Children have more taste buds than adults!",
        "teen": "Fun fact: Teenagers need more sleep than adults!",
        "adult": "Interesting fact: The human body contains enough carbon to make around 900 pencils!",
        "senior": "Amazing fact: The oldest person ever lived to be 122 years old!"
    }
    
    if age < 13:
        st.info(fun_facts["child"])
    elif age < 20:
        st.info(fun_facts["teen"])
    elif age < 60:
        st.info(fun_facts["adult"])
    else:
        st.info(fun_facts["senior"])

# Add a playful greeting button with animation
if st.button('🎈 Greet Me!', key='greet'):
    if name:
        st.markdown(f"<h1 style='text-align: center; color: #1f77b4; animation: bounce 1s infinite;'>Hello {name}! 🌟</h1>", unsafe_allow_html=True)
        st.snow()
    else:
        st.warning("Please enter your name first! 😊")

# Add footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")

