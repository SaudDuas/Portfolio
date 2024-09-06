import streamlit as st
from streamlit_navigation_bar import st_navbar
import streamlit_shadcn_ui as ui  # Import Shadcn UI components

# Set page configuration including favicon
st.set_page_config(page_title="My Portfolio", page_icon="favicon-32x32.png")

# Define your navigation bar
page = st_navbar(["Home", "Experience", "Education", "Skills", "Projects", "Certifications", "Contact"])

# Conditional rendering based on the selected page
if page == "Home":
    st.markdown("<h1 style='text-align: center;'>Saud Alotaibi</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>👨‍💻 Computer Engineering Student | 📊 Aspiring Data Scientist | 💼 Fintech Enthusiast</h3>", unsafe_allow_html=True)
    
    # Add alert using Shadcn UI
    ui.alert_dialog(show=ui.button(text="Latest Update", key="update_btn"), title="Portfolio Update", 
                    description="Check out my latest projects!", confirm_label="OK", key="update_dialog")

    # Combine Home and Summary content
    st.markdown("<h2 id='summary'>🔍 Summary</h2>", unsafe_allow_html=True)
    st.write("""
    I am a computer engineering student with a strong interest in machine learning, data analysis, and fintech. My goal is to work for a big data analysis company or start my own tech startup. I have experience in Python, machine learning, and data visualization tools such as Tableau and Power BI.
    """)

elif page == "Experience":
    st.markdown("<h2 id='experience'>💼 Experience</h2>", unsafe_allow_html=True)
    
    # Use Shadcn card component for experiences
    with ui.card(key="experience_card"):
        st.write("**KAUST/SDAIA Artificial Intelligence Intern**")
        st.write("Developed predictive models using linear and logistic regression to solve complex business problems.")
        ui.button(text="View Details", key="experience_details")

    with ui.card(key="absherthon_card"):
        st.write("**Finalist in Absherthon 2024 Competition**")
        st.write("Led a cross-functional team to design AI-driven solutions for law enforcement, improving suspect identification processes.")
        ui.button(text="View Details", key="absherthon_details")

elif page == "Education":
    st.markdown("<h2 id='education'>🎓 Education</h2>", unsafe_allow_html=True)
    st.write("""
    **Bachelor of Engineering (B.Eng.) in Computer Engineering**
    - King Abdulaziz University, Jeddah
    - Member of Ai Division at DRAG KAU and Engineering Innovation Club – Project Consulting
    """)
    
elif page == "Skills":
    st.markdown("<h2 id='skills'>🛠️ Skills</h2>", unsafe_allow_html=True)

    # Apply custom CSS for responsive and improved tab styles
    st.markdown("""
    <style>
    .tabs-container {
        display: flex;
        justify-content: space-around;
        width: 100%;
        flex-wrap: wrap;
    }
    .tab-button {
        padding: 10px 20px;
        border: none;
        background-color: #f0f0f0;
        font-size: 16px;
        border-radius: 8px;
        margin: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .tab-button:hover {
        background-color: #ddd;
    }
    .tab-button-selected {
        background-color: #ccc;
    }
    </style>
    """, unsafe_allow_html=True)

    # Add tabs with improved styles
    selected_tab = ui.tabs(
        options=["Programming", "Data Visualization", "Machine Learning", "Software Development"],
        key="skills_tabs"
    )
    # Display dynamic content based on the selected skill
    if selected_tab == "Programming":
        st.write("Skills: Python, Java, C++.")
    elif selected_tab == "Data Visualization":
        st.write("Tools: Tableau, Power BI.")
    elif selected_tab == "Machine Learning":
        st.write("Frameworks: TensorFlow, PyTorch.")
    elif selected_tab == "Software Development":
        st.write("Technologies: Git, Docker, CI/CD.")

    # Show the selected tab
    st.write(f"You selected: {selected_tab}")


elif page == "Projects":
    st.markdown("<h2 id='projects'>🚀 Projects</h2>", unsafe_allow_html=True)
    
    # Use Shadcn card component for project descriptions
    with ui.card(key="trading_bot_card"):
        st.write("**Trading Bot**")
        st.write("Developed a trading bot to analyze the US stock market, providing daily buy/sell recommendations with high accuracy.")
        st.image("pic1.webp", caption="Trading Bot Project", use_column_width=True)
        ui.button(text="More Details", key="trading_bot_btn")

    with ui.card(key="law_enforcement_card"):
        st.write("**AI-Driven Solutions for Law Enforcement**")
        st.write("Led a cross-functional team in the Absherthon 2024 competition, designing AI-driven solutions for law enforcement.")
        st.image("pic2.webp", caption="AI-Driven Solutions for Law Enforcement", use_column_width=True)
        ui.button(text="More Details", key="law_enforcement_btn")

elif page == "Certifications":
    st.markdown("<h2 id='certifications'>🎖️ Certifications</h2>", unsafe_allow_html=True)
    st.write("""
    - **Introduction to AI** – KAUST/SDAIA
    - **Advanced AI** – KAUST/SDAIA
    - **Data Analytics Certificate** – Google
    - **McKinsey Forward Program** – McKinsey & Company
    """)

elif page == "Contact":
    st.markdown("<h2 id='contact'>📬 Contact</h2>", unsafe_allow_html=True)
    st.write("If you're interested in connecting, please fill out the form below:")

    contact_form = st.form(key='contact_form')
    name = contact_form.text_input("Your Name")
    email = contact_form.text_input("Your Email")
    message = contact_form.text_area("Message")
    submit_button = contact_form.form_submit_button(label='Submit')

    if submit_button:
        # Sending form data to FormSubmit
        st.write(f"Thank you {name}! Your message has been sent.")
        st.markdown(f"""
        <form action="https://formsubmit.co/saud.bin.fawaz@gmail.com" method="POST" style="display:none;">
            <input type="hidden" name="_subject" value="New contact form submission from {name}">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="name" value="{name}">
            <input type="hidden" name="email" value="{email}">
            <input type="hidden" name="message" value="{message}">
            <input type="submit" value="Send">
        </form>
        <script>
        document.forms[0].submit();
        </script>
        """, unsafe_allow_html=True)
