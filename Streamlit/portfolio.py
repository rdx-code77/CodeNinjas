import streamlit as st
from datetime import datetime
import os
from PIL import Image
import time  # For chat typing animation

# Configure page
st.set_page_config(
    page_title="SaiKumar Srinivas | Data Analytics Portfolio",
    page_icon="📊",
    layout="wide"
)

def local_css(file_name):
    try:
        path = os.path.join(os.path.dirname(__file__), file_name)
        with open(path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.markdown("""
        <style>
            .stApp { background-color: #f5f5f5; }
            h1 { color: #2c3e50; }
            h2 { color: #3498db; }
        </style>
        """, unsafe_allow_html=True)
        st.warning(f"CSS file '{file_name}' not found. Using basic styling.")

local_css("style.css")

# Header Section
def create_header():
    col1, col2 = st.columns([1, 3])
    with col1:
        try:
            img = Image.open("profile.jpg")
            st.image(img, width=150, caption="SaiKumar Srinivas")
        except FileNotFoundError:
            st.image(Image.new('RGB', (150, 150), caption="SaiKumar Srinivas"))

    with col2:
        st.title("Saikumar Srinivas")
        st.subheader("Data Analytics Professional")
        st.write("""
        Worcester, MA | +1 (508) 365 9639 | 
        [saikumar.srinivas123@gmail.com](mailto:saikumar.srinivas123@gmail.com) | 
        [LinkedIn](https://www.linkedin.com/in/saikumar-srinivas/) |
        [GitHub](https://github.com/rdx-code77)
        """)
        st.write("""
        Data Analyst with expertise in Snowflake, Power BI, Python, and Machine Learning. 
        Passionate about transforming data into actionable insights.
        """)

# Navigation
def create_navigation():
    st.markdown("---")
    st.sidebar.title("Navigation")
    return st.sidebar.radio("Go to", 
                          ["About", "Education", "Experience", "Projects", "Skills", "Contact", "Chat"])

# About Section
def show_about():
    st.header("About Me")
    st.write("""
    Data Analytics professional currently pursuing my Master's degree at Clark University (3.9 GPA).
    Hands-on experience in data engineering, visualization, and machine learning.
    
    Technical Expertise:
    - Data Warehousing (Snowflake, SQL)
    - Data Visualization (Power BI, Tableau)
    - Programming (Python, R, SQL)
    - Machine Learning & NLP
    - Cloud Technologies (AWS, Docker, Kubernetes)
    """)

# Education Section
def show_education():
    st.header("Education")
    
    with st.expander("Clark University, Worcester, MA", expanded=True):
        st.subheader("Master of Science in Data Analytics")
        st.write("Aug 2023 - May 2025 | CGPA: 3.9/4.0")
        st.write("""
        Courses: Mathematical Statistics, Machine Learning, Agile Methodologies, 
        Data Visualization, Business Intelligence
        """)
    
    with st.expander("AMC Engineering College, Bengaluru, India"):
        st.subheader("Bachelor of Science in Computers")
        st.write("July 2018 - Aug 2022 | CGPA: 3.7/4.0")

# Experience Section
def show_experience():
    st.header("Professional Experience")
    
    experiences = [
        {
            "title": "Code Ninjas, Northborough, MA - Program Coordinator / Data Analyst",
            "period": "Feb 2025 - Present",
            "details": [
                "Spearheaded migration from legacy billing system to Snowflake",
                "Designed efficient data models in Snowflake",
                "Automated legacy billing reconciliation",
                "Reduced pipeline latency by 40%"
            ]
        },
        {
            "title": "Clark University - Teaching Assistant in Data Visualization",
            "period": "Dec 2024 - May 2025",
            "details": [
                "Guided students in Tableau and Power BI",
                "Applied advanced visualization features",
                "Data modeling and blending"
            ]
        },
        {
            "title": "Digit Insurance - Graduate Trainee Engineer",
            "period": "Aug 2022 - Aug 2023",
            "details": [
                "Developed email ticketing system",
                "Automated web processes with Selenium",
                "Deployed applications in Docker & Kubernetes"
            ]
        }
    ]
    
    for exp in experiences:
        with st.expander(exp["title"], expanded=(exp == experiences[0])):
            st.subheader(exp["title"].split("-")[0].strip())
            st.write(exp["period"])
            for detail in exp["details"]:
                st.write(f"- {detail}")

# Projects Section
def show_projects():
    st.header("Projects")
    
    projects = [
        {
            "title": "Language Data Analytics & Computational Linguistics",
            "location": "Clark University",
            "details": [
                "Built multilingual datasets",
                "Developed statistical language models",
                "Analyzed linguistic patterns"
            ]
        },
        {
            "title": "Automated Reporting System",
            "location": "",
            "details": [
                "Python and Power BI solution",
                "Reduced reporting time by 60%",
                "Implemented data validation checks"
            ]
        }
    ]
    
    for proj in projects:
        with st.expander(proj["title"], expanded=(proj == projects[0])):
            st.subheader(proj["title"])
            if proj["location"]:
                st.write(proj["location"])
            for detail in proj["details"]:
                st.write(f"- {detail}")

# Skills Section
def show_skills():
    st.header("Technical Skills")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Programming")
        st.write("- Python\n- R\n- SQL")
        
        st.subheader("Database")
        st.write("- Snowflake\n- PostgreSQL\n- MongoDB")

    with col2:
        st.subheader("Data Tools")
        st.write("- Power BI\n- Tableau\n- Pandas\n- NumPy")
        
        st.subheader("ML/DL")
        st.write("- Scikit-learn\n- TensorFlow\n- PyTorch")

    with col3:
        st.subheader("NLP")
        st.write("- Transformers\n- NLTK\n- SpaCy")
        
        st.subheader("Cloud/DevOps")
        st.write("- AWS\n- Docker\n- Kubernetes")

# Contact Section
def show_contact():
    st.header("Contact Me")
    
    contact_form = """
    <form action="https://formsubmit.co/saikumar.srinivas123@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message"></textarea>
        <button type="submit">Send Message</button>
    </form>
    """
    
    st.markdown(contact_form, unsafe_allow_html=True)
    
    st.write("""
    ### Direct Contact:
    - Email: [saikumar.srinivas123@gmail.com](mailto:saikumar.srinivas123@gmail.com)
    - Phone: +1 (508) 365 9639
    - LinkedIn: [linkedin.com/in/saikumar-srinivas/](https://www.linkedin.com/in/saikumar-srinivas/)
    """)

# Chat Section
# Chat Section
def show_chat():
    st.header("Chat with My AI Assistant")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm an AI assistant for SaiKumar's portfolio. Ask me about his experience, skills, or projects!"}
        ]
    
    # Display chat messages
    for message in st.session_state.messages:
        # Use None for avatar to use default icons
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your question here...", key="portfolio_chat_input"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Process the user's question
                prompt_lower = prompt.lower()
                
                if any(word in prompt_lower for word in ["hi", "hello", "hey"]):
                    response = "Hello! How can I help you learn more about SaiKumar today?"
                elif any(word in prompt_lower for word in ["experience", "work", "job"]):
                    response = """**Professional Experience:**
                    - Code Ninjas: Data Analyst (Snowflake, automation)
                    - Clark University: Teaching Assistant
                    - Digit Insurance: Software Engineer"""
                elif any(word in prompt_lower for word in ["skill", "technology"]):
                    response = """**Technical Skills:**
                    - Data: Snowflake, Power BI, SQL
                    - Programming: Python, R
                    - ML: Scikit-learn, TensorFlow"""
                elif "project" in prompt_lower:
                    response = """**Projects:**
                    - Language Data Analytics
                    - Automated Reporting System"""
                elif any(word in prompt_lower for word in ["contact", "email", "phone"]):
                    response = """**Contact:**
                    Email: saikumar.srinivas123@gmail.com
                    Phone: +1 (508) 365 9639"""
                else:
                    response = "I can discuss SaiKumar's experience, skills, projects, and education. What would you like to know?"
                
                # Typing animation
                message_placeholder = st.empty()
                full_response = ""
                for chunk in response.split():
                    full_response += chunk + " "
                    message_placeholder.markdown(full_response + "▌")
                    time.sleep(0.05)
                message_placeholder.markdown(full_response)
                
                # Add to history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
# Footer
def create_footer():
    st.markdown("---")
    st.markdown(f"© {datetime.now().year} Sai Kumar Srinivas. All rights reserved.")

# Main App
def main():
    create_header()
    section = create_navigation()
    
    if section == "About":
        show_about()
    elif section == "Education":
        show_education()
    elif section == "Experience":
        show_experience()
    elif section == "Projects":
        show_projects()
    elif section == "Skills":
        show_skills()
    elif section == "Contact":
        show_contact()
    elif section == "Chat":
        show_chat()
    
    create_footer()

if __name__ == "__main__":
    main()