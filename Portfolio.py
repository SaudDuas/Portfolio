import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64

# Set page configuration
st.set_page_config(page_title="My Portfolio", page_icon=":briefcase:", layout="wide")

# Hide default Streamlit style and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Dark background */
    body {
        background-color: #121212;
        color: #FFFFFF;
    }
    .main {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
    }
    /* Adjust headings color */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF;
    }
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1E1E1E;
    }
    /* Option menu styling */
    .nav-link {
        color: #FFFFFF !important;
    }
    .nav-link:hover {
        background-color: #333333 !important;
    }
    /* Button styling */
    .stButton > button {
        background-color: #333333;
        color: #FFFFFF;
    }
    .stButton > button:hover {
        background-color: #555555;
        color: #FFFFFF;
    }
    /* Input fields */
    .stTextInput > div > div > input {
        background-color: #333333;
        color: #FFFFFF;
    }
    .stTextArea > div > textarea {
        background-color: #333333;
        color: #FFFFFF;
    }
    /* Tabs styling */
    .stTabs [data-baseweb="tab"] {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #333333;
        color: #FFFFFF;
    }
    /* Remove padding around main content */
    .css-18e3th9 {
        padding: 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Define the navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Experience", "Skills", "Projects", "Contact"],
        icons=["house", "briefcase", "gear", "rocket", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
    )

# Home Page
if selected == "Home":
    st.title("Saud Alotaibi")
    st.subheader("👨‍💻 Computer Engineering Student | 📊 Aspiring Data Scientist")
    
    # Objective Section
    st.markdown("## 🌟 Objective")
    st.write("""
    Aspiring consultant with a strong background in AI, machine learning, and data analysis seeking to leverage my technical and analytical skills in management consulting roles to deliver data-driven solutions for complex business challenges.
    """)
    
    # Summary Section
    st.markdown("## 🔍 Summary")
    st.write("""
    I am a computer engineering student with a strong interest in machine learning, data analysis, and fintech. My goal is to work for a big data analysis company or start my own tech startup. I have experience in Python, machine learning, and data visualization tools such as Tableau and Power BI.
    """)
    
    # Profile Picture
    profile_pic = Image.open("cv_pic.png")  # Replace with your profile picture
    st.image(profile_pic, width=200)
    with open("SALOTAIBI_C.pdf", "rb") as file:
                btn = st.download_button(
                    label="Download Resume",
                    data=file,
                    file_name="SALOTAIBI_C.pdf",
                    mime="application/pdf"
                )


# Experience Page
elif selected == "Experience":
    st.markdown("## 💼 Experience")
    
    # KAUST/SDAIA Internship
    st.markdown("### KAUST/SDAIA Artificial Intelligence Intern")
    st.write("""
    - Developed predictive models using linear and logistic regression to solve complex business problems.
    - Contributed to computer vision techniques to improve decision-making processes.
    """)
    if st.button("View Details", key="experience1"):
        st.write("More information about the KAUST/SDAIA Artificial Intelligence Intern position.")
    
    # STC Data Analyst
    st.markdown("### STC Data Analyst (Virtual Experience)")
    st.write("""
    - Conducted in-depth data analysis and predictive modeling to build a recommendation system for STC TV.
    - Enhanced user engagement and satisfaction.
    """)
    
    # Absherthon Competition
    st.markdown("### Finalist in Absherthon 2024 Competition")
    st.write("""
    - Led a cross-functional team to design AI-driven solutions for law enforcement.
    - Improved suspect identification processes.
    """)
    if st.button("View Details", key="experience2"):
        st.write("More information about the Absherthon 2024 competition experience.")

# Skills Page
elif selected == "Skills":
    st.markdown("## 🛠️ Skills")
    
    # Create tabs for different skill categories
    tabs = st.tabs(["Programming", "Data Visualization", "Machine Learning", "Software Development"])
    
    with tabs[0]:
        st.markdown("### Programming Languages")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://img.icons8.com/color/60/000000/python.png")
            st.write("Python")
        with col2:
            st.image("https://img.icons8.com/color/60/000000/java-coffee-cup-logo.png")
            st.write("Java")
        with col3:
            st.image("https://img.icons8.com/color/60/000000/c-programming.png")
            st.write("C")

    with tabs[1]:
        st.markdown("### Data Visualization Tools")
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://img.icons8.com/color/60/000000/tableau-software.png")
            st.write("Tableau")
        with col2:
            st.image("https://img.icons8.com/color/60/000000/power-bi.png")
            st.write("Power BI")
    
    with tabs[2]:
        st.markdown("### Machine Learning Frameworks")
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://img.icons8.com/color/60/000000/tensorflow.png")
            st.write("TensorFlow")
        with col2:
            st.image("https://img.icons8.com/color/60/000000/pytorch.png")
            st.write("PyTorch")
    
    with tabs[3]:
        st.markdown("### Software Development Tools")
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://img.icons8.com/color/60/000000/git.png")
            st.write("Git")
        with col2:
            st.image("https://img.icons8.com/color/60/000000/docker.png")
            st.write("Docker")
    
    # Certifications
    st.markdown("## 🎖️ Certifications")
    st.write("""
    - **Introduction to AI** – KAUST/SDAIA
    - **Advanced AI** – KAUST/SDAIA
    - **Data Analytics Certificate** – Google
    - **McKinsey Forward Program** – McKinsey & Company
    """)

# Projects Page
elif selected == "Projects":
    st.markdown("## 🚀 Projects")
    
    # Trading Bot Project
    st.markdown("### Trading Bot")
    st.write("""
    Developed a trading bot to analyze the US stock market, providing daily buy/sell recommendations with high accuracy.
    """)
    st.image("trading_bot.png", caption="Trading Bot Project", use_column_width=True)
    if st.button("More Details", key="project1"):
        st.write("Detailed description of the Trading Bot project.")
    
    # Law Enforcement AI Project
    st.markdown("### AI-Driven Solutions for Law Enforcement")
    st.write("""
    Led a cross-functional team in the Absherthon 2024 competition, designing AI-driven solutions for law enforcement.
    """)
    st.image("law_enforcement_image.jpg", caption="AI-Driven Solutions for Law Enforcement", use_column_width=True)
    if st.button("More Details", key="project2"):
        st.write("Detailed description of the Law Enforcement AI project.")

# Contact Page
elif selected == "Contact":

# Enhanced Custom CSS for Modern Contact Form
            st.markdown("""
                <style>
                .contact-container {
                    background-color: #1E1E1E;
                    padding: 40px;
                    border-radius: 10px;
                    max-width: 600px;
                    margin: auto;
                    color: #FFFFFF;
                    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.3);
                }
                .contact-container h2 {
                    font-size: 28px;
                    font-weight: bold;
                    color: #6C63FF;
                    text-align: center;
                    margin-bottom: 20px;
                }
                .contact-container p {
                    color: #CCCCCC;
                    text-align: center;
                    margin-bottom: 30px;
                }
                label {
                    font-size: 15px;
                    color: #FFFFFF;
                    font-weight: bold;
                    display: block;
                    margin-bottom: 5px;
                }
                input[type="text"], input[type="email"], textarea {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 20px;
                    background-color: #333333;
                    border: 1px solid #444444;
                    border-radius: 5px;
                    color: #FFFFFF;
                    font-size: 15px;
                }
                input[type="text"]:focus, input[type="email"]:focus, textarea:focus {
                    border-color: #6C63FF;
                    outline: none;
                }
                button[type="submit"] {
                    background-color: #6C63FF;
                    color: #FFFFFF;
                    border: none;
                    padding: 10px 20px;
                    font-size: 16px;
                    font-weight: bold;
                    border-radius: 5px;
                    cursor: pointer;
                    width: 100%;
                }
                button[type="submit"]:hover {
                    background-color: #8a85ff;
                }
                </style>
                """, unsafe_allow_html=True)
            
            # Display Contact Form Container
            st.markdown('<div class="contact-container">', unsafe_allow_html=True)
            st.markdown('<h2>📬 Contact</h2>', unsafe_allow_html=True)
            st.markdown('<p>Fill out the form below to send me a message:</p>', unsafe_allow_html=True)
            
            # HTML Contact Form
            contact_form = """
            <form action="https://formsubmit.co/798ca3aac81c91f8fe69bfb3b6fcada0" method="POST">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message</label>
                <textarea id="message" name="message" rows="4" required></textarea>
                
                <button type="submit">Send</button>
            </form>
            """
            
            # Render the Contact Form
            st.markdown(contact_form, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            


# Footer
st.markdown("---")
st.markdown("© 2024 Saud Alotaibi")

