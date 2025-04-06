import os
from PIL import Image
import streamlit as st

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                        url("https://images.unsplash.com/photo-1504384308090-c894fdcc538d") no-repeat center center fixed;
            background-size: cover;
            color: white;
        }

        .content-block {
            background-color: rgba(255, 255, 255, 0.85); /* White with 85% opacity */
            color: black;
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1rem;
        }

        section[data-testid="stSidebar"] {
            background-color: rgba(255, 255, 255, 0.85);
        }
    </style>
""", unsafe_allow_html=True)




# Check if the image file exists
img_path = "profile-pic.png"

if not os.path.exists(img_path):
    st.error(f"Image file '{img_path}' not found. Please check the file name and location.")
else:
    img_profile = Image.open(img_path)

    # Display in the main section
    st.image(img_profile, caption="Ahmed, The Python Pro 💻", use_container_width=True)

    # --- SIDEBAR ---
    with st.sidebar:
        st.image(img_profile, width=200)
        st.title("Welcome 👋")
        st.markdown("""
            - 📊 Data Analyst  
            - 🐍 Python Developer  
            - 📍 Nigeria  
        """)
        st.write("---")
        st.write("💼 [LinkedIn](https://www.linkedin.com)")
        st.write("🌐 [GitHub](https://www.github.com)")
        st.write("📧 abubakaramoka360.com")

    # --- HEADER ---
    with st.container():
        st.markdown('<div class="content-block">', unsafe_allow_html=True)
        st.subheader("Hi, I am Ahmed 👋")
        st.title("A Data Analyst From Nigeria")
        st.write("I use Python to build smart web tools and solve real-world problems.")
        st.write("[Learn more >](https://pythonandvba.com)")
        st.markdown('</div>', unsafe_allow_html=True)


    # --- WHAT I DO ---
    with st.container():
        st.markdown('<div class="content-block">', unsafe_allow_html=True)
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I Do")
            st.write("##")
            st.write("""
                On my YouTube channel, I create tutorials for people who:
                - Want to use Python to automate their work  
                - Love building web apps with Streamlit  
                - Are interested in data analytics and visualization  
            """)
        st.markdown('</div>', unsafe_allow_html=True)

        # Make sure the second image exists
        if os.path.exists("code-screenshot.png"):
            with right_column:
                st.image("code-screenshot.png", caption="Code Preview")
        else:
            st.warning("Screenshot image not found.")

    # --- CONTACT FORM ---
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Contact Form
        contact_form = """
        <form action="https://formsubmit.co/abubakaramoka360@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Your name" required><br><br>
            <input type="email" name="email" placeholder="Your email" required><br><br>
            <textarea name="message" placeholder="Your message here" required></textarea><br><br>
            <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)
