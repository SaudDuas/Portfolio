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
    st.markdown("<h3 style='text-align: center;'>👨‍💻 Computer Engineering Student | 📊 Aspiring Data Scientist | 💼 </h3>", unsafe_allow_html=True)
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

    # Custom CSS for centering the category icon and better layout for skill icons
    st.markdown("""
    <style>
    .center-icon {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .skills-container {
        display: flex;
        justify-content: center;
        width: 100%;
        flex-wrap: wrap;
    }
    .skill-row {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 15px;
    }
    .skill-icon {
        width: 60px;
        height: 60px;
        margin-right: 20px;
    }
    .skill-text {
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # Example icons (replace with actual URLs or local images)
    icons = {
        "Programming": "https://img.icons8.com/color/48/000000/programming.png",
        "Data Visualization": "https://img.icons8.com/color/48/000000/combo-chart.png",
        "Machine Learning": "https://img.icons8.com/external-outline-juicy-fish/60/000000/external-machine-learning-education-outline-outline-juicy-fish.png",
        "Software Development": "https://img.icons8.com/color/48/000000/code.png"
    }

    # Tabs with icons
    tabs = st.tabs(["Programming", "Data Visualization", "Machine Learning", "Software Development"])

    # Tab content with category icon in the center
    with tabs[0]:
        st.markdown('<div class="center-icon"><img src="{}" width="80"></div>'.format(icons["Programming"]), unsafe_allow_html=True)
        st.write("Skills: Python, Java, C++.")
        st.markdown('<div class="skill-row"><img src="https://img.icons8.com/color/60/000000/python.png" class="skill-icon"><span class="skill-text">Python</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-row"><img src="https://img.icons8.com/color/60/000000/java-coffee-cup-logo.png" class="skill-icon"><span class="skill-text">Java</span></div>', unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="center-icon"><img src="{}" width="80"></div>'.format(icons["Data Visualization"]), unsafe_allow_html=True)
        st.write("Tools: Tableau, Power BI.")
        st.markdown('<div class="skill-row"><img src="https://img.icons8.com/color/60/000000/tableau-software.png" class="skill-icon"><span class="skill-text">Tableau</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-row"><img src="https://img.icons8.com/color/60/000000/microsoft-power-bi.png" class="skill-icon"><span class="skill-text">Power BI</span></div>', unsafe_allow_html=True)

    with tabs[2]:
        st.markdown('<div class="center-icon"><img src="{}" width="80"></div>'.format(icons["Machine Learning"]), unsafe_allow_html=True)
        st.write("Frameworks: TensorFlow, PyTorch.")
        st.markdown('<div class="skill-row"><img src="https://img.icons8.com/color/60/000000/tensorflow.png" class="skill-icon"><span class="skill-text">TensorFlow</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-row"><img src="https://img.icons8.com/color/60/000000/pytorch.png" class="skill-icon"><span class="skill-text">PyTorch</span></div>', unsafe_allow_html=True)

    with tabs[3]:
        st.markdown('<div class="center-icon"><img src="{}" width="80"></div>'.format(icons["Software Development"]), unsafe_allow_html=True)
        st.write("Technologies: Git, Docker, CI/CD.")
        st.markdown('<div class="skill-row"><img src="https://img.icons8.com/color/60/000000/git.png" class="skill-icon"><span class="skill-text">Git</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-row"><img src="https://img.icons8.com/color/60/000000/docker.png" class="skill-icon"><span class="skill-text">Docker</span></div>', unsafe_allow_html=True)


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
