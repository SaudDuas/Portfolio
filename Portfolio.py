import streamlit as st
from streamlit_navigation_bar import st_navbar

st.set_page_config(page_title="My Portfolio", page_icon="favicon-32x32.png")

# Define your navigation bar
page = st_navbar(["Home", "Experience", "Education", "Skills", "Projects", "Certifications", "Contact"])

# Conditional rendering based on the selected page
if page == "Home":
    st.markdown("<h1 style='text-align: center;'>Saud Alotaibi</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>👨‍💻 Computer Engineering Student | 📊 Aspiring Data Scientist | 💼 Fintech Enthusiast</h3>", unsafe_allow_html=True)
    
    # Combine Home and Summary content
    st.markdown("<h2 id='summary'>🔍 Summary</h2>", unsafe_allow_html=True)
    st.write("""
    I am a computer engineering student with a strong interest in machine learning, data analysis, and fintech. My goal is to work for a big data analysis company or start my own tech startup. I have experience in Python, machine learning, and data visualization tools such as Tableau and Power BI.
    """)

elif page == "Experience":
    st.markdown("<h2 id='experience'>💼 Experience</h2>", unsafe_allow_html=True)
    st.write("""
    **KAUST/SDAIA Artificial Intelligence Intern**
    - Developed predictive models using linear and logistic regression to solve complex business problems.
    - Applied computer vision techniques to enhance decision-making processes through advanced image analysis and object detection.

    **Finalist in Absherthon 2024 Competition**
    - Led a cross-functional team to design AI-driven solutions for law enforcement, improving suspect identification processes.
    - Demonstrated leadership and innovation by ranking within the top 9 out of 6000 participants from 56 countries.

    **Virtual Work Experience (Misk)**
    - **STC Data Analyst**: Conducted in-depth data analysis and predictive modeling to build a recommendation system for STC TV, enhancing user engagement and satisfaction.
    - **Foodics UX Designer**: Delivered insightful business recommendations through user experience testing and customer needs analysis, driving better user retention.
    """)


elif page == "Education":
    st.markdown("<h2 id='education'>🎓 Education</h2>", unsafe_allow_html=True)
    st.write("""
    **Bachelor of Engineering (B.Eng.) in Computer Engineering**
    - King Abdulaziz University, Jeddah
    - Member of Ai Division at DRAG KAU and Engineering Innovation Club – Project Consulting
    """)

elif page == "Skills":
    st.markdown("<h2 id='skills'>🛠️ Skills</h2>", unsafe_allow_html=True)
    st.write("""
    - **Programming Languages**: Python, R, SQL
    - **Data Visualization**: Tableau, Power BI
    - **Machine Learning**: Pytorch, Scikit-learn
    - **Software Development**: Git, Docker
    - **Soft Skills**: Leadership, Analytical Problem-Solving, Business Analysis
    - **Management Consulting**: Data-Driven Decision Making, Strategic Analysis
    - **Tools**: Excel, SQL, Power BI, Tableau
    """)


elif page == "Projects":
    st.markdown("<h2 id='projects'>🚀 Projects</h2>", unsafe_allow_html=True)
    st.write("""
    **Trading Bot**
    - Developed a trading bot to analyze the US stock market, providing daily buy/sell recommendations with high accuracy.
    """)
    st.image("pic1.webp", caption="Trading Bot Project", use_column_width=True)

    st.write("""**AI-Driven Solutions for Law Enforcement**
    - Led a cross-functional team in the Absherthon 2024 competition, designing AI-driven solutions for law enforcement.
    """)
    st.image("pic2.webp", caption="AI-Driven Solutions for Law Enforcement", use_column_width=True)

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
        <form action="https://formsubmit.co/saud.bin.fawaz@gmail.com" method="POST">
            <input type="hidden" name="_subject" value="New contact form submission from {name}">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="name" value="{name}">
            <input type="hidden" name="email" value="{email}">
            <input type="hidden" name="message" value="{message}">
            <input type="submit" value="Send">
        </form>
        <script>
        document.forms[0].submit(); // Automatically submit the form
        </script>
        """, unsafe_allow_html=True)