import string
from PIL import Image
import streamlit.components.v1 as components
import os

# Function to generate password
def generate_password(length, lower, upper, numbers, symbols, exclude_duplicates, include_spaces):
    characters = ""
    if lower:
        characters += string.ascii_lowercase
    if upper:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    if include_spaces:
        characters += " "
    
    if exclude_duplicates:
        if length > len(characters):
            raise ValueError("Length exceeds the number of unique characters available")
        password = ''.join(random.sample(characters, length))
    else:
        password = ''.join(random.choices(characters, k=length))
    
    return password

# Streamlit App
st.title('Password Generator')

# Add the cyber image
image_path = 'C:/Users/prash/OneDrive/Documents/Python Project/cyber_image.jpeg'
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, use_column_width=True)
else:
    st.error(f"Error loading image: {image_path} not found.")

# Initialize session state for settings
if 'length' not in st.session_state:
    st.session_state.length = 15
if 'lower' not in st.session_state:
    st.session_state.lower = True
if 'upper' not in st.session_state:
    st.session_state.upper = False
if 'numbers' not in st.session_state:
    st.session_state.numbers = False
if 'symbols' not in st.session_state:
    st.session_state.symbols = True
if 'exclude_duplicates' not in st.session_state:
    st.session_state.exclude_duplicates = False
if 'include_spaces' not in st.session_state:
    st.session_state.include_spaces = False

# Password Length
length = st.slider('Password Length', min_value=6, max_value=30, value=st.session_state.length)
st.session_state.length = length

# Password Settings
lower = st.checkbox('Lowercase (a-z)', value=st.session_state.lower)
st.session_state.lower = lower
upper = st.checkbox('Uppercase (A-Z)', value=st.session_state.upper)
st.session_state.upper = upper
numbers = st.checkbox('Numbers (0-9)', value=st.session_state.numbers)
st.session_state.numbers = numbers
symbols = st.checkbox('Symbols (!-@$+)', value=st.session_state.symbols)
st.session_state.symbols = symbols
exclude_duplicates = st.checkbox('Exclude Duplicates', value=st.session_state.exclude_duplicates)
st.session_state.exclude_duplicates = exclude_duplicates
include_spaces = st.checkbox('Include Spaces', value=st.session_state.include_spaces)
st.session_state.include_spaces = include_spaces

# Generate Password
col1, col2 = st.columns([3, 1])

with col1:
    if st.button('Generate Password'):
        if not (lower or upper or numbers or symbols or include_spaces):
            st.error('Please select at least one character set')
        else:
            try:
                password = generate_password(length, lower, upper, numbers, symbols, exclude_duplicates, include_spaces)
                st.write('Generated Password:', password)
                st.text_input('Copy Password', value=password, key='password_input')
                
                # Copy to Clipboard Button
                components.html(
                    f"""
                    <button onclick="navigator.clipboard.writeText('{password}')">Copy code</button>
                    """,
                    height=50
                )
            except Exception as e:
                st.error(f"Error generating password: {e}")


